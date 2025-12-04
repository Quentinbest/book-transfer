# book2md Project Summary

## 📚 Overview

This project provides **two complete implementations** for converting books (EPUB, PDF, DOCX, TXT) into Markdown chapter files:

1. **🐍 Python Version** - Object-oriented, full-featured implementation
2. **🔧 Bash Version** - Pure shell script, zero Python dependencies

## 🗂️ Project Structure

```
book-transfer/
├── 🐍 Python Implementation
│   ├── main.py                    # CLI entry point
│   ├── book_converter.py          # Core conversion logic
│   │   ├── Book (ABC)             # Abstract base class
│   │   ├── EpubBook               # EPUB reader
│   │   ├── DocxBook               # DOCX reader
│   │   ├── PdfBook                # PDF reader
│   │   ├── TxtBook                # TXT reader
│   │   ├── BookFactory            # Factory pattern
│   │   ├── MarkdownWriter         # Output writer
│   │   └── BookConverter          # Orchestrator
│   └── requirements.txt           # Python dependencies
│
├── 🔧 Bash Implementation
│   ├── book2md.sh                 # Pure Bash script (~600 lines)
│   └── BASH_VERSION.md            # Bash documentation
│
├── 📖 Documentation
│   ├── README.md                  # Main documentation
│   └── INSTALL.md                 # Installation guide (from refactor.sh)
│
├── 🧪 Test Files
│   ├── test_book.txt              # Sample test file
│   └── test_output/               # Test conversion output
│
└── 📦 Utilities
    └── refactor.sh                # Package structure refactoring script
```

## 🚀 Quick Start

### Python Version

```bash
# Setup
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Convert
python3 main.py convert mybook.epub -o output/
```

### Bash Version

```bash
# No setup needed! Just run:
./book2md.sh mybook.epub output/

# Install optional dependencies for better quality:
brew install poppler pandoc  # macOS
```

## 🎯 Feature Comparison

| Feature | Python 🐍 | Bash 🔧 |
|---------|----------|---------|
| **EPUB Support** | ✅ Full TOC parsing | ✅ Archive extraction |
| **PDF Support** | ✅ pdfminer.six | ✅ pdftotext |
| **DOCX Support** | ✅ python-docx | ✅ unzip + pandoc |
| **TXT Support** | ✅ Regex parsing | ✅ Regex parsing |
| **HTML→MD** | ✅ markdownify | ✅ pandoc/basic |
| **Dependencies** | 6 Python packages | Native Unix tools |
| **Installation** | pip install | chmod +x |
| **Code Structure** | OOP (Factory + Strategy) | Procedural |
| **Lines of Code** | ~240 (modular) | ~600 (single file) |

## 📋 Supported Formats

### EPUB (.epub)
- **Python**: Uses `ebooklib` for full TOC structure parsing
- **Bash**: Extracts ZIP, processes HTML files with `unzip` + `pandoc`

### PDF (.pdf)
- **Python**: `pdfminer.six` for layout-aware text extraction
- **Bash**: `pdftotext` with layout preservation

### DOCX (.docx)
- **Python**: `python-docx` for reading document structure
- **Bash**: Extracts ZIP, uses `pandoc` or XML parsing

### TXT (.txt)
- **Python**: Regex-based chapter detection
- **Bash**: Regex-based chapter detection (similar logic)

## 🧩 Design Patterns (Python Version)

### Factory Pattern
```python
BookFactory.create_book(filepath)
# Returns: EpubBook | DocxBook | PdfBook | TxtBook
```

### Strategy Pattern
Each book type implements `extract_chapters()`:
```python
class Book(ABC):
    @abstractmethod
    def extract_chapters(self) -> List[Tuple[str, str]]:
        pass
```

### Single Responsibility
- `BookFactory` - Creates readers
- `Book` subclasses - Extract content
- `MarkdownWriter` - Writes files
- `BookConverter` - Orchestrates

## 📊 Usage Examples

### Basic Conversion

```bash
# Python
python3 main.py convert book.epub

# Bash
./book2md.sh book.epub
```

### Custom Output Directory

```bash
# Python
python3 main.py convert book.pdf -o chapters/

# Bash
./book2md.sh book.pdf chapters/
```

### Batch Processing (Bash)

```bash
# Convert all EPUBs in a directory
for book in books/*.epub; do
    ./book2md.sh "$book" "output/$(basename "$book" .epub)/"
done
```

## 🔧 Dependencies

### Python Version
```
ebooklib==0.20
beautifulsoup4==4.14.2
markdownify==1.2.2
pdfminer.six==20251107
python-docx==1.2.0
click==8.3.1
```

### Bash Version
**Required:**
- `unzip` (usually pre-installed)

**Recommended:**
- `pdftotext` (poppler-utils) - For PDF support
- `pandoc` - For better HTML→Markdown conversion

**Optional:**
- `xmllint` - For better DOCX parsing

## 📝 Output Format

Both versions produce identical output:

```
output_md/
├── 01_Introduction.md
├── 02_Getting_Started.md
├── 03_Advanced_Concepts.md
└── ...
```

Each file:
```markdown
# Chapter Title

Chapter content in Markdown format...
```

## ✅ Verification

Test with provided sample file:

```bash
# Test Python version
python3 main.py convert test_book.txt test_python/

# Test Bash version
./book2md.sh test_book.txt test_bash/

# Compare outputs
diff -r test_python/ test_bash/
```

Both should produce identical chapter splits!

## 🎓 Learning Resources

- **Factory Pattern**: `BookFactory` in `book_converter.py`
- **Strategy Pattern**: `Book` subclasses implementing different extraction strategies
- **Bash Scripting**: `book2md.sh` demonstrates advanced Bash techniques
- **Text Processing**: Regex-based chapter detection in both versions

## 🤝 Contributing

To extend the project:

**Python:**
1. Add new `Book` subclass for new format
2. Update `BookFactory.create_book()`
3. Add tests in `tests/`

**Bash:**
1. Add new `convert_format()` function
2. Update file extension case statement
3. Test with sample files

## 📄 License

Open source - modify and use as needed.

## 🔗 Key Files

- **[README.md](file:///Users/quentin/workspace/pythonspace/book-transfer/README.md)** - Main documentation
- **[BASH_VERSION.md](file:///Users/quentin/workspace/pythonspace/book-transfer/BASH_VERSION.md)** - Bash-specific docs
- **[main.py](file:///Users/quentin/workspace/pythonspace/book-transfer/main.py)** - Python CLI
- **[book_converter.py](file:///Users/quentin/workspace/pythonspace/book-transfer/book_converter.py)** - Python core logic
- **[book2md.sh](file:///Users/quentin/workspace/pythonspace/book-transfer/book2md.sh)** - Bash implementation

---

**Choose your version and start converting! 📚→📝**
