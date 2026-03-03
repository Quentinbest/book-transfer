# 使用指南 | Usage Guide

> 本文档以“先能跑、再可控、最后可扩展”为目标，覆盖安装、运行、策略、排障与验证。

## 1. 环境准备 | Environment

### 1.1 Python 依赖

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 1.2 OCR 依赖（处理扫描 PDF 必需）

```bash
# macOS
brew install ocrmypdf

# Ubuntu/Debian
sudo apt-get install ocrmypdf
```

### 1.3 可选：验证工具

```bash
which ocrmypdf
.venv/bin/python --version
```

## 2. 命令与参数 | Command and Options

基础命令：

```bash
.venv/bin/python main.py convert <input_file> [OPTIONS]
```

参数：

- `--outdir, -o`：输出目录（默认 `output_md`）
- `--chapter-mode`：`auto|outline|toc|heading|chunk`（默认 `auto`）
- `--ocr`：`auto|force|off`（默认 `auto`）
- `--ocr-lang`：OCR 语言（默认 `chi_sim+eng`）
- `--keep-intermediate`：成功后保留中间文件
- `--chunk-words`：`chunk` 分割词数（默认 `4000`）
- `--toc-max-pages`：TOC 首轮扫描页数（默认 `30`）

## 3. 常用场景 | Common Scenarios

### 3.1 普通文本书籍（TXT/EPUB/DOCX）

```bash
.venv/bin/python main.py convert ./book.txt -o ./out/txt
.venv/bin/python main.py convert ./book.epub -o ./out/epub
.venv/bin/python main.py convert ./book.docx -o ./out/docx
```

### 3.2 PDF 自动流程（推荐）

```bash
.venv/bin/python main.py convert ./book.pdf -o ./out/pdf --chapter-mode auto --ocr auto
```

### 3.3 强制 OCR（疑似扫描件）

```bash
.venv/bin/python main.py convert ./scan.pdf -o ./out/scan --ocr force
```

### 3.4 禁用 OCR（已知文本 PDF）

```bash
.venv/bin/python main.py convert ./text.pdf -o ./out/text --ocr off
```

### 3.5 只用 TOC 策略

```bash
.venv/bin/python main.py convert ./book.pdf -o ./out/toc --chapter-mode toc --toc-max-pages 40
```

## 4. PDF 策略说明 | PDF Strategy

### 4.1 `chapter-mode=auto` 降级链

固定顺序：

1. `outline`
2. `toc`
3. `heading`
4. `chunk`

### 4.2 OCR 自动判定

采样前 20 页，指标：

- `avg_chars_per_page`
- `empty_page_ratio`
- `full_page_image_ratio`

逻辑：

- 若字符密度低或空页比例高，进入疑似扫描。
- 再看整页主图像比例是否足够高。
- 命中则 OCR；否则按普通 PDF 继续分章。

### 4.3 TOC 自适应深度

- 首轮：`1..toc_max_pages`。
- 失败：扩展到 `1..50`，并使用轻量匹配。
- 仍失败：降级 `heading`。

### 4.4 OCR 崩溃恢复

- 临时目录由系统 `tempfile` 生成（前缀 `book-transfer-`）。
- OCR 完成后若下游失败，会保留 `ocr_output.pdf` 并提示可复用路径。
- 同时写入 `run.log` 便于复现。

## 5. Skill 调用 | Agent Skill

安装：

```bash
bash scripts/install_skill.sh
```

Skill 路径：`~/.codex/skills/book-transfer-converter`

关键约束：

- `agents/openai.yaml`：enum + `additionalProperties: false`
- `run_book_transfer.sh`：参数白名单、enum 校验、正整数校验、固定命令模板

## 6. 手动测试清单 | Manual Test Checklist

1. `--ocr off` 处理文本 PDF，确认不触发 OCR。
2. `--ocr auto` 处理扫描 PDF，确认 OCR 后正常拆章。
3. 构造下游失败，确认错误提示包含可复用 OCR 文件路径。
4. 验证 `auto` 降级链：outline/toc/heading/chunk。
5. Skill Runner 传非法参数，确认立即失败。

## 7. 自动化测试 | Automated Testing

```bash
.venv/bin/pytest -q
.venv/bin/pytest --cov=main --cov=book_converter --cov=pdf_processing --cov=ocr_utils --cov=chapter_utils --cov-fail-under=90 -q
```

## 8. 关键文档 | Related Docs

- 架构：`docs/ARCHITECTURE.md`
- 业务流程：`docs/BUSINESS_LOGIC.md`
- 开发运维：`docs/DEVELOPER_RUNBOOK.md`
- TDD 规范：`docs/TDD_POLICY.md`
- Bash 差异：`BASH_VERSION.md`

