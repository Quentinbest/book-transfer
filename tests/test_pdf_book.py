import builtins
import sys
import types

import pytest

from book_converter import PdfBook


def _install_fake_pdfminer(monkeypatch, text):
    pdfminer_module = types.ModuleType("pdfminer")
    high_level_module = types.ModuleType("pdfminer.high_level")
    layout_module = types.ModuleType("pdfminer.layout")

    class FakeLTTextContainer:
        def __init__(self, value):
            self._value = value

        def get_text(self):
            return self._value

    def extract_pages(_filepath):
        return [[FakeLTTextContainer(text)]]

    high_level_module.extract_pages = extract_pages
    layout_module.LTTextContainer = FakeLTTextContainer

    monkeypatch.setitem(sys.modules, "pdfminer", pdfminer_module)
    monkeypatch.setitem(sys.modules, "pdfminer.high_level", high_level_module)
    monkeypatch.setitem(sys.modules, "pdfminer.layout", layout_module)


def test_pdf_extract_chapters_detects_markers(monkeypatch):
    text = "Chapter 1 Intro\nBody A\n\nChapter 2 Ending\nBody B\n"
    _install_fake_pdfminer(monkeypatch, text)

    chapters = PdfBook("dummy.pdf").extract_chapters()

    assert len(chapters) == 2
    assert chapters[0][0] == "1 Intro"
    assert "Body A" in chapters[0][1]
    assert chapters[1][0] == "2 Ending"
    assert "Body B" in chapters[1][1]


def test_pdf_extract_chapters_fallback_chunks(monkeypatch):
    text = " ".join(f"w{i}" for i in range(4500))
    _install_fake_pdfminer(monkeypatch, text)

    chapters = PdfBook("dummy.pdf").extract_chapters()

    assert len(chapters) == 2
    assert chapters[0][0] == "Auto Chapter 1"
    assert chapters[1][0] == "Auto Chapter 2"


def test_pdf_extract_chapters_missing_dependency_message(monkeypatch):
    for name in list(sys.modules):
        if name == "pdfminer" or name.startswith("pdfminer."):
            monkeypatch.delitem(sys.modules, name, raising=False)

    original_import = builtins.__import__

    def fake_import(name, globals=None, locals=None, fromlist=(), level=0):
        if name.startswith("pdfminer"):
            raise ImportError("missing pdfminer")
        return original_import(name, globals, locals, fromlist, level)

    monkeypatch.setattr(builtins, "__import__", fake_import)

    with pytest.raises(ImportError, match="PDF conversion requires 'pdfminer.six'"):
        PdfBook("dummy.pdf").extract_chapters()
