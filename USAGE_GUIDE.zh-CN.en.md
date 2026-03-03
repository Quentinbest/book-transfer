# book-transfer 使用指南 | book-transfer User Guide

> 本文档是项目主 README，提供中英文双语的完整使用说明。  
> This README is the canonical bilingual usage guide for this repository.

## 1. 项目目标 | Project Goal

`book-transfer` 将 EPUB/PDF/DOCX/TXT 电子书拆分为按章节组织的 `.md` 文件，重点增强了 PDF 流程：

- 更细粒度分章（书签/目录/标题/分块多级降级）
- 扫描版 PDF 的 OCR 前置处理
- OCR 之后异常的可恢复中间产物
- 可被 AI Agent 通过 Skill 稳定调用

`book-transfer` converts EPUB/PDF/DOCX/TXT books into chapter-level `.md` files with a hardened PDF pipeline:

- finer chapter splitting (outline/TOC/heading/chunk fallback chain)
- OCR-first flow for scanned PDFs
- crash-recoverable OCR intermediate files
- stable agent invocation through an installable Skill

## 2. 支持范围 | Supported Scope

### 2.1 输入格式 | Input Formats

- `.epub`
- `.pdf`
- `.docx`
- `.txt`

### 2.2 输出格式 | Output Format

- 输出目录默认：`output_md/`
- 文件命名：`01_<chapter_title>.md`, `02_<chapter_title>.md`, ...
- 单文件结构：
  - 第一行：`# 章节标题`
  - 其余：章节正文

- Default output directory: `output_md/`
- Filename pattern: `01_<chapter_title>.md`, `02_<chapter_title>.md`, ...
- Per file:
  - First line: `# Chapter Title`
  - Remaining content: chapter body

## 3. 安装与环境 | Setup

### 3.1 Python 主线（推荐） | Python Mainline (Recommended)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3.2 OCR 依赖 | OCR Dependency

扫描 PDF 需要 `ocrmypdf`（不会自动安装）：

```bash
# macOS
brew install ocrmypdf

# Ubuntu/Debian
sudo apt-get install ocrmypdf
```

Scanned PDF OCR requires `ocrmypdf` (not auto-installed):

```bash
# macOS
brew install ocrmypdf

# Ubuntu/Debian
sudo apt-get install ocrmypdf
```

### 3.3 Bash 版本依赖 | Bash Version Dependencies

见 `BASH_VERSION.md`。Bash 版本不是 Python 主线的等价实现。

See `BASH_VERSION.md`. The Bash implementation is not feature-equivalent to the Python mainline.

## 4. 快速开始 | Quick Start

```bash
.venv/bin/python main.py convert test_book.txt -o output_md
```

PDF（自动策略 + OCR 自动判定）：

```bash
.venv/bin/python main.py convert "/path/to/book.pdf" -o "/path/to/out"
```

PDF (auto strategy + auto OCR detection):

```bash
.venv/bin/python main.py convert "/path/to/book.pdf" -o "/path/to/out"
```

## 5. CLI 参数 | CLI Options

命令格式：

```bash
.venv/bin/python main.py convert <input_file> [OPTIONS]
```

参数：

- `--outdir, -o`：输出目录（默认 `output_md`）
- `--chapter-mode [auto|outline|toc|heading|chunk]`（默认 `auto`）
- `--ocr [auto|force|off]`（默认 `auto`）
- `--ocr-lang TEXT`（默认 `chi_sim+eng`）
- `--keep-intermediate`（默认关闭）
- `--chunk-words INT`（默认 `4000`）
- `--toc-max-pages INT`（默认 `30`）

Options:

- `--outdir, -o`: output directory (default `output_md`)
- `--chapter-mode [auto|outline|toc|heading|chunk]` (default `auto`)
- `--ocr [auto|force|off]` (default `auto`)
- `--ocr-lang TEXT` (default `chi_sim+eng`)
- `--keep-intermediate` (off by default)
- `--chunk-words INT` (default `4000`)
- `--toc-max-pages INT` (default `30`)

示例：

```bash
# 强制 OCR
.venv/bin/python main.py convert book.pdf -o out --ocr force

# 关闭 OCR，直接分章
.venv/bin/python main.py convert book.pdf -o out --ocr off

# 只使用 TOC 策略，并把 TOC 首轮扫描页数提高到 40
.venv/bin/python main.py convert book.pdf -o out --chapter-mode toc --toc-max-pages 40
```

## 6. PDF 分章与 OCR 策略 | PDF Splitting and OCR Strategy

### 6.1 `chapter-mode=auto` 固定降级链 | Fixed Fallback Chain

顺序固定：

1. `outline`（PDF 书签）
2. `toc`（目录页）
3. `heading`（正文标题）
4. `chunk`（按词数切块）

Order is fixed:

1. `outline` (PDF bookmarks)
2. `toc` (table of contents pages)
3. `heading` (body headings)
4. `chunk` (word-count chunking)

### 6.2 OCR 自动判定（双特征） | OCR Auto Detection (Dual Feature)

对前 20 页采样，计算：

