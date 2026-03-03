import os
import shutil
import subprocess
from dataclasses import dataclass

from pdfminer.high_level import extract_text


@dataclass
class OCRDetectionMetrics:
    avg_chars_per_page: float
    empty_page_ratio: float
    full_page_image_ratio: float
    sampled_pages: int
    is_scanned: bool


def classify_scan_from_metrics(
    avg_chars_per_page: float,
    empty_page_ratio: float,
    full_page_image_ratio: float,
    text_threshold: float = 80.0,
    empty_ratio_threshold: float = 0.7,
    image_ratio_threshold: float = 0.6,
) -> bool:
    """Classify a PDF as scanned based on text + full-page-image heuristic."""
    suspected = (avg_chars_per_page < text_threshold) or (empty_page_ratio > empty_ratio_threshold)
    if not suspected:
        return False
    return full_page_image_ratio >= image_ratio_threshold


def _sample_text_metrics(pdf_path: str, sample_pages: int = 20) -> tuple[float, float, int]:
    chars = []
    empties = 0
    sampled = 0
    for i in range(sample_pages):
        text = (extract_text(pdf_path, page_numbers=[i]) or "").strip()
        if not text and i >= 2:
            # Assume we reached the end if several trailing pages are empty.
            break
        sampled += 1
        chars.append(len(text))
        if not text:
            empties += 1
    if sampled == 0:
        return 0.0, 1.0, 0
    return sum(chars) / sampled, empties / sampled, sampled


def _safe_get_page_size(page) -> tuple[float, float]:
    mbox = page.mediabox
    return float(mbox.width), float(mbox.height)


def _is_full_page_image(page, image_obj) -> bool:
    page_w, page_h = _safe_get_page_size(page)
    img_w = getattr(image_obj, "width", 0) or 0
    img_h = getattr(image_obj, "height", 0) or 0
    if page_w <= 0 or page_h <= 0 or img_w <= 0 or img_h <= 0:
        return False
    ratio_w = img_w / page_w
    ratio_h = img_h / page_h
    return ratio_w >= 0.8 and ratio_h >= 0.8


def _has_single_main_full_page_image(page, images) -> bool:
    full = [img for img in images if _is_full_page_image(page, img)]
    # Scanned pages are usually one dominant image per page.
    if len(full) != 1:
        return False
    return len(images) <= 2


def _sample_full_page_image_ratio(pdf_path: str, sample_pages: int = 20) -> float:
    try:
        from pypdf import PdfReader
    except Exception:
        return 0.0

    reader = PdfReader(pdf_path)
    page_count = min(len(reader.pages), sample_pages)
    if page_count == 0:
        return 0.0

    hit = 0
    for i in range(page_count):
        page = reader.pages[i]
        images = list(getattr(page, "images", []) or [])
        if not images:
            continue
        if _has_single_main_full_page_image(page, images):
            hit += 1
    return hit / page_count


def detect_scanned_pdf(pdf_path: str, sample_pages: int = 20) -> OCRDetectionMetrics:
    avg_chars, empty_ratio, sampled = _sample_text_metrics(pdf_path, sample_pages=sample_pages)
    image_ratio = _sample_full_page_image_ratio(pdf_path, sample_pages=sample_pages)
    scanned = classify_scan_from_metrics(avg_chars, empty_ratio, image_ratio)
    return OCRDetectionMetrics(
        avg_chars_per_page=avg_chars,
        empty_page_ratio=empty_ratio,
        full_page_image_ratio=image_ratio,
        sampled_pages=sampled,
        is_scanned=scanned,
    )


def ensure_ocrmypdf_available() -> None:
    if shutil.which("ocrmypdf"):
        return
    raise RuntimeError(
        "ocrmypdf is required for scanned PDF OCR. "
        "Install it with `brew install ocrmypdf` (macOS) or `apt install ocrmypdf` (Linux)."
    )


def run_ocr_ocrmypdf(input_pdf: str, output_pdf: str, ocr_lang: str = "chi_sim+eng") -> None:
    ensure_ocrmypdf_available()
    cmd = [
        "ocrmypdf",
        "--skip-text",
        "--force-ocr",
        "--language",
        ocr_lang,
        input_pdf,
        output_pdf,
    ]
    subprocess.run(cmd, check=True, text=True, capture_output=True, env=os.environ.copy())
