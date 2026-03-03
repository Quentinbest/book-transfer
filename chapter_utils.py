import re
from typing import Iterable


def sanitize_title_for_filename(title: str, limit: int = 90) -> str:
    """Sanitize chapter title for markdown filenames."""
    safe = re.sub(r"[^0-9A-Za-z\u4e00-\u9fff_-]+", "_", title).strip("_")
    return (safe or "Chapter")[:limit]


def unique_sorted_ranges(starts: Iterable[int], total_pages: int) -> list[int]:
    """Normalize chapter start pages to sorted unique page indexes (1-based)."""
    cleaned = sorted({p for p in starts if isinstance(p, int) and 1 <= p <= total_pages})
    if not cleaned:
        return [1]
    if cleaned[0] != 1:
        cleaned.insert(0, 1)
    return cleaned
