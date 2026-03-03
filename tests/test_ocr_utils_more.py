import types

import pytest

import ocr_utils


def test_sample_text_metrics(monkeypatch):
    values = {
        0: "hello",
        1: "",
        2: "world",
    }

    def fake_extract(_path, page_numbers):
        return values.get(page_numbers[0], "")

    monkeypatch.setattr(ocr_utils, "extract_text", fake_extract)
    avg, empty_ratio, sampled = ocr_utils._sample_text_metrics("x.pdf", sample_pages=3)

    assert sampled == 3
    assert avg == pytest.approx((5 + 0 + 5) / 3)
    assert empty_ratio == pytest.approx(1 / 3)


def test_sample_full_page_image_ratio_no_pypdf(monkeypatch):
    monkeypatch.setattr(ocr_utils, "_sample_full_page_image_ratio", lambda *_args, **_kwargs: 0.0)
    monkeypatch.setattr(ocr_utils, "_sample_text_metrics", lambda *_args, **_kwargs: (10.0, 0.8, 20))
    metrics = ocr_utils.detect_scanned_pdf("x.pdf", sample_pages=20)
    assert metrics.is_scanned is False


def test_ensure_ocrmypdf_available(monkeypatch):
    monkeypatch.setattr(ocr_utils.shutil, "which", lambda _x: None)
    with pytest.raises(RuntimeError, match="ocrmypdf is required"):
        ocr_utils.ensure_ocrmypdf_available()


def test_run_ocr_ocrmypdf_invokes_subprocess(monkeypatch, tmp_path):
    inp = tmp_path / "in.pdf"
    out = tmp_path / "out.pdf"
    inp.write_bytes(b"%PDF-1.4")

    monkeypatch.setattr(ocr_utils.shutil, "which", lambda _x: "/usr/local/bin/ocrmypdf")

    called = {}

    def fake_run(cmd, **kwargs):
        called["cmd"] = cmd
        called["kwargs"] = kwargs
        out.write_bytes(inp.read_bytes() + b"ocr")
        return types.SimpleNamespace(returncode=0)

    monkeypatch.setattr(ocr_utils.subprocess, "run", fake_run)

    ocr_utils.run_ocr_ocrmypdf(str(inp), str(out), "eng")

    assert called["cmd"][0] == "ocrmypdf"
    assert "--language" in called["cmd"]
    assert out.exists()
