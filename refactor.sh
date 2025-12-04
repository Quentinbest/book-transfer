#!/bin/bash

# refactor.sh - Refactor book-transfer project into proper Python package structure
# This script backs up the original project and creates a new organized structure

set -e  # Exit on error

PROJECT_ROOT="$(cd "$(dirname "$0")" && pwd)"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

echo "🔧 Starting project refactoring..."
echo "📍 Project root: $PROJECT_ROOT"

# Step 1: Backup original files
echo ""
echo "📦 Step 1: Backing up original files..."
BACKUP_DIR="$PROJECT_ROOT/original_backup_$TIMESTAMP"
mkdir -p "$BACKUP_DIR"

# Copy original Python files
cp "$PROJECT_ROOT/main.py" "$BACKUP_DIR/" 2>/dev/null || echo "  ⚠️  main.py not found"
cp "$PROJECT_ROOT/book_converter.py" "$BACKUP_DIR/" 2>/dev/null || echo "  ⚠️  book_converter.py not found"
cp "$PROJECT_ROOT/requirements.txt" "$BACKUP_DIR/" 2>/dev/null || echo "  ✓ requirements.txt backed up"
cp "$PROJECT_ROOT/README.md" "$BACKUP_DIR/" 2>/dev/null || echo "  ✓ README.md backed up"

echo "  ✅ Original files backed up to: $BACKUP_DIR"

# Step 2: Create new package structure
echo ""
echo "📁 Step 2: Creating new package structure..."

# Create directories
mkdir -p "$PROJECT_ROOT/src/book2md/readers"
mkdir -p "$PROJECT_ROOT/tests"
mkdir -p "$PROJECT_ROOT/docs"

echo "  ✓ Created src/book2md/"
echo "  ✓ Created src/book2md/readers/"
echo "  ✓ Created tests/"
echo "  ✓ Created docs/"

# Step 3: Extract Book ABC and Factory from book_converter.py
echo ""
echo "✂️  Step 3: Splitting book_converter.py into modules..."

# Create base.py with Book ABC
cat > "$PROJECT_ROOT/src/book2md/readers/base.py" << 'EOF'
"""Base abstract class for all book readers."""

from abc import ABC, abstractmethod


class Book(ABC):
    """Abstract base class for a book."""

    def __init__(self, filepath):
        self.filepath = filepath

    @abstractmethod
    def extract_chapters(self):
        """Extract chapters from the book.
        
        Returns:
            List[Tuple[str, str]]: List of (title, content) tuples
        """
        pass
EOF

echo "  ✓ Created src/book2md/readers/base.py"

# Create epub.py
cat > "$PROJECT_ROOT/src/book2md/readers/epub.py" << 'EOF'
"""EPUB book reader."""

from ebooklib import epub
from bs4 import BeautifulSoup
from markdownify import markdownify as md

from .base import Book


class EpubBook(Book):
    """A book in EPUB format."""

    def extract_chapters(self):
        book = epub.read_epub(self.filepath)
        chapters = []

        def extract_item_content(item):
            soup = BeautifulSoup(item.get_body_content(), "html.parser")
            title = None
            if soup.title and soup.title.string:
                title = soup.title.string
            else:
                first_heading = soup.find(["h1", "h2", "h3"])
                if first_heading:
                    title = first_heading.get_text(strip=True)
            title = title or "Untitled"
            text_md = md(str(soup))
            return title.strip(), text_md.strip()

        def flatten_toc(toc):
            result = []
            if isinstance(toc, (list, tuple)):
                for x in toc:
                    result.extend(flatten_toc(x))
                return result

            if hasattr(toc, "href"):
                return [toc]

            return []

        toc_items = flatten_toc(book.toc)
        used_hrefs = set()
        for entry in toc_items:
            if not hasattr(entry, "href"):
                continue
            href = entry.href.split("#")[0]
            if href in used_hrefs:
                continue
            used_hrefs.add(href)
            item = book.get_item_with_href(href)
            if item:
                title, content = extract_item_content(item)
                chapters.append((title, content))

        if not chapters:
            for item in book.get_items_of_type(epub.ITEM_DOCUMENT):
                title, body = extract_item_content(item)
                chapters.append((title, body))

        return chapters
EOF

echo "  ✓ Created src/book2md/readers/epub.py"

# Create docx.py
cat > "$PROJECT_ROOT/src/book2md/readers/docx.py" << 'EOF'
"""DOCX book reader."""

from docx import Document

from .base import Book


