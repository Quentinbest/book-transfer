from pdf_processing import extract_chapters_toc


def test_toc_depth_fallback_uses_extended_pages(monkeypatch):
    calls = []

    def fake_scan(_pdf_path, max_pages, lightweight=False):
        calls.append((max_pages, lightweight))
        if max_pages == 30 and lightweight is False:
            return []
        return [("Chapter 1", 11), ("Chapter 2", 20), ("Chapter 3", 30)]

    monkeypatch.setattr("pdf_processing.scan_toc_entries", fake_scan)
    monkeypatch.setattr("pdf_processing.build_chapters_from_toc_entries", lambda *args, **kwargs: [("ok", "body")])

    chapters = extract_chapters_toc("dummy.pdf", max_pages=30, extended_max_pages=50)

    assert chapters == [("ok", "body")]
    assert calls == [(30, False), (50, True)]
