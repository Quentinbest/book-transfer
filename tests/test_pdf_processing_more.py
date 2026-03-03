import types

import pdf_processing


def test_scan_toc_entries_uses_parse(monkeypatch):
    monkeypatch.setattr(pdf_processing, "_extract_pdf_page_texts", lambda *_args, **_kwargs: ["Contents", "Chapter One .... 11"])
    entries = pdf_processing.scan_toc_entries("x.pdf", max_pages=30)
    assert entries == [("Chapter One", 11)]


def test_scan_toc_entries_lightweight_filters_non_toc_pages(monkeypatch):
    monkeypatch.setattr(
        pdf_processing,
        "_extract_pdf_page_texts",
        lambda *_args, **_kwargs: ["Preface text only", "Contents\nChapter One .... 11"],
    )
    entries = pdf_processing.scan_toc_entries("x.pdf", max_pages=50, lightweight=True)
    assert entries == [("Chapter One", 11)]


def test_looks_like_toc_page():
    assert pdf_processing._looks_like_toc_page("Table of Contents\nChapter One ..... 11") is True
    assert pdf_processing._looks_like_toc_page("Random prose with no TOC pattern") is False


def test_infer_page_offset(monkeypatch):
    monkeypatch.setattr(pdf_processing, "_extract_pdf_page_texts", lambda *_args, **_kwargs: ["", "", "Chapter One", "Body"])
    offset = pdf_processing._infer_page_offset("x.pdf", [("Chapter One", 11)])
    assert offset == -8


def test_build_chapters_by_page_ranges(monkeypatch):
    monkeypatch.setattr(pdf_processing, "_extract_pdf_page_texts", lambda *_args, **_kwargs: ["p1", "p2", "p3"])
    chapters = pdf_processing._build_chapters_by_page_ranges("x.pdf", [("A", 1), ("B", 3)])
    assert chapters[0][0] == "A"
    assert "p1" in chapters[0][1]
    assert chapters[1][0] == "B"


def test_build_chapters_from_toc_entries_no_offset(monkeypatch):
    monkeypatch.setattr(pdf_processing, "_infer_page_offset", lambda *_args, **_kwargs: None)
    assert pdf_processing.build_chapters_from_toc_entries("x.pdf", [("A", 1), ("B", 2), ("C", 3)]) == []


def test_extract_chapters_outline(monkeypatch):
    class Dest:
        def __init__(self, title, page):
            self.title = title
            self.page = page

    class Reader:
        def __init__(self, _p):
            self.outline = [Dest("T1", 0), Dest("T2", 2), Dest("T3", 3)]

        def get_destination_page_number(self, node):
            return node.page

    monkeypatch.setitem(__import__("sys").modules, "pypdf", types.SimpleNamespace(PdfReader=Reader))
    monkeypatch.setattr(pdf_processing, "_build_chapters_by_page_ranges", lambda *_args, **_kwargs: [("ok", "body")])

    chapters = pdf_processing.extract_chapters_outline("x.pdf")
    assert chapters == [("ok", "body")]


def test_extract_chapters_heading_falls_back_to_chunk(monkeypatch):
    monkeypatch.setattr(pdf_processing, "extract_pages", lambda _p: [])
    monkeypatch.setattr(pdf_processing, "extract_chapters_chunk", lambda *_args, **_kwargs: [("Auto Chapter 1", "x")])
    chapters = pdf_processing.extract_chapters_heading("x.pdf", chunk_words=123)
    assert chapters == [("Auto Chapter 1", "x")]


def test_extract_pdf_chapters_mode_routing(monkeypatch):
    monkeypatch.setattr(pdf_processing, "extract_chapters_outline", lambda *_args, **_kwargs: [])
    monkeypatch.setattr(pdf_processing, "extract_chapters_toc", lambda *_args, **_kwargs: [])
    monkeypatch.setattr(pdf_processing, "extract_chapters_heading", lambda *_args, **_kwargs: [("H", "b")])
    monkeypatch.setattr(pdf_processing, "extract_chapters_chunk", lambda *_args, **_kwargs: [("C", "b")])

    chapters = pdf_processing.extract_pdf_chapters("x.pdf", chapter_mode="auto")
    assert chapters == [("H", "b")]