class DocxBook(Book):
    """A book in DOCX format."""

    def extract_chapters(self):
        doc = Document(self.filepath)
        chapters = []
        current_title = "Untitled"
        current_content = []

        for para in doc.paragraphs:
            style = para.style.name.lower() if para.style and para.style.name else ""
            text = para.text.strip()
            if not text:
                continue

            if "heading" in style and ("1" in style or style == "heading"):
                if current_content:
                    chapters.append((current_title, "\n".join(current_content)))
                current_title = text
                current_content = []
            else:
                current_content.append(text)

        if current_content:
            chapters.append((current_title, "\n".join(current_content)))

        if not chapters:
            return [("Book", "\n".join([p.text for p in doc.paragraphs]))]
        return chapters
EOF

echo "  ✓ Created src/book2md/readers/docx.py"

# Create pdf.py
cat > "$PROJECT_ROOT/src/book2md/readers/pdf.py" << 'EOF'
"""PDF book reader."""

import re
from pdfminer.high_level import extract_pages
from pdfminer.layout import LTTextContainer

from .base import Book


class PdfBook(Book):
    """A book in PDF format."""

    def extract_chapters(self):
        pages = list(extract_pages(self.filepath))
        text_blocks = []

        for page_layout in pages:
            for element in page_layout:
                if isinstance(element, LTTextContainer):
                    text_blocks.append(element.get_text().strip())

        full_text = "\n".join(text_blocks)
        chapters = []

        pattern = re.compile(
            r"(?P<title>(?:(?:CHAPTER|Chapter|Part|PART|BOOK|Book)\s+\w+.+?))(\n{1,2}|$)"
        )
        matches = list(pattern.finditer(full_text))
        if matches:
            for i in range(len(matches)):
                start = matches[i].end()
                end = matches[i + 1].start() if (i + 1) < len(matches) else len(full_text)
                title_line = matches[i].group("title").strip()
                body = full_text[start:end].strip()
                title = re.sub(r"^(CHAPTER|Chapter|Part|PART|Book|BOOK)\s*", "", title_line).strip()
                chapters.append((title or f"Chapter {i+1}", body))
        else:
            words = full_text.split()
            chunk_size = 4000
            for i in range(0, len(words), chunk_size):
                chunk = " ".join(words[i:i+chunk_size])
                chapters.append((f"Auto Chapter {len(chapters)+1}", chunk))

        return chapters
EOF

echo "  ✓ Created src/book2md/readers/pdf.py"

# Create txt.py
cat > "$PROJECT_ROOT/src/book2md/readers/txt.py" << 'EOF'
"""Plain text book reader."""

import re

from .base import Book


class TxtBook(Book):
    """A book in TXT format."""

    def extract_chapters(self):
        with open(self.filepath, "r", encoding="utf-8", errors="ignore") as f:
            text = f.read()

        pattern = re.compile(
            r"(?P<title>^(\s*Chapter|CHAPTER|Part|PART|Book|BOOK)\s+[\w\d]+.*$)",
            re.MULTILINE
        )
        matches = list(pattern.finditer(text))
        chapters = []

        if matches:
            for i in range(len(matches)):
                start = matches[i].end()
                end = matches[i + 1].start() if (i + 1) < len(matches) else len(text)
                title_line = matches[i].group("title").strip()
                content = text[start:end].strip()
                title = re.sub(r"^(Chapter|CHAPTER|Part|PART|Book|BOOK)\s+", "", title_line)
                chapters.append((title.strip() or f"Chapter {i+1}", content))
        else:
            chapters = [("Book", text)]
        return chapters
EOF

echo "  ✓ Created src/book2md/readers/txt.py"

# Create readers __init__.py
cat > "$PROJECT_ROOT/src/book2md/readers/__init__.py" << 'EOF'
"""Book readers for different formats."""

from .base import Book
from .epub import EpubBook
from .docx import DocxBook
from .pdf import PdfBook
from .txt import TxtBook

__all__ = ["Book", "EpubBook", "DocxBook", "PdfBook", "TxtBook"]
EOF

echo "  ✓ Created src/book2md/readers/__init__.py"

# Create factory.py
cat > "$PROJECT_ROOT/src/book2md/factory.py" << 'EOF'
"""Factory for creating book readers."""

import os
from .readers import EpubBook, DocxBook, PdfBook, TxtBook


class BookFactory:
    """Factory for creating book objects."""

    @staticmethod
    def create_book(filepath):
        """Create appropriate book reader based on file extension.
        
        Args:
            filepath: Path to the book file
            
        Returns:
            Book: Appropriate book reader instance
            
        Raises:
            ValueError: If file extension is not supported
        """
        ext = os.path.splitext(filepath)[1].lower()
        if ext == ".epub":
            return EpubBook(filepath)
        elif ext == ".docx":
            return DocxBook(filepath)
        elif ext == ".pdf":
            return PdfBook(filepath)
        elif ext == ".txt":
            return TxtBook(filepath)
        else:
            raise ValueError(f"Unsupported file type: {ext}")
