# TDD Policy (Strict)

## Scope

This project follows strict TDD for core conversion paths, especially PDF/OCR and skill invocation.

## Required Cycle

For each feature or bug fix:

1. Write a failing test first (`Red`).
2. Implement the minimal code to pass (`Green`).
3. Refactor while keeping tests green (`Refactor`).

No direct implementation-only changes are allowed on critical paths.

## Coverage Gate

- Line coverage must stay `>= 90%`.
- CI must fail when coverage drops below the threshold.

Recommended command:

```bash
.venv/bin/pytest --cov=main --cov=book_converter --cov=pdf_processing --cov=ocr_utils --cov=chapter_utils --cov-fail-under=90 -q
```

## Red-Path Evidence

Keep lightweight artifacts under `tests/tdd_evidence/` for critical paths:

1. OCR detection and trigger branches.
2. PDF `auto` fallback chain (`outline -> toc -> heading -> chunk`).
3. Skill schema + runner validation path.

Evidence can be command logs or concise notes proving red-to-green progression.

## Review Checklist

- Tests added before implementation for new behavior.
- No uncovered branch introduced in critical paths.
- Error messages include recovery hints when expensive OCR already succeeded.
