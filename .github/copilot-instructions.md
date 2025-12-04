## Repository context and goals

This is a small CLI utility (single-file) for converting books (EPUB, PDF, TXT, DOCX) into Markdown chapters. The main entrypoint is `book2.py` which exposes a Click-based CLI command `convert` that writes chapter Markdown files to an output directory.

## Key files

- `book2.py` — single source of truth. Contains readers for EPUB (`read_epub`), PDF (`read_pdf`), DOCX (`read_docx`), and TXT (`read_txt` / `read_txt_chapters`) plus `extract_chapters` dispatch and the `click` CLI.

## High-level architecture / data flow

- Input: a file path supplied to `book2.py convert <input_file>`.
- Dispatch: `extract_chapters(filepath)` chooses reader by file extension and returns List[Tuple[title, markdown_content]].
- Output: the CLI serializes each (title, content) pair to a numbered Markdown file (safe filename via regex) in `output_md` or `--outdir`.

Design notes for contributors/agents:
- Each reader returns the same shape: list of `(title, content)` tuples (strings). Keep this contract when changing or adding readers.
- EPUB uses EbookLib + BeautifulSoup + `markdownify` to produce markdown from HTML; preserve that flow when improving formatting.
- PDF extraction is heuristic: it aggregates text from pdfminer pages and attempts to detect large-font headings or Chapter/Part patterns. Be conservative changing the regex or heuristics and keep chunking fallback logic intact.

## Project-specific conventions and patterns

- Filenames: safe title computed with `re.sub(r"[^a-zA-Z0-9_-]+", "_", title)[:50]` and prefixed by a two-digit index (`{i:02d}_`).
- DOCX reading groups paragraphs by heading styles detected with `para.style.name` (checks for 'heading' and '1'). When modifying, preserve behavior for missing styles (falls back to collecting paragraphs).
- TXT fallback: `read_txt_chapters` uses a multiline regex on lines starting with `Chapter|CHAPTER|Part|...`. If no matches, the whole file becomes a single chapter.
- PDF fallback: if heading regex fails, the code splits the full text into chunks of ~4000 words (controlled by `chunk_size`).

## Dependencies and setup (how to run locally)

- Important runtime deps (search `book2.py` imports): `ebooklib`, `beautifulsoup4`, `markdownify`, `pdfminer.six`, `python-docx`, `click`.
- Typical local setup:
  - Create a venv: `python3 -m venv .venv && source .venv/bin/activate`
  - Install deps: `pip install ebooklib beautifulsoup4 markdownify pdfminer.six python-docx click`

## How to run (useful commands)

- Convert a single file: `python3 book2.py convert sample.epub -o outdir`
- Run as script (if executable): `./book2.py convert book.pdf`. The script begins with a shebang so it can be made executable.

## Editing guidance for AI agents (practical rules)

1. Preserve the `(title, content)` return shape when editing or adding readers. Tests and the CLI assume a list of tuples.
2. When changing EPUB handling, provide a small example in the PR showing before/after for a real EPUB item (title extraction + markdown fragments) because formatting regressions are easy.
3. If you alter PDF heuristics, include unit-like checks showing the regex or chunk behavior on sample text: e.g., use a synthetic string with `CHAPTER 1` markers and validate `read_pdf` (or extract_pages mocking) returns expected chapters.
4. Keep CLI output messages (icons/emojis) or document their removal in the PR description — users expect the current prompts like `📘 Converting:` and `✅ Conversion complete.`

## Where to add tests and what to test

- Add small pytest tests under `tests/` (not present yet). Minimal, fast tests to add:
  - `test_dispatch.py`: verify `extract_chapters` returns the expected reader for `.epub`, `.pdf`, `.txt`, `.docx` using temp files or mocks.
  - `test_read_txt_chapters.py`: feed a multi-chapter TXT string to `read_txt_chapters` and assert titles/content boundaries.
  - `test_read_docx_heading_split.py`: create a small in-memory docx (or include a fixture) and assert heading-based splitting.

## Integration and external considerations

- PDF parsing depends on `pdfminer.six` APIs (`extract_pages`, `LTTextContainer`) — tests should mock PDF layout objects where possible to avoid heavy binary fixtures.
- EPUB relies on EbookLib's `book.toc` structure. Some EPUBs have missing TOC; the code falls back to iterating `book.get_items_of_type(epub.ITEM_DOCUMENT)` — keep that fallback.

## PR and review checklist for agent-created changes

- Keep changes to `book2.py` minimal and well-documented.
- Provide example input and a short before/after snippet for any change that touches text extraction or markdown formatting.
- Add or update tests for parsing behavior where heuristics are changed.

---

If anything important is missing or you want the instructions expanded (e.g., add a sample `requirements.txt` or example EPUB fixture), tell me which area to expand and I will update this file.
