# Book Transfer Options

- `--chapter-mode`: `auto|outline|toc|heading|chunk`
- `--ocr`: `auto|force|off`
- `--ocr-lang`: OCR language codes for ocrmypdf/tesseract (default: `chi_sim+eng`)
- `--keep-intermediate`: preserve intermediate OCR files
- `--chunk-words`: chunk fallback size (default `4000`)
- `--toc-max-pages`: initial TOC scan depth (default `30`, adaptive retry to `50`)

## Override Rules

- `--ocr force`: always run OCR first for PDF.
- `--ocr off`: never run OCR, even if scan heuristics say scanned.
- `--chapter-mode auto`: fixed fallback chain `outline -> toc -> heading -> chunk`.
- Unknown args are rejected by `scripts/run_book_transfer.sh`.
