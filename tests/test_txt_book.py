import os
import pytest
from book_converter import TxtBook

@pytest.fixture
def create_txt_file(tmp_path):
    def _create(content):
        p = tmp_path / "test_book.txt"
        p.write_text(content, encoding="utf-8")
        return str(p)
    return _create

def test_extract_chapters_simple(create_txt_file):
    content = """Chapter 1: The Beginning
Content of chapter 1.

Chapter 2: The End
Content of chapter 2.
"""
    filepath = create_txt_file(content)
    book = TxtBook(filepath)
    chapters = book.extract_chapters()
    
    assert len(chapters) == 2
    assert chapters[0][0] == "1: The Beginning"
    assert "Content of chapter 1" in chapters[0][1]
    assert chapters[1][0] == "2: The End"
    assert "Content of chapter 2" in chapters[1][1]

def test_extract_chapters_mixed_markers(create_txt_file):
    content = """Part I: Introduction
Intro content.

Chapter 1: First Chapter
    The content of the chapter.

Book 2: The Sequel
Sequel content.
"""
    filepath = create_txt_file(content)
    book = TxtBook(filepath)
    chapters = book.extract_chapters()
    
    assert len(chapters) == 3
    assert chapters[0][0] == "I: Introduction"
    assert chapters[1][0] == "1: First Chapter"
    assert chapters[2][0] == "2: The Sequel"

def test_extract_chapters_bug_repro(create_txt_file):
    """Test the specific case that was failing: title with colon and extra text."""
    content = """Chapter 1: The Beginning
This is the first chapter.
"""
    filepath = create_txt_file(content)
    book = TxtBook(filepath)
    chapters = book.extract_chapters()
    
    assert len(chapters) == 1
    # Before fix, this would have been "1" and content would include ": The Beginning"
    assert chapters[0][0] == "1: The Beginning"
    assert ": The Beginning" not in chapters[0][1]
    assert "This is the first chapter" in chapters[0][1]

def test_extract_chapters_no_markers(create_txt_file):
    content = """Just a simple text file.
With no chapter markers.
"""
    filepath = create_txt_file(content)
    book = TxtBook(filepath)
    chapters = book.extract_chapters()
    
    assert len(chapters) == 1
    assert chapters[0][0] == "Book"
    assert "Just a simple text file" in chapters[0][1]
