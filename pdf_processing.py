import os
import re
import shutil
import tempfile
import traceback
from dataclasses import dataclass

from pdfminer.high_level import extract_pages, extract_text
from pdfminer.layout import LTTextContainer

from chapter_utils import unique_sorted_ranges
from ocr_utils import detect_scanned_pdf, run_ocr_ocrmypdf


@dataclass
class ProcessingContext:
    input_pdf: str
    processed_pdf: str
    temp_dir: str
    run_log_path: str
    ocr_output_path: str | None
    ocr_performed: bool
    keep_intermediate: bool


def prepare_pdf_for_processing(
    input_pdf: str,
    ocr_mode: str = "auto",
    ocr_lang: str = "chi_sim+eng",
    keep_intermediate: bool = False,
    scan_detector=detect_scanned_pdf,
    ocr_runner=run_ocr_ocrmypdf,
) -> ProcessingContext:
    temp_dir = tempfile.mkdtemp(prefix="book-transfer-")
    run_log_path = os.path.join(temp_dir, "run.log")
    ocr_output = os.path.join(temp_dir, "ocr_output.pdf")

    should_ocr = False
    if ocr_mode == "force":
        should_ocr = True
    elif ocr_mode == "off":
        should_ocr = False
    else:
        detection = scan_detector(input_pdf)
        should_ocr = bool(getattr(detection, "is_scanned", detection))

    if should_ocr:
        ocr_runner(input_pdf, ocr_output, ocr_lang)
        processed = ocr_output
    else:
        processed = input_pdf

    return ProcessingContext(
        input_pdf=input_pdf,
        processed_pdf=processed,
        temp_dir=temp_dir,
        run_log_path=run_log_path,
        ocr_output_path=ocr_output if should_ocr else None,
        ocr_performed=should_ocr,
        keep_intermediate=keep_intermediate,
    )


def finalize_pdf_processing(context: ProcessingContext, success: bool, error: Exception | None) -> str:
    if error is not None:
        with open(context.run_log_path, "a", encoding="utf-8") as f:
            f.write(str(error) + "\n")
            f.write(traceback.format_exc() + "\n")

    note = ""
    if success:
        if not context.keep_intermediate and os.path.isdir(context.temp_dir):
            shutil.rmtree(context.temp_dir, ignore_errors=True)
        return note

    if context.ocr_performed and context.ocr_output_path and os.path.exists(context.ocr_output_path):
        note = (
            "OCR succeeded but downstream failed. "
            f"Reusable file: {context.ocr_output_path} "
            f"(log: {context.run_log_path})"
        )
    return note


def _extract_pdf_page_texts(pdf_path: str, max_pages: int | None = None) -> list[str]:
    pages = []
    if max_pages is None:
        # Stop after a long trailing empty sequence.
        empty_tail = 0
        for i in range(0, 600):
            text = (extract_text(pdf_path, page_numbers=[i]) or "").strip()
            if not text:
                empty_tail += 1
                if i > 20 and empty_tail >= 8:
                    break
            else:
                empty_tail = 0
            pages.append(text)
        return pages

    for i in range(max_pages):
        text = (extract_text(pdf_path, page_numbers=[i]) or "").strip()
        pages.append(text)
    return pages


