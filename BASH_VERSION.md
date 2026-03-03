# Bash Version Notes - `book2md.sh`

## 1. Positioning

`book2md.sh` is a lightweight shell implementation for quick conversions when Python dependencies are unavailable.

`book2md.sh` 是轻量 Bash 版本，适用于无法使用 Python 依赖时的快速转换。

## 2. Feature Difference vs Python Mainline

Bash version is **not** feature-equivalent to Python mainline (`main.py` + `book_converter.py`).

Bash 版本与 Python 主线并非等价实现。

### 2.1 What Python Mainline Has (Bash Does Not)

- Strict PDF strategy chain: `outline -> toc -> heading -> chunk`
- OCR auto detection by dual heuristics (`text density + full-page image ratio`)
- OCR crash recovery and reusable intermediate path reporting
- Skill package + schema/runner guardrails for AI agent invocation
- TDD-first test matrix and enforced coverage gate (>= 90%)

### 2.2 What Bash Version Provides

- Basic EPUB/PDF/DOCX/TXT conversion
- Shell-friendly operation with minimal dependencies
- Simple chapter marker splitting and chunk fallback

## 3. Dependencies

Required:

- `unzip`

Recommended:

- `pdftotext` (PDF extraction)
- `pandoc` (HTML/DOCX to Markdown quality)

OCR for scanned PDFs is not automatically orchestrated by Bash version.

Bash 版本不提供自动 OCR 编排。

## 4. Usage

```bash
chmod +x book2md.sh
./book2md.sh <input_file> [output_dir]
```

Examples:

```bash
./book2md.sh mybook.epub out_epub
./book2md.sh mybook.pdf out_pdf
./book2md.sh mybook.docx out_docx
./book2md.sh mybook.txt out_txt
```

## 5. Recommendation

For production workflows, scanned PDFs, and AI-agent tool calls, use Python mainline:

```bash
.venv/bin/python main.py convert <input_file> -o <outdir>
```

对于生产场景、扫描 PDF、Agent 调用，推荐 Python 主线。
