from pathlib import Path

import pytest

from book_converter import BookConverter, BookFactory, MarkdownWriter


def test_markdown_writer_writes_files(tmp_path):
    writer = MarkdownWriter(str(tmp_path))
    writer.write_chapters([("Title One", "Body1"), ("Title Two", "Body2")])
    files = sorted(tmp_path.glob("*.md"))
    assert len(files) == 2
    assert files[0].name.startswith("01_")
    assert files[0].read_text(encoding="utf-8").startswith("# Title One")


def test_book_factory_unsupported_type():
    with pytest.raises(ValueError, match="Unsupported file type"):
        BookFactory.create_book("a.xlsx")


def test_book_converter_passes_options(monkeypatch):
    captured = {}

    class FakeBook:
        def extract_chapters(self):
            return [("T", "B")]

    def fake_create_book(filepath, **options):
        captured["filepath"] = filepath
        captured["options"] = options
        return FakeBook()

    monkeypatch.setattr("book_converter.BookFactory.create_book", fake_create_book)
    monkeypatch.setattr("book_converter.MarkdownWriter.write_chapters", lambda self, chapters: captured.setdefault("chapters", chapters))

    converter = BookConverter(
        "book.pdf",
        "out",
        chapter_mode="toc",
        ocr_mode="force",
        ocr_lang="eng",
        keep_intermediate=True,
        chunk_words=1234,
        toc_max_pages=40,
    )
    converter.convert()

    assert captured["filepath"] == "book.pdf"
    assert captured["options"]["chapter_mode"] == "toc"
    assert captured["options"]["ocr_mode"] == "force"
    assert captured["options"]["ocr_lang"] == "eng"
    assert captured["options"]["keep_intermediate"] is True
    assert captured["options"]["chunk_words"] == 1234
    assert captured["options"]["toc_max_pages"] == 40
    assert captured["chapters"] == [("T", "B")]