EOF

echo "  ✓ Created src/book2md/factory.py"

# Create writer.py
cat > "$PROJECT_ROOT/src/book2md/writer.py" << 'EOF'
"""Markdown file writer."""

import os
import re


class MarkdownWriter:
    """Writes chapters to Markdown files."""

    def __init__(self, outdir):
        self.outdir = outdir
        os.makedirs(self.outdir, exist_ok=True)

    def write_chapters(self, chapters):
        """Write chapters to numbered markdown files.
        
        Args:
            chapters: List of (title, content) tuples
        """
        for i, (title, content) in enumerate(chapters, 1):
            safe_title = re.sub(r"[^a-zA-Z0-9_-]+", "_", title)[:50]
            filename = os.path.join(self.outdir, f"{i:02d}_{safe_title or 'Chapter'}.md")
            with open(filename, "w", encoding="utf-8") as f:
                f.write(f"# {title}\n\n{content.strip()}\n")
EOF

echo "  ✓ Created src/book2md/writer.py"

# Create converter.py
cat > "$PROJECT_ROOT/src/book2md/converter.py" << 'EOF'
"""Main book converter orchestrator."""

from .factory import BookFactory
from .writer import MarkdownWriter


class BookConverter:
    """Orchestrates the book conversion process."""

    def __init__(self, input_file, outdir):
        self.input_file = input_file
        self.outdir = outdir

    def convert(self):
        """Convert book to markdown chapters."""
        print(f"📘 Converting: {self.input_file}")
        book = BookFactory.create_book(self.input_file)
        chapters = book.extract_chapters()
        print(f"→ Detected {len(chapters)} chapters. Writing to {self.outdir}/")
        writer = MarkdownWriter(self.outdir)
        writer.write_chapters(chapters)
        print("✅ Conversion complete.")
EOF

echo "  ✓ Created src/book2md/converter.py"

# Create CLI module
cat > "$PROJECT_ROOT/src/book2md/cli.py" << 'EOF'
"""Command-line interface for book2md."""

import click
from .converter import BookConverter


@click.group()
def cli():
    """book2md - Convert books to Markdown chapters."""
    pass


@cli.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.option("--outdir", "-o", default="output_md", help="Output directory")
def convert(input_file, outdir):
    """Convert a book into multiple Markdown chapter files."""
    converter = BookConverter(input_file, outdir)
    converter.convert()


if __name__ == "__main__":
    cli()
EOF

echo "  ✓ Created src/book2md/cli.py"

# Create package __init__.py
cat > "$PROJECT_ROOT/src/book2md/__init__.py" << 'EOF'
"""book2md - Convert books to Markdown chapters.

Supports EPUB, PDF, DOCX, and TXT formats.
"""

__version__ = "2.2.0"

from .converter import BookConverter
from .factory import BookFactory
from .writer import MarkdownWriter

__all__ = ["BookConverter", "BookFactory", "MarkdownWriter"]
EOF

echo "  ✓ Created src/book2md/__init__.py"

# Step 4: Create new main.py entry point
echo ""
echo "📝 Step 4: Creating new entry point..."

cat > "$PROJECT_ROOT/main.py" << 'EOF'
#!/usr/bin/env python3
"""
book2md v2.2
-------------
Entry point for the book2md CLI.
"""

from src.book2md.cli import cli

if __name__ == "__main__":
    cli()
EOF

echo "  ✓ Created new main.py"

# Step 5: Create setup.py and pyproject.toml
echo ""
echo "📦 Step 5: Creating packaging files..."

cat > "$PROJECT_ROOT/setup.py" << 'EOF'
from setuptools import setup, find_packages

setup(
    name="book2md",
    version="2.2.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "ebooklib==0.20",
        "beautifulsoup4==4.14.2",
        "markdownify==1.2.2",
        "pdfminer.six==20251107",
        "python-docx==1.2.0",
        "click==8.3.1",
    ],
    entry_points={
        "console_scripts": [
            "book2md=book2md.cli:cli",
        ],
    },
    python_requires=">=3.7",
    author="Your Name",
    description="Convert books (EPUB, PDF, DOCX, TXT) to Markdown chapters",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/book-transfer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
EOF

