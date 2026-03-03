---
name: book-transfer-converter
description: Convert EPUB/PDF/DOCX/TXT books into chapter-level markdown files. Automatically run OCR for scanned PDF files before chapter splitting. Use this when users ask to split books by chapters, especially scanned PDFs.
---

# Book Transfer Converter

## Trigger

Use this skill when the user asks to:
- split ebook files into chapter markdown files
- process scanned/photocopy PDF files with OCR before splitting
- run book-transfer conversion with specific chapter strategy or OCR mode

## Workflow

1. Validate input path exists.
2. Validate enum options and numeric ranges (no free-form flags).
3. Run `scripts/run_book_transfer.sh` with validated parameters.
3. Prefer defaults:
- `--chapter-mode auto`
- `--ocr auto`
- `--ocr-lang chi_sim+eng`
4. Return output directory and generated file count.

## Allowed enum values

- `--chapter-mode`: `auto|outline|toc|heading|chunk`
- `--ocr`: `auto|force|off`

## Guardrails

- Reject unknown options.
- Use a fixed command template; do not execute arbitrary command fragments.
- Preserve compatibility for baseline call: `main.py convert <input> -o <outdir>`.

For full option details, read `references/options.md`.
