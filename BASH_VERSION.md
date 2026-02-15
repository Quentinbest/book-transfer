# Bash Shell Version - book2md.sh

## Overview

`book2md.sh` is a **pure Bash shell script** implementation that converts books to Markdown chapters **without requiring Python**. It uses only standard Unix command-line tools.

## Features

✅ **No Python Required** - Pure Bash implementation  
✅ **Same Functionality** - Converts EPUB, PDF, DOCX, TXT to Markdown  
✅ **Chapter Detection** - Smart chapter splitting with fallback  
✅ **Cross-Platform** - Works on macOS and Linux  

## Dependencies

### Required

- **unzip** - For EPUB and DOCX extraction (usually pre-installed)

### Recommended

- **pdftotext** (from poppler-utils) - For PDF conversion
  ```bash
  # macOS
  brew install poppler
  
  # Ubuntu/Debian
  sudo apt-get install poppler-utils
  ```

- **pandoc** - For better HTML→Markdown conversion
  ```bash
  # macOS
  brew install pandoc
  
  # Ubuntu/Debian
  sudo apt-get install pandoc
  ```

### Optional

- **xmllint** - For better DOCX parsing (usually pre-installed)

## Installation

```bash
# Make the script executable
chmod +x book2md.sh
```

## Usage

### Basic Usage

```bash
# Convert to default output directory (output_md/)
./book2md.sh mybook.epub

# Specify custom output directory
./book2md.sh mybook.pdf chapters/

# Convert different formats
./book2md.sh document.docx output/
./book2md.sh notes.txt markdown/
```

### Help

```bash
./book2md.sh --help
```

## How It Works

### EPUB Conversion
1. Extracts EPUB archive using `unzip` (EPUB is a ZIP file)
2. Finds all HTML/XHTML chapter files
3. Extracts chapter titles from `<title>` or `<h1>` tags
4. Converts HTML to Markdown using `pandoc` (if available) or basic regex
5. Creates numbered Markdown files

### PDF Conversion
1. Extracts text using `pdftotext` with layout preservation
2. Searches for chapter markers: `CHAPTER`, `Chapter`, `Part`, `PART`, `BOOK`, `Book`
3. Splits content by detected chapters
4. Falls back to auto-chunking if no chapters found (~200 lines per chunk)

### DOCX Conversion
1. Extracts DOCX archive using `unzip` (DOCX is a ZIP file)
2. Uses `pandoc` to convert to Markdown (if available)
3. Splits by Heading 1 markers (`# `)
4. Falls back to XML text extraction if pandoc unavailable

### TXT Conversion
1. Reads plain text file
2. Searches for chapter markers using regex
3. Splits content by detected chapters (when markers exist, preface text before the first marker is not emitted as a separate chapter)
4. Falls back to single-file output if no chapters found

## Output Format

Generated files follow the same naming convention as the Python version:

```
output_md/
├── 01_Introduction.md
├── 02_Getting_Started.md
├── 03_Advanced_Topics.md
└── ...
```

Each file contains:
- `# Chapter Title` (H1 heading)
- Chapter content in Markdown

Filenames are sanitized (special characters → underscores) and limited to 50 characters.

## Comparison with Python Version

| Feature | Python Version | Bash Version |
|---------|---------------|--------------|
| Installation | `pip install` multiple packages | Native tools only |
| Dependencies | ebooklib, beautifulsoup4, markdownify, etc. | unzip, pdftotext, pandoc |
| Speed | Fast | Very fast (native tools) |
| HTML→MD Quality | High (markdownify) | Good (pandoc) |
| Portability | Requires Python 3.7+ | Works anywhere with Bash |
| Maintenance | Object-oriented, modular | Single script, procedural |

## Troubleshooting

### "pdftotext not found"
Install poppler-utils:
```bash
# macOS
brew install poppler

# Linux
sudo apt-get install poppler-utils
```

### "pandoc not found"
The script will work with basic HTML stripping, but pandoc provides better conversion:
```bash
# macOS
brew install pandoc

# Linux
sudo apt-get install pandoc
```

### Poor PDF extraction
- Scanned PDFs may need OCR pre-processing
- Try using `pdftotext -layout` manually to check text quality
- Adjust `chunk_size` in the script if needed

### EPUB not extracting chapters
- Some EPUBs have non-standard structures
- The script processes all HTML files found
- Check that the EPUB is not DRM-protected

### DOCX extraction limited
Without pandoc, only plain text is extracted. Install pandoc for:
- Proper formatting preservation
- Heading detection
- Better structure

## Advanced Usage

### Check dependencies before conversion
```bash
# Test which tools are available
command -v unzip && echo "✓ unzip"
command -v pdftotext && echo "✓ pdftotext"
command -v pandoc && echo "✓ pandoc"
```

### Process multiple files
```bash
# Convert all EPUBs in a directory
for book in books/*.epub; do
    ./book2md.sh "$book" "output/$(basename "$book" .epub)/"
done
```

### Custom chapter patterns
Edit the script to modify chapter detection regex:
```bash
# Line ~223 and ~389
chapter_pattern='^\s*(CHAPTER|Chapter|PART|Part|BOOK|Book)\s+[IVXivx0-9]+'
```

## Integration with Python Version

Both versions can coexist:

```bash
# Use Bash version (no dependencies)
./book2md.sh mybook.epub

# Use Python version (better quality)
python3 main.py convert mybook.epub
```

Choose based on your needs:
- **Bash version**: Quick conversions, minimal setup, shell scripting workflows
- **Python version**: Better accuracy, programmatic access, easier to extend

## Contributing

To improve the Bash version:

1. **Better HTML parsing**: Consider using `xmlstarlet` or `xml2`
2. **Improved chapter detection**: Add more sophisticated regex patterns
3. **Performance**: Optimize for large files
4. **Error handling**: Add more validation and user feedback

## License

Same as the main project - open source, modify and use as needed.