cat > "$PROJECT_ROOT/pyproject.toml" << 'EOF'
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "book2md"
version = "2.2.0"
description = "Convert books (EPUB, PDF, DOCX, TXT) to Markdown chapters"
readme = "README.md"
requires-python = ">=3.7"
license = {text = "MIT"}
authors = [
    {name = "Your Name", email = "your.email@example.com"}
]
dependencies = [
    "ebooklib==0.20",
    "beautifulsoup4==4.14.2",
    "markdownify==1.2.2",
    "pdfminer.six==20251107",
    "python-docx==1.2.0",
    "click==8.3.1",
]

[project.scripts]
book2md = "book2md.cli:cli"

[project.urls]
Homepage = "https://github.com/yourusername/book-transfer"
EOF

echo "  ✓ Created setup.py"
echo "  ✓ Created pyproject.toml"

# Step 6: Create requirements-dev.txt
cat > "$PROJECT_ROOT/requirements-dev.txt" << 'EOF'
# Development dependencies
pytest>=7.0.0
pytest-cov>=4.0.0
black>=22.0.0
flake8>=5.0.0
mypy>=0.990
EOF

echo "  ✓ Created requirements-dev.txt"

# Step 7: Create basic test structure
echo ""
echo "🧪 Step 6: Creating test structure..."

cat > "$PROJECT_ROOT/tests/__init__.py" << 'EOF'
"""Tests for book2md package."""
EOF

cat > "$PROJECT_ROOT/tests/test_factory.py" << 'EOF'
"""Test BookFactory."""

import pytest
from src.book2md.factory import BookFactory
from src.book2md.readers import EpubBook, DocxBook, PdfBook, TxtBook


def test_factory_epub():
    book = BookFactory.create_book("test.epub")
    assert isinstance(book, EpubBook)


def test_factory_docx():
    book = BookFactory.create_book("test.docx")
    assert isinstance(book, DocxBook)


def test_factory_pdf():
    book = BookFactory.create_book("test.pdf")
    assert isinstance(book, PdfBook)


def test_factory_txt():
    book = BookFactory.create_book("test.txt")
    assert isinstance(book, TxtBook)


def test_factory_unsupported():
    with pytest.raises(ValueError, match="Unsupported file type"):
        BookFactory.create_book("test.xyz")
EOF

echo "  ✓ Created tests/__init__.py"
echo "  ✓ Created tests/test_factory.py"

# Step 8: Create installation guide
cat > "$PROJECT_ROOT/INSTALL.md" << 'EOF'
# Installation Guide

## For Users

### Option 1: Install in development mode (editable)

```bash
pip install -e .
```

After installation, you can use the `book2md` command directly:

```bash
book2md convert mybook.epub -o output/
```

### Option 2: Use without installation

```bash
python3 main.py convert mybook.epub -o output/
```

## For Developers

1. Clone the repository:

```bash
git clone <your-repo-url>
cd book-transfer
```

2. Create a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

3. Install in development mode with dev dependencies:

```bash
pip install -e .
pip install -r requirements-dev.txt
```

4. Run tests:

```bash
pytest tests/ -v
```

5. Run type checking:

```bash
mypy src/
```

6. Format code:

```bash
black src/ tests/
```
EOF

echo "  ✓ Created INSTALL.md"

# Step 9: Summary
echo ""
echo "✅ Refactoring complete!"
echo ""
echo "📊 Summary:"
echo "  • Original files backed up to: $BACKUP_DIR"
echo "  • New package structure created in: src/book2md/"
echo "  • Modular architecture with separate reader modules"
echo "  • Packaging files created (setup.py, pyproject.toml)"
echo "  • Test structure initialized"
echo ""
echo "📁 New structure:"
echo "  src/book2md/"
echo "  ├── __init__.py"
echo "  ├── cli.py           (CLI interface)"
echo "  ├── converter.py     (Main orchestrator)"
echo "  ├── factory.py       (Book factory)"
echo "  ├── writer.py        (Markdown writer)"
echo "  └── readers/"
echo "      ├── __init__.py"
echo "      ├── base.py      (Abstract Book class)"
echo "      ├── epub.py"
echo "      ├── docx.py"
echo "      ├── pdf.py"
echo "      └── txt.py"
echo ""
echo "🚀 Next steps:"
echo "  1. Install in development mode:"
echo "     pip install -e ."
echo ""
echo "  2. Test the new structure:"
echo "     python3 main.py convert <your-book> -o output/"
echo "     # OR after pip install -e ."
echo "     book2md convert <your-book> -o output/"
echo ""
echo "  3. Run tests:"
echo "     pip install -r requirements-dev.txt"
echo "     pytest tests/ -v"
echo ""
