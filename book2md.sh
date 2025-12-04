#!/bin/bash

################################################################################
# book2md.sh - Pure Bash implementation of book to Markdown converter
# 
# Converts EPUB, PDF, DOCX, and TXT files to Markdown chapters
# No Python required - uses only standard Unix tools
#
# Usage: ./book2md.sh <input_file> [output_dir]
#
# Dependencies:
#   - unzip (for EPUB and DOCX)
#   - pdftotext (from poppler-utils, for PDF)
#   - pandoc (optional, for better HTML->Markdown conversion)
#   - xmllint (for XML parsing in DOCX)
################################################################################

set -e  # Exit on error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
OUTPUT_DIR="output_md"
TEMP_DIR="/tmp/book2md_$$"

################################################################################
# Utility Functions
################################################################################

print_info() {
    echo -e "${BLUE}ℹ${NC} $1"
}

print_success() {
    echo -e "${GREEN}✓${NC} $1"
}

print_error() {
    echo -e "${RED}✗${NC} $1" >&2
}

print_warning() {
    echo -e "${YELLOW}⚠${NC} $1"
}

cleanup() {
    if [ -d "$TEMP_DIR" ]; then
        rm -rf "$TEMP_DIR"
    fi
}

trap cleanup EXIT

check_dependencies() {
    local missing_deps=()
    
    if ! command -v unzip &> /dev/null; then
        missing_deps+=("unzip")
    fi
    
    if ! command -v pdftotext &> /dev/null; then
        print_warning "pdftotext not found. PDF conversion will be limited."
        print_info "Install with: brew install poppler (macOS) or apt-get install poppler-utils (Linux)"
    fi
    
    if ! command -v pandoc &> /dev/null; then
        print_warning "pandoc not found. Using basic HTML->Markdown conversion."
        print_info "Install with: brew install pandoc (macOS) or apt-get install pandoc (Linux)"
    fi
    
    if [ ${#missing_deps[@]} -gt 0 ]; then
        print_error "Missing required dependencies: ${missing_deps[*]}"
        exit 1
    fi
}

sanitize_filename() {
    local text="$1"
    # Remove special characters, keep only alphanumeric, dash, and underscore
    echo "$text" | sed 's/[^a-zA-Z0-9_-]/_/g' | cut -c1-50
}

html_to_markdown() {
    local input_file="$1"
    
    if command -v pandoc &> /dev/null; then
        # Use pandoc for better conversion
        pandoc -f html -t markdown "$input_file" 2>/dev/null || cat "$input_file"
    else
        # Basic HTML tag stripping
        sed -e 's/<[^>]*>//g' \
            -e 's/&nbsp;/ /g' \
            -e 's/&lt;/</g' \
            -e 's/&gt;/>/g' \
            -e 's/&amp;/\&/g' \
            -e 's/&quot;/"/g' \
            "$input_file"
    fi
}

################################################################################
# EPUB Conversion
################################################################################

convert_epub() {
    local epub_file="$1"
    local output_dir="$2"
    
    print_info "Converting EPUB: $epub_file"
    
    # Extract EPUB (it's just a ZIP file)
    local extract_dir="$TEMP_DIR/epub"
    mkdir -p "$extract_dir"
    unzip -q "$epub_file" -d "$extract_dir"
    
    # Find content.opf to get reading order
    local opf_file=$(find "$extract_dir" -name "*.opf" | head -1)
    
    if [ -z "$opf_file" ]; then
        print_error "Could not find .opf file in EPUB"
        return 1
    fi
    
    # Extract chapter files from manifest
    local chapter_count=0
    
    # Look for HTML/XHTML files in the EPUB
    find "$extract_dir" -type f \( -name "*.html" -o -name "*.xhtml" -o -name "*.htm" \) | sort | while read -r html_file; do
        chapter_count=$((chapter_count + 1))
        
        # Extract title from HTML
        local title=$(grep -ioP '(?<=<title>)[^<]+' "$html_file" 2>/dev/null | head -1)
        if [ -z "$title" ]; then
            title=$(grep -ioP '(?<=<h1[^>]*>)[^<]+' "$html_file" 2>/dev/null | head -1)
        fi
        [ -z "$title" ] && title="Chapter $chapter_count"
        
        # Convert HTML to Markdown
        local content=$(html_to_markdown "$html_file")
        
        # Create output file
        local safe_title=$(sanitize_filename "$title")
        local output_file="$output_dir/$(printf "%02d" $chapter_count)_${safe_title}.md"
        
        echo "# $title" > "$output_file"
        echo "" >> "$output_file"
        echo "$content" >> "$output_file"
        
        print_success "Created: $output_file"
    done
}

################################################################################
# PDF Conversion
################################################################################

convert_pdf() {
    local pdf_file="$1"
    local output_dir="$2"
    
    print_info "Converting PDF: $pdf_file"
    
    if ! command -v pdftotext &> /dev/null; then
        print_error "pdftotext is required for PDF conversion"
        print_info "Install with: brew install poppler (macOS)"
        return 1
    fi
    
    # Extract text from PDF
    local text_file="$TEMP_DIR/pdf_text.txt"
    pdftotext -layout "$pdf_file" "$text_file"
    
    # Look for chapter markers
    local chapter_pattern='^\s*(CHAPTER|Chapter|PART|Part|BOOK|Book)\s+[IVXivx0-9]+'
    
    # Split by chapters
    local chapter_count=0
    local current_chapter=""
    local current_title="Introduction"
    local in_chapter=false
    
    while IFS= read -r line; do
        if echo "$line" | grep -qE "$chapter_pattern"; then
            # Save previous chapter
            if [ -n "$current_chapter" ]; then
                chapter_count=$((chapter_count + 1))
                local safe_title=$(sanitize_filename "$current_title")
                local output_file="$output_dir/$(printf "%02d" $chapter_count)_${safe_title}.md"
                
                echo "# $current_title" > "$output_file"
                echo "" >> "$output_file"
                echo "$current_chapter" >> "$output_file"
                
                print_success "Created: $output_file"
            fi
            
            # Start new chapter
            current_title=$(echo "$line" | sed -E 's/^\s*(CHAPTER|Chapter|PART|Part|BOOK|Book)\s+//')
            current_title=$(echo "$current_title" | xargs)
            current_chapter=""
            in_chapter=true
        else
            if [ "$in_chapter" = true ]; then
                current_chapter+="$line"$'\n'
            fi
        fi
    done < "$text_file"
    
    # Save last chapter
    if [ -n "$current_chapter" ]; then
        chapter_count=$((chapter_count + 1))
        local safe_title=$(sanitize_filename "$current_title")
        local output_file="$output_dir/$(printf "%02d" $chapter_count)_${safe_title}.md"
        
        echo "# $current_title" > "$output_file"
        echo "" >> "$output_file"
        echo "$current_chapter" >> "$output_file"
        
        print_success "Created: $output_file"
    fi
    
    # If no chapters found, split into chunks
    if [ $chapter_count -eq 0 ]; then
        print_warning "No chapter markers found. Splitting into auto-chunks..."
        
        local line_count=$(wc -l < "$text_file")
        local chunk_size=200
        local chunk_num=1
        
        split -l $chunk_size "$text_file" "$TEMP_DIR/chunk_"
        
        for chunk_file in "$TEMP_DIR"/chunk_*; do
            local output_file="$output_dir/$(printf "%02d" $chunk_num)_Auto_Chapter.md"
            echo "# Auto Chapter $chunk_num" > "$output_file"
            echo "" >> "$output_file"
            cat "$chunk_file" >> "$output_file"
            
            print_success "Created: $output_file"
            chunk_num=$((chunk_num + 1))
        done
    fi
}

################################################################################
# DOCX Conversion
################################################################################

convert_docx() {
    local docx_file="$1"
    local output_dir="$2"
    
    print_info "Converting DOCX: $docx_file"
    
    # Extract DOCX (it's a ZIP file)
    local extract_dir="$TEMP_DIR/docx"
    mkdir -p "$extract_dir"
    unzip -q "$docx_file" -d "$extract_dir"
    
    # The main document is in word/document.xml
    local doc_xml="$extract_dir/word/document.xml"
    
    if [ ! -f "$doc_xml" ]; then
        print_error "Could not find document.xml in DOCX"
        return 1
    fi
    
    if command -v pandoc &> /dev/null; then
        # Use pandoc for better DOCX conversion
        pandoc "$docx_file" -t markdown -o "$TEMP_DIR/docx_content.md"
        
        # Split by heading 1 markers
        local chapter_count=0
        local current_chapter=""
        local current_title="Book"
        
        while IFS= read -r line; do
            if echo "$line" | grep -q '^# '; then
                # Save previous chapter
                if [ -n "$current_chapter" ]; then
                    chapter_count=$((chapter_count + 1))
                    local safe_title=$(sanitize_filename "$current_title")
                    local output_file="$output_dir/$(printf "%02d" $chapter_count)_${safe_title}.md"
                    
                    echo "# $current_title" > "$output_file"
                    echo "" >> "$output_file"
                    echo "$current_chapter" >> "$output_file"
                    
                    print_success "Created: $output_file"
                fi
                
                # Start new chapter
                current_title=$(echo "$line" | sed 's/^# //')
                current_chapter=""
            else
                current_chapter+="$line"$'\n'
            fi
        done < "$TEMP_DIR/docx_content.md"
        
        # Save last chapter
        if [ -n "$current_chapter" ]; then
            chapter_count=$((chapter_count + 1))
            local safe_title=$(sanitize_filename "$current_title")
            local output_file="$output_dir/$(printf "%02d" $chapter_count)_${safe_title}.md"
            
            echo "# $current_title" > "$output_file"
            echo "" >> "$output_file"
            echo "$current_chapter" >> "$output_file"
            
            print_success "Created: $output_file"
        fi
        
        # If no chapters, create single file
        if [ $chapter_count -eq 0 ]; then
            local output_file="$output_dir/01_Book.md"
            cp "$TEMP_DIR/docx_content.md" "$output_file"
            print_success "Created: $output_file"
        fi
    else
        # Fallback: extract text from XML
        print_warning "Using basic XML extraction (install pandoc for better results)"
        
        local output_file="$output_dir/01_Book.md"
        echo "# Book" > "$output_file"
        echo "" >> "$output_file"
        
        # Extract text from w:t tags
        if command -v xmllint &> /dev/null; then
            xmllint --xpath "//w:t/text()" "$doc_xml" 2>/dev/null >> "$output_file" || \
            grep -oP '(?<=<w:t>)[^<]+' "$doc_xml" >> "$output_file"
        else
            grep -oP '(?<=<w:t>)[^<]+' "$doc_xml" >> "$output_file"
        fi
        
        print_success "Created: $output_file"
    fi
}

################################################################################
# TXT Conversion
################################################################################

convert_txt() {
    local txt_file="$1"
    local output_dir="$2"
    
    print_info "Converting TXT: $txt_file"
    
    # Look for chapter markers
    local chapter_pattern='^\s*(Chapter|CHAPTER|Part|PART|Book|BOOK)\s+[IVXivx0-9]+'
    
    local chapter_count=0
    local current_chapter=""
    local current_title="Book"
    local in_chapter=false
    
    while IFS= read -r line; do
        if echo "$line" | grep -qE "$chapter_pattern"; then
            # Save previous chapter
            if [ -n "$current_chapter" ]; then
                chapter_count=$((chapter_count + 1))
                local safe_title=$(sanitize_filename "$current_title")
                local output_file="$output_dir/$(printf "%02d" $chapter_count)_${safe_title}.md"
                
                echo "# $current_title" > "$output_file"
                echo "" >> "$output_file"
                echo "$current_chapter" >> "$output_file"
                
                print_success "Created: $output_file"
            fi
            
            # Start new chapter
            current_title=$(echo "$line" | sed -E 's/^\s*(Chapter|CHAPTER|Part|PART|Book|BOOK)\s+//')
            current_title=$(echo "$current_title" | xargs)
            current_chapter=""
            in_chapter=true
        else
            current_chapter+="$line"$'\n'
        fi
    done < "$txt_file"
    
    # Save last chapter
    if [ -n "$current_chapter" ]; then
        chapter_count=$((chapter_count + 1))
        local safe_title=$(sanitize_filename "$current_title")
        local output_file="$output_dir/$(printf "%02d" $chapter_count)_${safe_title}.md"
        
        echo "# $current_title" > "$output_file"
        echo "" >> "$output_file"
        echo "$current_chapter" >> "$output_file"
        
        print_success "Created: $output_file"
    fi
    
    # If no chapters found, treat as single file
    if [ $chapter_count -eq 0 ]; then
        local output_file="$output_dir/01_Book.md"
        echo "# Book" > "$output_file"
        echo "" >> "$output_file"
        cat "$txt_file" >> "$output_file"
        
        print_success "Created: $output_file"
    fi
}

################################################################################
# Main Logic
################################################################################

show_usage() {
    echo "Usage: $0 <input_file> [output_dir]"
    echo ""
    echo "Convert books to Markdown chapters"
    echo ""
    echo "Supported formats: .epub, .pdf, .docx, .txt"
    echo ""
    echo "Arguments:"
    echo "  input_file    Path to the book file"
    echo "  output_dir    Output directory (default: output_md)"
    echo ""
    echo "Examples:"
    echo "  $0 mybook.epub"
    echo "  $0 document.pdf chapters/"
    echo ""
}

main() {
    # Check arguments
    if [ $# -lt 1 ]; then
        show_usage
        exit 1
    fi
    
    local input_file="$1"
    local output_dir="${2:-$OUTPUT_DIR}"
    
    # Check if input file exists
    if [ ! -f "$input_file" ]; then
        print_error "File not found: $input_file"
        exit 1
    fi
    
    # Check dependencies
    check_dependencies
    
    # Create output directory
    mkdir -p "$output_dir"
    
    # Create temp directory
    mkdir -p "$TEMP_DIR"
    
    # Get file extension
    local extension="${input_file##*.}"
    extension=$(echo "$extension" | tr '[:upper:]' '[:lower:]')
    
    echo ""
    print_info "📘 Book to Markdown Converter"
    print_info "Input: $input_file"
    print_info "Output: $output_dir/"
    echo ""
    
    # Convert based on file type
    case "$extension" in
        epub)
            convert_epub "$input_file" "$output_dir"
            ;;
        pdf)
            convert_pdf "$input_file" "$output_dir"
            ;;
        docx)
            convert_docx "$input_file" "$output_dir"
            ;;
        txt)
            convert_txt "$input_file" "$output_dir"
            ;;
        *)
            print_error "Unsupported file format: .$extension"
            print_info "Supported formats: .epub, .pdf, .docx, .txt"
            exit 1
            ;;
    esac
    
    echo ""
    print_success "✅ Conversion complete!"
    print_info "Output directory: $output_dir/"
    
    # Count output files
    local file_count=$(find "$output_dir" -name "*.md" | wc -l)
    print_info "Generated $file_count Markdown files"
    echo ""
}

# Run main function
main "$@"
