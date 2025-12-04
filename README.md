# book2md — Convert books to Markdown

> A Python CLI tool to convert EPUB, PDF, DOCX, and TXT books into individual Markdown chapter files.

This tool uses an object-oriented architecture with the Factory and Strategy patterns to support multiple book formats. The main entry point is `main.py`, with all conversion logic in `book_converter.py`.

## Quick Start

### 1. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install ebooklib beautifulsoup4 markdownify pdfminer.six python-docx click
```

### 3. Convert a book

```bash
# Convert an EPUB file
python3 main.py convert sample.epub -o outdir

# Convert a PDF
python3 main.py convert book.pdf -o chapters

# Use the venv Python directly
.venv/bin/python main.py convert book.docx
```

## CLI Usage

View available options:

```bash
python3 main.py convert --help
```

**Command:**

```bash
python3 main.py convert <input_file> [OPTIONS]
```

**Options:**
- `--outdir`, `-o` — Output directory (default: `output_md`)

**Supported formats:** `.epub`, `.pdf`, `.docx`, `.txt`

## Output Format

The tool generates numbered Markdown files for each chapter:

- `01_Introduction.md`
- `02_Getting_Started.md`
- `03_Advanced_Topics.md`

Each file contains:
- An H1 heading with the chapter title
- The chapter content in Markdown format

Filenames are sanitized using `re.sub(r"[^a-zA-Z0-9_-]+", "_", title)[:50]` and prefixed with a zero-padded chapter index.

## Architecture

The project uses a clean object-oriented design:

### Core Components

**[main.py](file:///Users/quentin/workspace/pythonspace/book-transfer/main.py)**
- CLI entry point using Click
- Defines the `convert` command
- Delegates to `BookConverter`

**[book_converter.py](file:///Users/quentin/workspace/pythonspace/book-transfer/book_converter.py)**
- `Book` (ABC) — Abstract base class for all book types
- `EpubBook` — EPUB extraction using `ebooklib`
- `DocxBook` — DOCX extraction using `python-docx`
- `PdfBook` — PDF extraction using `pdfminer.six`
- `TxtBook` — Plain text processing
- `BookFactory` — Creates appropriate book reader based on file extension
- `MarkdownWriter` — Writes chapters to Markdown files
- `BookConverter` — Orchestrates the conversion process

### Format-Specific Extraction

**EPUB (`.epub`)**
- Uses `ebooklib` to read the EPUB file
- Attempts to extract chapters from the Table of Contents (TOC)
- Falls back to iterating all document items if TOC is unavailable
- Converts HTML content to Markdown using `BeautifulSoup` + `markdownify`

**DOCX (`.docx`)**
- Uses `python-docx` to read Word documents
- Splits chapters based on **Heading 1** paragraph styles
- Falls back to treating entire document as one chapter if no headings found

**PDF (`.pdf`)**
- Uses `pdfminer.six` to extract text from pages
- Applies regex pattern matching to detect chapter markers:
  - `CHAPTER`, `Chapter`, `Part`, `PART`, `BOOK`, `Book`
- Auto-splits into 4000-word chunks if no chapter markers detected

**TXT (`.txt`)**
- Reads plain text files with UTF-8 encoding
- Uses multiline regex to find chapter markers
- Falls back to treating entire file as one chapter

## Design Patterns

- **Factory Pattern**: `BookFactory` creates the appropriate book reader based on file extension
- **Strategy Pattern**: Each book format implements its own `extract_chapters()` method
- **Single Responsibility**: Separate classes for reading, writing, and orchestration

## Troubleshooting

**EPUB issues:**
- If no chapters are extracted, the EPUB may lack a TOC structure
- The code automatically falls back to processing all document items

**PDF issues:**
- Text extraction quality depends on the PDF format
- Scanned PDFs may require OCR pre-processing
- Adjust regex patterns in `PdfBook.extract_chapters()` if needed

**DOCX issues:**
- Chapter splitting relies on Heading 1 styles
- If styles are inconsistent, entire document may be treated as one chapter

## Development

### Project Structure

```
book-transfer/
├── main.py              # CLI entry point
├── book_converter.py    # Core conversion logic
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── outdir/             # Default output directory
```

### Design Constraints

- All book readers must return `List[Tuple[str, str]]` (title, content pairs)
- Maintain HTML→Markdown conversion quality for EPUB files
- Document any changes to PDF/TXT heuristics with examples

### Testing

No tests are currently implemented. Suggested test coverage:

- `test_factory.py` — Verify `BookFactory` creates correct reader by extension
- `test_epub_extraction.py` — Test TOC parsing and fallback behavior
- `test_docx_heading_split.py` — Validate Heading 1 detection
- `test_pdf_chapter_detection.py` — Test regex patterns with synthetic data
- `test_txt_chapter_parsing.py` — Validate chapter marker detection

## Dependencies

See [requirements.txt](file:///Users/quentin/workspace/pythonspace/book-transfer/requirements.txt):

- `ebooklib==0.20` — EPUB file reading
- `beautifulsoup4==4.14.2` — HTML parsing
- `markdownify==1.2.2` — HTML to Markdown conversion
- `pdfminer.six==20251107` — PDF text extraction
- `python-docx==1.2.0` — DOCX file reading
- `click==8.3.1` — CLI framework

## License

Open source - modify and use as needed.

---

For bug reports, feature requests, or contributions, please open an issue or pull request.