def _normalize(s: str) -> str:
    s = s.replace("ﬁ", "fi").replace("ﬂ", "fl")
    s = re.sub(r"[^A-Za-z0-9 ]+", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def parse_toc_lines(lines: list[str]) -> list[tuple[str, int]]:
    entries: list[tuple[str, int]] = []
    seen = set()
    pattern = re.compile(r"^\s*(?P<title>[^0-9]{3,}?)\s*(?:\.{2,}|\s{2,}|\s)\s*(?P<page>\d{1,4})\s*$")
    for line in lines:
        candidate = line.strip()
        if not candidate or candidate.lower() in {"contents", "table of contents"}:
            continue
        m = pattern.match(candidate)
        if not m:
            continue
        title = re.sub(r"\s+", " ", m.group("title")).strip(" .-")
        page = int(m.group("page"))
        if len(title) < 3:
            continue
        key = (title.lower(), page)
        if key in seen:
            continue
        seen.add(key)
        entries.append((title, page))
    return entries


def _looks_like_toc_page(text: str) -> bool:
    lower = text.lower()
    if "table of contents" in lower or "\ncontents" in lower or lower.startswith("contents"):
        return True
    # Lightweight hint: many TOC rows include dot leaders and page numbers.
    return bool(re.search(r"\.{2,}\s*\d{1,4}\s*$", text, flags=re.MULTILINE))


def scan_toc_entries(pdf_path: str, max_pages: int = 30, lightweight: bool = False) -> list[tuple[str, int]]:
    pages = _extract_pdf_page_texts(pdf_path, max_pages=max_pages)
    lines: list[str] = []
    for text in pages:
        if not text:
            continue
        if lightweight and not _looks_like_toc_page(text):
            continue
        lines.extend(text.splitlines())
    return parse_toc_lines(lines)


def _infer_page_offset(pdf_path: str, toc_entries: list[tuple[str, int]]) -> int | None:
    if not toc_entries:
        return None
    pages = _extract_pdf_page_texts(pdf_path, max_pages=140)
    normalized_pages = [_normalize(p) for p in pages]
    for title, printed_page in toc_entries[:8]:
        nt = _normalize(title)
        if not nt:
            continue
        for idx, body in enumerate(normalized_pages, start=1):
            if nt in body:
                return idx - printed_page
    return None


def _build_chapters_by_page_ranges(
    pdf_path: str,
    titled_starts: list[tuple[str, int]],
) -> list[tuple[str, str]]:
    pages = _extract_pdf_page_texts(pdf_path, max_pages=None)
    total = len(pages)
    if total == 0:
        return []

    starts = [p for _, p in titled_starts]
    starts = unique_sorted_ranges(starts, total_pages=total)

    title_by_start = {p: title for title, p in titled_starts}
    chapters = []
    for i, start in enumerate(starts):
        end = starts[i + 1] - 1 if i + 1 < len(starts) else total
        title = title_by_start.get(start, f"Chapter {i + 1}")
        chunk = "\n\n".join(pages[start - 1 : end]).strip()
        chapters.append((title, chunk))
    return chapters


def build_chapters_from_toc_entries(
    pdf_path: str,
    toc_entries: list[tuple[str, int]],
) -> list[tuple[str, str]]:
    if len(toc_entries) < 3:
        return []
    offset = _infer_page_offset(pdf_path, toc_entries)
    if offset is None:
        return []
    titled_starts = [(title, page + offset) for title, page in toc_entries]
    return _build_chapters_by_page_ranges(pdf_path, titled_starts)


def extract_chapters_outline(pdf_path: str) -> list[tuple[str, str]]:
    try:
        from pypdf import PdfReader
    except Exception:
        return []

    try:
        reader = PdfReader(pdf_path)
    except Exception:
        return []

    raw_outline = getattr(reader, "outline", None)
    if not raw_outline:
        return []

    entries: list[tuple[str, int]] = []

    def walk(nodes):
        for node in nodes:
            if isinstance(node, list):
                walk(node)
                continue
            title = getattr(node, "title", None)
            if title is None:
                continue
            try:
                page = reader.get_destination_page_number(node) + 1
            except Exception:
                continue
            entries.append((str(title).strip(), page))

    walk(raw_outline)
    if len(entries) < 3:
        return []
    return _build_chapters_by_page_ranges(pdf_path, entries)


def extract_chapters_heading(pdf_path: str, chunk_words: int = 4000) -> list[tuple[str, str]]:
    pages = list(extract_pages(pdf_path))
    text_blocks = []
    for page_layout in pages:
        for element in page_layout:
            if isinstance(element, LTTextContainer):
                text_blocks.append(element.get_text().strip())
    full_text = "\n".join(text_blocks)
    if not full_text.strip():
        return extract_chapters_chunk(pdf_path, chunk_words=chunk_words)

    pattern = re.compile(r"(?P<title>(?:(?:CHAPTER|Chapter|Part|PART|BOOK|Book)\s+\w+.+?))(\n{1,2}|$)")
    matches = list(pattern.finditer(full_text))
    chapters = []
    if matches:
        for i in range(len(matches)):
            start = matches[i].end()
            end = matches[i + 1].start() if (i + 1) < len(matches) else len(full_text)
            title_line = matches[i].group("title").strip()
            body = full_text[start:end].strip()
            title = re.sub(r"^(CHAPTER|Chapter|Part|PART|Book|BOOK)\s*", "", title_line).strip()
            chapters.append((title or f"Chapter {i+1}", body))
        return chapters

    return extract_chapters_chunk(pdf_path, chunk_words=chunk_words)


def extract_chapters_chunk(pdf_path: str, chunk_words: int = 4000) -> list[tuple[str, str]]:
    pages = _extract_pdf_page_texts(pdf_path, max_pages=None)
    full_text = "\n".join(pages).strip()
    if not full_text:
        return []
    words = full_text.split()
    chapters = []
    for i in range(0, len(words), chunk_words):
        chunk = " ".join(words[i : i + chunk_words])
        chapters.append((f"Auto Chapter {len(chapters)+1}", chunk))
    return chapters


def extract_chapters_toc(
    pdf_path: str,
    max_pages: int = 30,
    extended_max_pages: int = 50,
) -> list[tuple[str, str]]:
    entries = scan_toc_entries(pdf_path, max_pages=max_pages, lightweight=False)
    if not entries and extended_max_pages > max_pages:
        entries = scan_toc_entries(pdf_path, max_pages=extended_max_pages, lightweight=True)
    if not entries:
        return []
    return build_chapters_from_toc_entries(pdf_path, entries)


def extract_pdf_chapters(
    pdf_path: str,
    chapter_mode: str = "auto",
    chunk_words: int = 4000,
    toc_max_pages: int = 30,
) -> list[tuple[str, str]]:
    strategy_order = {
        "outline": ["outline"],
        "toc": ["toc"],
        "heading": ["heading"],
        "chunk": ["chunk"],
        "auto": ["outline", "toc", "heading", "chunk"],
    }
    order = strategy_order.get(chapter_mode, strategy_order["auto"])

    for mode in order:
        if mode == "outline":
            chapters = extract_chapters_outline(pdf_path)
        elif mode == "toc":
            chapters = extract_chapters_toc(pdf_path, max_pages=toc_max_pages, extended_max_pages=50)
        elif mode == "heading":
            chapters = extract_chapters_heading(pdf_path, chunk_words=chunk_words)
        else:
            chapters = extract_chapters_chunk(pdf_path, chunk_words=chunk_words)
        if chapters:
            return chapters
    return []
