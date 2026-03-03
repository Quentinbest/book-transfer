from click.testing import CliRunner

import main


def test_cli_options_are_forwarded_to_converter(monkeypatch):
    captured = {}

    class FakeConverter:
        def __init__(self, input_file, outdir, chapter_mode, ocr_mode, ocr_lang, keep_intermediate, chunk_words, toc_max_pages):
            captured["args"] = {
                "input_file": input_file,
                "outdir": outdir,
                "chapter_mode": chapter_mode,
                "ocr_mode": ocr_mode,
                "ocr_lang": ocr_lang,
                "keep_intermediate": keep_intermediate,
                "chunk_words": chunk_words,
                "toc_max_pages": toc_max_pages,
            }

        def convert(self):
            captured["converted"] = True

    monkeypatch.setattr(main, "BookConverter", FakeConverter)

    runner = CliRunner()
    with runner.isolated_filesystem():
        with open("book.pdf", "wb") as f:
            f.write(b"%PDF-1.4")

        result = runner.invoke(
            main.cli,
            [
                "convert",
                "book.pdf",
                "-o",
                "out",
                "--chapter-mode",
                "toc",
                "--ocr",
                "force",
                "--ocr-lang",
                "eng",
                "--keep-intermediate",
                "--chunk-words",
                "1234",
                "--toc-max-pages",
                "40",
            ],
        )

    assert result.exit_code == 0, result.output
    assert captured["converted"] is True
    assert captured["args"]["chapter_mode"] == "toc"
    assert captured["args"]["ocr_mode"] == "force"
    assert captured["args"]["ocr_lang"] == "eng"
    assert captured["args"]["keep_intermediate"] is True
    assert captured["args"]["chunk_words"] == 1234
    assert captured["args"]["toc_max_pages"] == 40
