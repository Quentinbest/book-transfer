import types

import pdf_processing


class FakeTextElement:
    def __init__(self, text):
        self._text = text

    def get_text(self):
        return self._text


def test_extract_pdf_page_texts_auto_break(monkeypatch):
    def fake_extract(_path, page_numbers):
        i = page_numbers[0]
        if i < 3:
            return "hello"
        return ""

    monkeypatch.setattr(pdf_processing, "extract_text", fake_extract)
    pages = pdf_processing._extract_pdf_page_texts("x.pdf", max_pages=None)
    assert len(pages) >= 3


def test_extract_pdf_page_texts_with_max_pages(monkeypatch):
    monkeypatch.setattr(pdf_processing, "extract_text", lambda _path, page_numbers: f"p{page_numbers[0]}")
    pages = pdf_processing._extract_pdf_page_texts("x.pdf", max_pages=3)
    assert pages == ["p0", "p1", "p2"]


def test_parse_toc_lines_filters_short_titles():
    lines = ["A 12", "Valid Entry .... 20"]
    out = pdf_processing.parse_toc_lines(lines)
    assert out == [("Valid Entry", 20)]


def test_infer_page_offset_none_when_no_match(monkeypatch):
    monkeypatch.setattr(pdf_processing, "_extract_pdf_page_texts", lambda *_args, **_kwargs: ["x", "y"])
    assert pdf_processing._infer_page_offset("x.pdf", [("Chapter One", 1)]) is None


def test_build_chapters_from_toc_entries_success(monkeypatch):
    monkeypatch.setattr(pdf_processing, "_infer_page_offset", lambda *_args, **_kwargs: 10)
    monkeypatch.setattr(
        pdf_processing,
        "_build_chapters_by_page_ranges",
        lambda _path, starts: [(starts[0][0], "a"), (starts[1][0], "b"), (starts[2][0], "c")],
    )
    out = pdf_processing.build_chapters_from_toc_entries("x.pdf", [("A", 1), ("B", 5), ("C", 9)])
    assert [x[0] for x in out] == ["A", "B", "C"]


def test_extract_chapters_outline_handles_missing_outline(monkeypatch):
    class Reader:
        def __init__(self, _p):
            self.outline = []

    monkeypatch.setitem(__import__("sys").modules, "pypdf", types.SimpleNamespace(PdfReader=Reader))
    assert pdf_processing.extract_chapters_outline("x.pdf") == []


def test_extract_chapters_heading_matches_pattern(monkeypatch):
    monkeypatch.setattr(pdf_processing, "LTTextContainer", FakeTextElement)
    monkeypatch.setattr(
        pdf_processing,
        "extract_pages",
        lambda _p: [[FakeTextElement("Chapter 1 Intro\nA\n\nChapter 2 End\nB")]],
    )
    out = pdf_processing.extract_chapters_heading("x.pdf", chunk_words=500)
    assert len(out) == 2
    assert out[0][0] == "1 Intro"


def test_extract_chapters_chunk_no_text(monkeypatch):
    monkeypatch.setattr(pdf_processing, "_extract_pdf_page_texts", lambda *_args, **_kwargs: ["", ""])
    assert pdf_processing.extract_chapters_chunk("x.pdf", chunk_words=10) == []


def test_extract_pdf_chapters_unknown_mode_defaults_auto(monkeypatch):
    monkeypatch.setattr(pdf_processing, "extract_chapters_outline", lambda *_args, **_kwargs: [])
    monkeypatch.setattr(pdf_processing, "extract_chapters_toc", lambda *_args, **_kwargs: [])
    monkeypatch.setattr(pdf_processing, "extract_chapters_heading", lambda *_args, **_kwargs: [])
    monkeypatch.setattr(pdf_processing, "extract_chapters_chunk", lambda *_args, **_kwargs: [("Auto Chapter 1", "z")])
    out = pdf_processing.extract_pdf_chapters("x.pdf", chapter_mode="???")
    assert out == [("Auto Chapter 1", "z")]
