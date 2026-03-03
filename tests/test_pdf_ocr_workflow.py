from pathlib import Path

from pdf_processing import prepare_pdf_for_processing


def test_prepare_pdf_auto_runs_ocr_when_detector_true(tmp_path):
    input_pdf = tmp_path / "input.pdf"
    input_pdf.write_bytes(b"%PDF-1.4")

    called = {"ocr": False}

    def fake_detector(_path):
        return True

    def fake_runner(inp, out, _lang):
        called["ocr"] = True
        Path(out).write_bytes(Path(inp).read_bytes() + b"-ocr")

    ctx = prepare_pdf_for_processing(
        str(input_pdf),
        ocr_mode="auto",
        ocr_lang="chi_sim+eng",
        keep_intermediate=False,
        scan_detector=fake_detector,
        ocr_runner=fake_runner,
    )

    assert called["ocr"] is True
    assert ctx.ocr_performed is True
    assert Path(ctx.processed_pdf).name == "ocr_output.pdf"


def test_prepare_pdf_force_runs_ocr_even_if_detector_false(tmp_path):
    input_pdf = tmp_path / "input.pdf"
    input_pdf.write_bytes(b"%PDF-1.4")

    called = {"ocr": False}

    def fake_runner(inp, out, _lang):
        called["ocr"] = True
        Path(out).write_bytes(Path(inp).read_bytes())

    ctx = prepare_pdf_for_processing(
        str(input_pdf),
        ocr_mode="force",
        scan_detector=lambda _: False,
        ocr_runner=fake_runner,
    )

    assert called["ocr"] is True
    assert ctx.ocr_performed is True


def test_prepare_pdf_off_skips_ocr(tmp_path):
    input_pdf = tmp_path / "input.pdf"
    input_pdf.write_bytes(b"%PDF-1.4")

    called = {"ocr": False}

    def fake_runner(_inp, _out, _lang):
        called["ocr"] = True

    ctx = prepare_pdf_for_processing(
        str(input_pdf),
        ocr_mode="off",
        scan_detector=lambda _: True,
        ocr_runner=fake_runner,
    )

    assert called["ocr"] is False
    assert ctx.ocr_performed is False
    assert ctx.processed_pdf == str(input_pdf)
