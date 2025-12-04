
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
def convert(input_file, outdir):
    """Convert a book into multiple Markdown chapter files."""
    converter = BookConverter(input_file, outdir)
    converter.convert()

if __name__ == "__main__":
    cli()