- `avg_chars_per_page`
- `empty_page_ratio`
- `full_page_image_ratio`

规则：

- 当 `avg_chars_per_page < 80` 或 `empty_page_ratio > 0.7` 时，进入疑似扫描判定。
- 若同时 `full_page_image_ratio >= 0.6`，判定为扫描件并触发 OCR。
- 否则视作“稀疏文本/混合 PDF”，不强制 OCR，继续分章。

Rules:

- If `avg_chars_per_page < 80` or `empty_page_ratio > 0.7`, mark as scan-suspected.
- If `full_page_image_ratio >= 0.6`, classify as scanned and run OCR.
- Otherwise treat as sparse/hybrid text PDF and continue without forced OCR.

### 6.3 TOC 自适应深度 | Adaptive TOC Depth

- 首轮扫描：`1..toc_max_pages`（默认 30 页）
- 未命中时扩展：`1..50` 页（轻量匹配）
- 仍失败才降级到 `heading`

- First pass: `1..toc_max_pages` (default 30 pages)
- If no TOC hit: extend to `1..50` pages (lightweight matching)
- Fall back to `heading` only if still not found

### 6.4 OCR 中间文件恢复机制 | OCR Intermediate Recovery

临时目录：`/tmp/book-transfer-<run-id>/`

- 成功结束：`--keep-intermediate` 决定是否清理
- 失败结束：若 OCR 已成功，会保留 `ocr_output.pdf`，并在错误信息中给出可复用路径与 `run.log`

Temp directory: `/tmp/book-transfer-<run-id>/`

- On success: cleaned unless `--keep-intermediate`
- On failure: if OCR succeeded, `ocr_output.pdf` is preserved and surfaced in the error message with `run.log`

## 7. Agent Skill 调用 | Agent Skill Usage

### 7.1 安装 Skill

```bash
bash scripts/install_skill.sh
```

安装目标：`~/.codex/skills/book-transfer-converter`

Install target: `~/.codex/skills/book-transfer-converter`

### 7.2 Skill 约束

Skill 包含两层防护：

1. `agents/openai.yaml`
   - `chapter_mode` / `ocr_mode` 为严格 enum
   - `input_schema.additionalProperties: false`
2. `scripts/run_book_transfer.sh`
   - 参数白名单（未知参数直接报错）
   - enum 校验 + 正整数校验
   - 固定命令模板构造

The skill has two guardrail layers:

1. `agents/openai.yaml`
   - strict enums for `chapter_mode` / `ocr_mode`
   - `input_schema.additionalProperties: false`
2. `scripts/run_book_transfer.sh`
   - argument whitelist (unknown args rejected)
   - enum + positive integer validation
   - fixed command template

## 8. 测试与质量门禁 | Testing and Quality Gate

### 8.1 运行全量测试 | Run Full Test Suite

```bash
.venv/bin/pytest -q
```

### 8.2 覆盖率门禁（>= 90%） | Coverage Gate (>= 90%)

```bash
.venv/bin/pytest --cov=main --cov=book_converter --cov=pdf_processing --cov=ocr_utils --cov=chapter_utils --cov-fail-under=90 -q
```

### 8.3 CI

GitHub Actions 工作流：`.github/workflows/ci.yml`。  
CI 会执行测试并强制 `--cov-fail-under=90`。

GitHub Actions workflow: `.github/workflows/ci.yml`.  
CI runs tests and enforces `--cov-fail-under=90`.

### 8.4 TDD 规范

详见 `docs/TDD_POLICY.md` 与 `tests/tdd_evidence/`。

See `docs/TDD_POLICY.md` and `tests/tdd_evidence/`.

## 9. 手动测试建议 | Manual Verification Checklist

1. 使用普通文本 PDF，运行：`--ocr off`，确认不触发 OCR。
2. 使用扫描 PDF，运行：`--ocr auto`，确认 OCR 后能成功拆章。
3. 制造 downstream 异常，确认报错含 `Reusable file:` 绝对路径。
4. 对同一本 PDF 分别测试 `outline/toc/heading/chunk`，确认输出行为符合预期。
5. 验证 Skill runner：传非法参数应直接失败。

1. For text PDF, run with `--ocr off` and confirm no OCR.
2. For scanned PDF, run with `--ocr auto` and confirm OCR-first split.
3. Force downstream failure and verify `Reusable file:` absolute path in error.
4. Run `outline/toc/heading/chunk` modes on one PDF and compare output behavior.
5. Validate skill runner: invalid args should fail immediately.

## 10. Bash 版本说明 | Bash Version Note

Bash 版本用于轻量场景，不包含 Python 主线的完整 OCR 自动判定、恢复编排与 Skill 安全约束。详见 `BASH_VERSION.md`。

The Bash version targets lightweight workflows and does not provide full Python-mainline OCR heuristics, recovery orchestration, or skill guardrails. See `BASH_VERSION.md`.

## 11. 相关文件 | Key Files

- `main.py`
- `book_converter.py`
- `pdf_processing.py`
- `ocr_utils.py`
- `skills/book-transfer-converter/`
- `docs/TDD_POLICY.md`
- `tests/`
