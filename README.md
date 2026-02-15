# book2md

Convert EPUB, PDF, DOCX, and TXT books into chapter-based Markdown files.

## Documentation

- Comprehensive bilingual guide (中文 + English):
  - `USAGE_GUIDE.zh-CN.en.md`
- Bash-specific notes:
  - `BASH_VERSION.md`
- Project summary:
  - `PROJECT_SUMMARY.md`

## Quick Start (Python)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
.venv/bin/python main.py convert test_book.txt -o output_md
```

## Quick Start (Bash)

```bash
chmod +x book2md.sh
./book2md.sh test_book.txt output_md
```

## CLI

```bash
.venv/bin/python main.py convert --help
.venv/bin/python main.py convert <input_file> -o <outdir>
```

## Tests

```bash
.venv/bin/pytest -q
```

## Behavior Notes

- TXT chapter behavior is aligned between Python and Bash:
  - If chapter markers exist, text before the first marker is not emitted as a separate chapter.
  - If no markers exist, the whole file is emitted as a single `Book` chapter.

## Core Files

- `main.py`: CLI entrypoint
- `book_converter.py`: conversion core
- `book2md.sh`: shell implementation
- `tests/`: pytest suite for TXT/PDF/DOCX/EPUB behaviors
