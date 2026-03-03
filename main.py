
#!/usr/bin/env python3
"""
book2md v2.2
-------------
Convert books (PDF, TXT, EPUB, DOCX) into Markdown files, properly split
by chapter titles or TOC structure.
"""

import click
from book_converter import BookConverter

@click.group()
def cli():
    pass

@cli.command()
@click.argument("input_file", type=click.Path(exists=True))
@click.option("--outdir", "-o", default="output_md", help="Output directory")
@click.option(
    "--chapter-mode",
    default="auto",
    type=click.Choice(["auto", "outline", "toc", "heading", "chunk"], case_sensitive=False),
    show_default=True,
    help="Chapter splitting strategy for PDF files.",
)
@click.option(
    "--ocr",
    "ocr_mode",
    default="auto",
    type=click.Choice(["auto", "force", "off"], case_sensitive=False),
    show_default=True,
    help="OCR behavior for PDF files.",
)
@click.option("--ocr-lang", default="chi_sim+eng", show_default=True, help="OCR language(s).")
@click.option("--keep-intermediate", is_flag=True, help="Keep intermediate OCR files.")
@click.option(
    "--chunk-words",
    default=4000,
    show_default=True,
    type=click.IntRange(min=1),
    help="Chunk size fallback.",
)
@click.option(
    "--toc-max-pages",
    default=30,
    show_default=True,
    type=click.IntRange(min=1),
    help="TOC scan depth before adaptive extension to 50 pages.",
)
def convert(input_file, outdir, chapter_mode, ocr_mode, ocr_lang, keep_intermediate, chunk_words, toc_max_pages):
    """Convert a book into multiple Markdown chapter files."""
    converter = BookConverter(
        input_file,
        outdir,
        chapter_mode=chapter_mode,
        ocr_mode=ocr_mode,
        ocr_lang=ocr_lang,
        keep_intermediate=keep_intermediate,
        chunk_words=chunk_words,
        toc_max_pages=toc_max_pages,
    )
    converter.convert()

if __name__ == "__main__":
    cli()
