from book_converter import PdfBook
from pdf_processing import ProcessingContext


def _fake_context(tmp_path, ocr_performed=False):
    run_dir = tmp_path / "run"
    run_dir.mkdir()
    return ProcessingContext(
        input_pdf=str(tmp_path / "input.pdf"),
        processed_pdf=str(tmp_path / "processed.pdf"),
        temp_dir=str(run_dir),
        run_log_path=str(run_dir / "run.log"),
        ocr_output_path=str(run_dir / "ocr_output.pdf") if ocr_performed else None,
        ocr_performed=ocr_performed,
        keep_intermediate=False,
    )


def test_pdf_book_extract_chapters_uses_processing_pipeline(monkeypatch, tmp_path):
    monkeypatch.setattr(
        "book_converter.prepare_pdf_for_processing",
        lambda *args, **kwargs: _fake_context(tmp_path),
    )
    monkeypatch.setattr(
        "book_converter.extract_pdf_chapters",
        lambda *args, **kwargs: [("A", "Body A"), ("B", "Body B")],
    )
    called = {"success": None}

    def fake_finalize(_ctx, success, error):
        called["success"] = success
        assert error is None
        return ""

    monkeypatch.setattr("book_converter.finalize_pdf_processing", fake_finalize)

    chapters = PdfBook("dummy.pdf", ocr_mode="off").extract_chapters()

    assert chapters == [("A", "Body A"), ("B", "Body B")]
    assert called["success"] is True


def test_pdf_book_extract_chapters_reports_reusable_path_on_downstream_failure(monkeypatch, tmp_path):
    monkeypatch.setattr(
        "book_converter.prepare_pdf_for_processing",
        lambda *args, **kwargs: _fake_context(tmp_path, ocr_performed=True),
    )

    def fake_extract(*_args, **_kwargs):
        raise RuntimeError("downstream parse failed")

    monkeypatch.setattr("book_converter.extract_pdf_chapters", fake_extract)
    monkeypatch.setattr(
        "book_converter.finalize_pdf_processing",
        lambda *_args, **_kwargs: "OCR succeeded but downstream failed. Reusable file: /tmp/x.pdf",
    )

    try:
        PdfBook("dummy.pdf", ocr_mode="force").extract_chapters()
    except RuntimeError as exc:
        message = str(exc)
        assert "downstream parse failed" in message
        assert "OCR succeeded but downstream failed" in message
    else:
        raise AssertionError("Expected RuntimeError")
