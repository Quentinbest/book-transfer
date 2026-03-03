from pdf_processing import parse_toc_lines


def test_parse_toc_lines_extracts_entries():
    lines = [
        "Contents",
        "Introduction 1",
        "Chapter One .......... 11",
        "Chapter Two .......... 25",
        "Appendix A .......... 201",
    ]

    entries = parse_toc_lines(lines)

    assert ("Chapter One", 11) in entries
    assert ("Chapter Two", 25) in entries
    assert ("Appendix A", 201) in entries


def test_parse_toc_lines_ignores_noise():
    lines = ["Contents", "vii", "page x", "123", "..."]
    entries = parse_toc_lines(lines)
    assert entries == []
