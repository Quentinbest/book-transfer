import types

import ocr_utils


class _Box:
    def __init__(self, w, h):
        self.width = w
        self.height = h


class _Page:
    def __init__(self, w, h):
        self.mediabox = _Box(w, h)


class _Img:
    def __init__(self, w, h):
        self.width = w
        self.height = h


def test_safe_get_page_size():
    assert ocr_utils._safe_get_page_size(_Page(100, 200)) == (100.0, 200.0)


def test_is_full_page_image_true_and_false():
    page = _Page(1000, 1000)
    assert ocr_utils._is_full_page_image(page, _Img(900, 900)) is True
    assert ocr_utils._is_full_page_image(page, _Img(100, 100)) is False


def test_has_single_main_full_page_image():
    page = _Page(1000, 1000)
    assert ocr_utils._has_single_main_full_page_image(page, [_Img(900, 900)]) is True
    assert ocr_utils._has_single_main_full_page_image(page, [_Img(900, 900), _Img(900, 900)]) is False


def test_sample_full_page_image_ratio(monkeypatch):
    class FakePage:
        def __init__(self, has_full):
            self.mediabox = _Box(1000, 1000)
            self.images = [_Img(900, 900)] if has_full else [_Img(100, 100)]

    class FakeReader:
        def __init__(self, _path):
            self.pages = [FakePage(True), FakePage(False), FakePage(True)]

    monkeypatch.setitem(__import__("sys").modules, "pypdf", types.SimpleNamespace(PdfReader=FakeReader))
    ratio = ocr_utils._sample_full_page_image_ratio("x.pdf", sample_pages=3)
    assert ratio == 2 / 3


def test_detect_scanned_pdf_true(monkeypatch):
    monkeypatch.setattr(ocr_utils, "_sample_text_metrics", lambda *_args, **_kwargs: (10.0, 0.8, 20))
    monkeypatch.setattr(ocr_utils, "_sample_full_page_image_ratio", lambda *_args, **_kwargs: 0.9)
    metrics = ocr_utils.detect_scanned_pdf("x.pdf", sample_pages=20)
    assert metrics.is_scanned is True


def test_ensure_ocrmypdf_available_success(monkeypatch):
    monkeypatch.setattr(ocr_utils.shutil, "which", lambda _x: "/usr/bin/ocrmypdf")
    ocr_utils.ensure_ocrmypdf_available()
