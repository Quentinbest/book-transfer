# 开发与运维手册

## 1. 本地开发

### 1.1 初始化

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 1.2 快速验证

```bash
.venv/bin/python main.py convert ./test_book.txt -o ./out/dev
```

## 2. 测试策略

### 2.1 全量测试

```bash
.venv/bin/pytest -q
```

### 2.2 覆盖率门禁

```bash
.venv/bin/pytest --cov=main --cov=book_converter --cov=pdf_processing --cov=ocr_utils --cov=chapter_utils --cov-fail-under=90 -q
```

### 2.3 关键路径回归

```bash
.venv/bin/pytest -q \
  tests/test_pdf_ocr_detection.py \
  tests/test_pdf_ocr_workflow.py \
  tests/test_pdf_intermediate_recovery.py \
  tests/test_pdf_toc_depth_fallback.py \
  tests/test_pdf_outline_split.py \
  tests/test_skill_schema_and_runner.py
```

## 3. 常见问题排障

### 3.1 `ocrmypdf is required`

- 原因：系统未安装 OCR 工具。
- 处理：安装 `ocrmypdf`，再执行转换。

### 3.2 OCR 很慢

- 扫描 PDF OCR 是 CPU 密集型，耗时取决于页数和分辨率。
- 建议先用较小样本验证参数。

### 3.3 OCR 后下游失败

- 错误信息应包含 `Reusable file: <path>`。
- 可直接复用该 OCR 产物再次运行，缩短重试时间。

### 3.4 TOC 未命中

- 提高 `--toc-max-pages`（如 40）。
- 或使用 `--chapter-mode heading` / `--chapter-mode chunk`。

## 4. Skill 维护

### 4.1 安装/更新

```bash
bash scripts/install_skill.sh
```

### 4.2 校验 schema 与 runner

```bash
.venv/bin/pytest -q tests/test_skill_schema_and_runner.py
```

### 4.3 关键约束

- `openai.yaml`：严格 enum + `additionalProperties: false`
- `run_book_transfer.sh`：禁止未知参数 + 固定命令模板

## 5. 提交流程建议

1. 先跑全量测试。
2. 再跑覆盖率门禁。
3. 文档更新需同步 `README.md` 与 `USAGE_GUIDE.zh-CN.en.md`。
4. 推送前检查是否误提交 `.coverage` 与 `__pycache__`。

