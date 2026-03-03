import types

from pdf_processing import extract_chapters_outline


class _Dest:
    def __init__(self, title):
        self.title = title


def test_extract_chapters_outline_builds_ranges_from_outline(monkeypatch):
    class FakeReader:
        def __init__(self, _path):
            self.outline = [_Dest("Intro"), _Dest("Part I"), _Dest("Part II")]

        def get_destination_page_number(self, node):
            mapping = {"Intro": 0, "Part I": 3, "Part II": 7}
            return mapping[node.title]

    monkeypatch.setitem(__import__("sys").modules, "pypdf", types.SimpleNamespace(PdfReader=FakeReader))
    monkeypatch.setattr(
        "pdf_processing._build_chapters_by_page_ranges",
        lambda _path, starts: [(title, f"p{start}") for title, start in starts],
    )

    out = extract_chapters_outline("dummy.pdf")
    assert out == [("Intro", "p1"), ("Part I", "p4"), ("Part II", "p8")]
