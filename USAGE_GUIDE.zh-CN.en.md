# book2md 使用指南（中文 + English）

> 本文档是本项目的完整双语使用指南。  
> This document is the complete bilingual usage guide for this project.

## 1. 项目简介 | Project Overview

`book2md` 用于将书籍文件转换为按章节拆分的 Markdown 文件，支持两种实现方式：

- Python CLI（`main.py` + `book_converter.py`）
- Bash 脚本（`book2md.sh`）

`book2md` converts book files into chapter-based Markdown files with two implementations:

- Python CLI (`main.py` + `book_converter.py`)
- Bash script (`book2md.sh`)

适用场景：

- 将 EPUB/PDF/DOCX/TXT 转为可编辑 Markdown
- 后续用于知识库、笔记系统、AI 处理流水线

Use cases:

- Convert EPUB/PDF/DOCX/TXT into editable Markdown
- Feed outputs into knowledge bases, note systems, or AI pipelines

## 2. 功能与格式支持 | Features and Format Support

### 2.1 支持格式 | Supported Formats

- `.epub`
- `.pdf`
- `.docx`
- `.txt`

### 2.2 输出规则 | Output Rules

- 输出目录默认 `output_md/`
- 文件命名：`01_<chapter_title>.md`、`02_<chapter_title>.md` ...
- 每个文件内容：
  - 第一行 `# 章节标题`
  - 后续为章节正文

- Default output directory: `output_md/`
- Filename pattern: `01_<chapter_title>.md`, `02_<chapter_title>.md` ...
- Each file contains:
  - First line: `# Chapter Title`
  - Then chapter body

### 2.3 两种实现对比 | Python vs Bash

- Python 版本：
  - 结构清晰，易扩展
  - 对 EPUB/DOCX 结构化解析更友好
- Bash 版本：
  - 依赖少，启动快
  - 适合纯命令行环境快速批处理

- Python version:
  - Cleaner architecture, easier to extend
  - Better structured parsing for EPUB/DOCX
- Bash version:
  - Fewer dependencies, quick startup
  - Great for shell-heavy batch workflows

## 3. 环境准备 | Environment Setup

## 3.1 Python 版本依赖 | Python Dependencies

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

可选（不激活虚拟环境时）：

```bash
.venv/bin/python --version
```

Optional (without activating venv):

```bash
.venv/bin/python --version
```

## 3.2 Bash 版本依赖 | Bash Dependencies

必须：

- `unzip`

推荐：

- `pdftotext`（PDF）
- `pandoc`（更好的 HTML/DOCX 转 Markdown）

Required:

- `unzip`

Recommended:

- `pdftotext` (PDF)
- `pandoc` (better HTML/DOCX to Markdown conversion)

## 4. 快速开始 | Quick Start

### 4.1 Python CLI 快速转换 | Quick Conversion with Python CLI

```bash
.venv/bin/python main.py convert test_book.txt -o output_md
```

### 4.2 Bash 快速转换 | Quick Conversion with Bash

```bash
chmod +x book2md.sh
./book2md.sh test_book.txt output_md
```

## 5. 命令用法详解 | CLI Usage Details

### 5.1 Python 命令格式 | Python Command Syntax

```bash
.venv/bin/python main.py convert <input_file> [OPTIONS]
```

参数：

- `input_file`：输入书籍文件路径（必须存在）
- `--outdir`, `-o`：输出目录（默认 `output_md`）

Arguments:

- `input_file`: path to source book file (must exist)
- `--outdir`, `-o`: output directory (default: `output_md`)

查看帮助：

```bash
.venv/bin/python main.py convert --help
```

Show help:

```bash
.venv/bin/python main.py convert --help
```

### 5.2 常用示例 | Common Examples

```bash
# EPUB
.venv/bin/python main.py convert "/path/to/book.epub" -o "/path/to/out_epub"

# PDF
.venv/bin/python main.py convert "/path/to/book.pdf" -o "/path/to/out_pdf"

# DOCX
.venv/bin/python main.py convert "/path/to/book.docx" -o "/path/to/out_docx"

# TXT
.venv/bin/python main.py convert "/path/to/book.txt" -o "/path/to/out_txt"
```

### 5.3 Bash 脚本示例 | Bash Script Examples

