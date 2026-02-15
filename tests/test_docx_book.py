import builtins
import sys
import types
from types import SimpleNamespace

import pytest

from book_converter import DocxBook


def _install_fake_docx(monkeypatch, paragraphs):
    docx_module = types.ModuleType("docx")

    def Document(_filepath):
        return SimpleNamespace(paragraphs=paragraphs)

    docx_module.Document = Document
    monkeypatch.setitem(sys.modules, "docx", docx_module)


def test_docx_extract_chapters_from_heading_1(monkeypatch):
    paragraphs = [
        SimpleNamespace(text="Chapter One", style=SimpleNamespace(name="Heading 1")),
        SimpleNamespace(text="Body one", style=SimpleNamespace(name="Normal")),
        SimpleNamespace(text="Chapter Two", style=SimpleNamespace(name="Heading 1")),
        SimpleNamespace(text="Body two", style=SimpleNamespace(name="Normal")),
    ]
    _install_fake_docx(monkeypatch, paragraphs)

    chapters = DocxBook("dummy.docx").extract_chapters()

    assert len(chapters) == 2
    assert chapters[0][0] == "Chapter One"
    assert "Body one" in chapters[0][1]
    assert chapters[1][0] == "Chapter Two"
    assert "Body two" in chapters[1][1]


def test_docx_extract_chapters_fallback_to_book_when_empty(monkeypatch):
    paragraphs = [
        SimpleNamespace(text="", style=SimpleNamespace(name="Normal")),
        SimpleNamespace(text="", style=SimpleNamespace(name="Normal")),
    ]
    _install_fake_docx(monkeypatch, paragraphs)

    chapters = DocxBook("dummy.docx").extract_chapters()

    assert len(chapters) == 1
    assert chapters[0][0] == "Book"


def test_docx_extract_chapters_missing_dependency_message(monkeypatch):
    monkeypatch.delitem(sys.modules, "docx", raising=False)

    original_import = builtins.__import__

    def fake_import(name, globals=None, locals=None, fromlist=(), level=0):
        if name == "docx":
            raise ImportError("missing docx")
        return original_import(name, globals, locals, fromlist, level)

    monkeypatch.setattr(builtins, "__import__", fake_import)

    with pytest.raises(ImportError, match="DOCX conversion requires 'python-docx'"):
        DocxBook("dummy.docx").extract_chapters()
