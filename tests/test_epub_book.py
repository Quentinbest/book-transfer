import builtins
import re
import sys
import types
from types import SimpleNamespace

import pytest

from book_converter import EpubBook


def _install_fake_epub_stack(monkeypatch, toc, items):
    ebooklib_module = types.ModuleType("ebooklib")
    epub_module = types.ModuleType("ebooklib.epub")
    bs4_module = types.ModuleType("bs4")
    markdownify_module = types.ModuleType("markdownify")

    class FakeSoup:
        def __init__(self, body, _parser):
            if isinstance(body, bytes):
                body = body.decode("utf-8")
            self.body = body

            title_match = re.search(r"<title>(.*?)</title>", body, re.IGNORECASE | re.DOTALL)
            self.title = (
                SimpleNamespace(string=title_match.group(1).strip()) if title_match else None
            )

        def find(self, _tags):
            heading_match = re.search(r"<h[1-3]>(.*?)</h[1-3]>", self.body, re.IGNORECASE | re.DOTALL)
            if not heading_match:
                return None
            heading_text = heading_match.group(1).strip()
            return SimpleNamespace(get_text=lambda strip=True: heading_text.strip() if strip else heading_text)

        def __str__(self):
            return self.body

    class FakeBook:
        def __init__(self, toc_items, href_to_item):
            self.toc = toc_items
            self._href_to_item = href_to_item

        def get_item_with_href(self, href):
            return self._href_to_item.get(href)

        def get_items_of_type(self, _item_type):
            return list(self._href_to_item.values())

    def read_epub(_filepath):
        return FakeBook(toc, items)

    def markdownify(value):
        return value

    epub_module.read_epub = read_epub
    epub_module.ITEM_DOCUMENT = "doc"
    bs4_module.BeautifulSoup = FakeSoup
    markdownify_module.markdownify = markdownify
    ebooklib_module.epub = epub_module

    monkeypatch.setitem(sys.modules, "ebooklib", ebooklib_module)
    monkeypatch.setitem(sys.modules, "ebooklib.epub", epub_module)
    monkeypatch.setitem(sys.modules, "bs4", bs4_module)
    monkeypatch.setitem(sys.modules, "markdownify", markdownify_module)


def _fake_item(html):
    return SimpleNamespace(get_body_content=lambda: html.encode("utf-8"))


def test_epub_extract_chapters_uses_toc_and_deduplicates(monkeypatch):
    toc = [
        SimpleNamespace(href="ch1.xhtml"),
        [SimpleNamespace(href="ch1.xhtml#anchor"), SimpleNamespace(href="ch2.xhtml")],
    ]
    items = {
        "ch1.xhtml": _fake_item("<html><title>Chapter One</title><p>A</p></html>"),
        "ch2.xhtml": _fake_item("<html><h1>Chapter Two</h1><p>B</p></html>"),
    }
    _install_fake_epub_stack(monkeypatch, toc, items)

    chapters = EpubBook("dummy.epub").extract_chapters()

    assert len(chapters) == 2
    assert chapters[0][0] == "Chapter One"
    assert chapters[1][0] == "Chapter Two"


def test_epub_extract_chapters_falls_back_when_no_toc(monkeypatch):
    items = {
        "a.xhtml": _fake_item("<html><title>A</title><p>1</p></html>"),
        "b.xhtml": _fake_item("<html><title>B</title><p>2</p></html>"),
    }
    _install_fake_epub_stack(monkeypatch, [], items)

    chapters = EpubBook("dummy.epub").extract_chapters()

    assert len(chapters) == 2
    assert {title for title, _ in chapters} == {"A", "B"}


def test_epub_extract_chapters_missing_dependency_message(monkeypatch):
    monkeypatch.delitem(sys.modules, "ebooklib", raising=False)
    monkeypatch.delitem(sys.modules, "ebooklib.epub", raising=False)

    original_import = builtins.__import__

    def fake_import(name, globals=None, locals=None, fromlist=(), level=0):
        if name == "ebooklib":
            raise ImportError("missing ebooklib")
        return original_import(name, globals, locals, fromlist, level)

    monkeypatch.setattr(builtins, "__import__", fake_import)

    with pytest.raises(ImportError, match="EPUB conversion requires 'ebooklib'"):
        EpubBook("dummy.epub").extract_chapters()