```bash
./book2md.sh "/path/to/book.epub" "/path/to/out_epub"
./book2md.sh "/path/to/book.pdf" "/path/to/out_pdf"
./book2md.sh "/path/to/book.docx" "/path/to/out_docx"
./book2md.sh "/path/to/book.txt" "/path/to/out_txt"
```

## 6. 手动验证流程 | Manual Validation Workflow

建议每次改动后按以下步骤验证：

1. 用 Python 版本转换一个 `TXT`（小文件）
2. 检查输出目录是否生成多个编号 `.md`
3. 打开首个/末尾章节检查标题和正文
4. 再转换一个 `EPUB` 或 `DOCX` 做交叉验证

Recommended verification after changes:

1. Convert a small `TXT` with Python
2. Confirm multiple numbered `.md` files are created
3. Open first/last chapters to validate title/body
4. Convert one `EPUB` or `DOCX` for cross-checking

## 7. 自动化测试 | Automated Tests

运行测试：

```bash
.venv/bin/pytest -q
```

Run tests:

```bash
.venv/bin/pytest -q
```

当前测试主要覆盖 TXT 章节切分逻辑（包括回归场景）。

Current tests mainly cover TXT chapter splitting (including regression cases).

## 8. 章节识别说明 | Chapter Detection Behavior

### 8.1 TXT（Python）

- 识别 `Chapter/Part/Book + 编号` 形式的行作为章节标题
- 若未匹配到章节标记，则整个文件作为一个章节输出

### 8.2 PDF（Python）

- 尝试识别 `CHAPTER/Chapter/Part/PART/BOOK/Book`
- 若识别失败，按固定词数自动分块输出

### 8.3 DOCX（Python）

- 优先依据 `Heading 1` 拆章
- 没有标题样式时，退化为单章节输出

### 8.4 EPUB（Python）

- 优先使用 TOC
- 无 TOC 时遍历文档条目兜底

### 8.1 TXT (Python)

- Detects lines matching `Chapter/Part/Book + token` as chapter titles
- Falls back to single chapter if no markers are found

### 8.2 PDF (Python)

- Tries `CHAPTER/Chapter/Part/PART/BOOK/Book` markers
- Falls back to fixed-size auto chunks when no markers are found

### 8.3 DOCX (Python)

- Splits by `Heading 1`
- Falls back to single chapter when no heading style is detected

### 8.4 EPUB (Python)

- Uses TOC first
- Falls back to iterating document items

## 9. 常见问题与排障 | Troubleshooting

### 9.1 `ModuleNotFoundError`

原因：未安装依赖或未使用项目虚拟环境。  
解决：

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Cause: dependencies missing or wrong Python interpreter.  
Fix:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 9.2 PDF 转换质量不稳定

- 检查 PDF 是否为扫描件（可能需要 OCR）
- 尝试 Bash 版本 + `pdftotext -layout`

- Check whether the PDF is scanned (OCR may be required)
- Try Bash flow with `pdftotext -layout`

### 9.3 DOCX 未按章节拆分

- 确保文档使用了 `Heading 1`
- 否则会被视为连续正文

- Ensure chapter titles use `Heading 1`
- Otherwise the document may be treated as continuous content

## 10. 项目结构与入口 | Project Structure and Entry Points

```text
book-transfer/
├── main.py                # Python CLI entry
├── book_converter.py      # Core conversion logic
├── book2md.sh             # Bash implementation
├── tests/                 # Pytest tests
├── requirements.txt       # Python dependencies
├── README.md              # Project index and quick navigation
└── USAGE_GUIDE.zh-CN.en.md
```

## 11. 开发与扩展建议 | Development and Extension Notes

- 新增格式时，优先在 Python 版本添加新的 `Book` 子类并注册到 `BookFactory`
- 对章节识别规则的改动，应同步补充测试用例
- 保持输出命名约定，避免下游流程破坏

- For new formats, add a new `Book` subclass and register it in `BookFactory`
- Add tests whenever chapter detection rules change
- Keep output naming conventions stable for downstream compatibility

## 12. 相关文档 | Related Documents

- 项目索引：`README.md`
- Bash 说明：`BASH_VERSION.md`
- 项目概览：`PROJECT_SUMMARY.md`

- Project index: `README.md`
- Bash docs: `BASH_VERSION.md`
- Project summary: `PROJECT_SUMMARY.md`
