from pathlib import Path

from pdf_processing import ProcessingContext, finalize_pdf_processing


def test_finalize_keeps_intermediate_on_failure_and_reports_path(tmp_path):
    temp_dir = tmp_path / "run"
    temp_dir.mkdir()
    ocr_file = temp_dir / "ocr_output.pdf"
    ocr_file.write_bytes(b"ocr")

    ctx = ProcessingContext(
        input_pdf="/tmp/input.pdf",
        processed_pdf=str(ocr_file),
        temp_dir=str(temp_dir),
        run_log_path=str(temp_dir / "run.log"),
        ocr_output_path=str(ocr_file),
        ocr_performed=True,
        keep_intermediate=False,
    )

    note = finalize_pdf_processing(ctx, success=False, error=RuntimeError("boom"))

    assert "OCR succeeded but downstream failed" in note
    assert str(ocr_file) in note
    assert Path(ctx.run_log_path).exists()


def test_finalize_deletes_temp_dir_on_success_when_keep_false(tmp_path):
    temp_dir = tmp_path / "run"
    temp_dir.mkdir()
    (temp_dir / "run.log").write_text("ok", encoding="utf-8")

    ctx = ProcessingContext(
        input_pdf="/tmp/input.pdf",
        processed_pdf="/tmp/input.pdf",
        temp_dir=str(temp_dir),
        run_log_path=str(temp_dir / "run.log"),
        ocr_output_path=None,
        ocr_performed=False,
        keep_intermediate=False,
    )

    note = finalize_pdf_processing(ctx, success=True, error=None)

    assert note == ""
    assert not temp_dir.exists()
