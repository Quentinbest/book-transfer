import pytest

from ocr_utils import classify_scan_from_metrics


def test_classify_scan_positive_with_full_page_images():
    assert classify_scan_from_metrics(
        avg_chars_per_page=12,
        empty_page_ratio=0.9,
        full_page_image_ratio=0.8,
    ) is True


def test_classify_scan_negative_for_sparse_but_not_scanned_pdf():
    assert classify_scan_from_metrics(
        avg_chars_per_page=30,
        empty_page_ratio=0.75,
        full_page_image_ratio=0.1,
    ) is False


def test_classify_scan_negative_for_dense_text_pdf():
    assert classify_scan_from_metrics(
        avg_chars_per_page=500,
        empty_page_ratio=0.1,
        full_page_image_ratio=0.0,
    ) is False


def test_classify_scan_threshold_edges():
    assert classify_scan_from_metrics(79.9, 0.2, 0.6) is True
    assert classify_scan_from_metrics(80.0, 0.69, 0.6) is False
