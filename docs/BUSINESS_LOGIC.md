# 业务逻辑说明（重点：PDF）

## 1. 总体处理流程

```mermaid
flowchart TD
    A["读取输入文件"] --> B{"文件类型"}
    B -->|"epub"| E1["EPUB 提取章节"]
    B -->|"docx"| E2["DOCX 提取章节"]
    B -->|"txt"| E3["TXT 提取章节"]
    B -->|"pdf"| P1["进入 PDF 流程"]

    E1 --> W["写出 markdown"]
    E2 --> W
    E3 --> W
    P1 --> W
```

## 2. PDF 核心业务流程

```mermaid
flowchart TD
    A["Input PDF"] --> B{"ocr_mode"}
    B -->|"force"| C["执行 OCR"]
    B -->|"off"| D["跳过 OCR"]
    B -->|"auto"| E["扫描判定"]

    E --> E1["avg_chars_per_page"]
    E --> E2["empty_page_ratio"]
    E --> E3["full_page_image_ratio"]
    E1 --> F{"疑似扫描?"}
    E2 --> F
    F -->|"否"| D
    F -->|"是"| G{"图像比高?"}
    E3 --> G
    G -->|"是"| C
    G -->|"否"| D

    C --> H["chapter_mode 分章"]
    D --> H

    H --> I{"chapter_mode"}
    I -->|"auto"| J["outline"]
    J -->|"失败"| K["toc 首轮: 1..toc_max_pages"]
    K -->|"失败"| K2["toc 二轮: 1..50 轻量匹配"]
    K2 -->|"失败"| L["heading"]
    L -->|"失败"| M["chunk"]

    I -->|"outline"| J
    I -->|"toc"| K
    I -->|"heading"| L
    I -->|"chunk"| M

    J -->|"成功"| N["写出章节 markdown"]
    K -->|"成功"| N
    K2 -->|"成功"| N
    L -->|"成功"| N
    M --> N
```

## 3. 关键业务规则

### 3.1 OCR 决策规则

- 强制模式：`--ocr force`，无条件 OCR。
- 关闭模式：`--ocr off`，无条件不 OCR。
- 自动模式：先看文本稀疏性，再看整页主图像比例，避免把“图文混排但非扫描件”误判为扫描件。

### 3.2 TOC 自适应规则

- `toc` 首轮扫描 `1..toc_max_pages`。
- 未命中时扩展至 `1..50`，并采用轻量过滤（只快速识别目录页特征）。
- 仍失败才降级 `heading`。

### 3.3 崩溃恢复规则

- OCR 成功后若下游失败：
  - 保留 `ocr_output.pdf`
  - 错误信息中输出可复用路径
  - `run.log` 落盘异常信息

## 4. Skill 业务调用逻辑

```mermaid
sequenceDiagram
    participant Agent as AI Agent
    participant Runner as run_book_transfer.sh
    participant CLI as main.py
    participant Core as book_converter/pdf_processing

    Agent->>Runner: 传入参数
    Runner->>Runner: 白名单/enum/数值校验
    Runner->>CLI: 调用 convert 命令
    CLI->>Core: 执行转换
    Core-->>CLI: 返回章节结果
    CLI-->>Runner: 退出码 + 输出
    Runner-->>Agent: 成功/失败结果
```

