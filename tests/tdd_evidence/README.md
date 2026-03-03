# TDD Evidence

This folder stores red/green evidence for key paths required by strict TDD policy.

## Red phase

- `red_phase_1.log`
  - Failing collection due to missing modules (`ocr_utils`, `pdf_processing`)
  - Represents the initial Red state before implementing OCR workflow and PDF strategy modules.

## Green phase

- `green_phase_1.log`
  - Passing tests for key paths:
    - OCR detection and trigger paths
    - OCR intermediate recovery path
    - TOC depth adaptive fallback (30 -> 50)
    - Outline split path
    - Skill runner enum/unknown-argument validation

## Related test files

- `tests/test_pdf_ocr_detection.py`
- `tests/test_pdf_ocr_workflow.py`
- `tests/test_pdf_intermediate_recovery.py`
- `tests/test_pdf_toc_depth_fallback.py`
- `tests/test_pdf_outline_split.py`
- `tests/test_skill_schema_and_runner.py`
