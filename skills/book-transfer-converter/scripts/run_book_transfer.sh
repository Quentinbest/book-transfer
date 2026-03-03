#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../../../" && pwd)"

input_file=""
outdir="output_md"
chapter_mode="auto"
ocr_mode="auto"
ocr_lang="chi_sim+eng"
keep_intermediate="false"
chunk_words="4000"
toc_max_pages="30"

is_valid_chapter_mode() {
  case "$1" in
    auto|outline|toc|heading|chunk) return 0 ;;
    *) return 1 ;;
  esac
}

is_valid_ocr_mode() {
  case "$1" in
    auto|force|off) return 0 ;;
    *) return 1 ;;
  esac
}

is_positive_int() {
  [[ "$1" =~ ^[1-9][0-9]*$ ]]
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --input-file)
      input_file="${2:-}"
      shift 2
      ;;
    --outdir)
      outdir="${2:-}"
      shift 2
      ;;
    --chapter-mode)
      chapter_mode="${2:-}"
      shift 2
      ;;
    --ocr)
      ocr_mode="${2:-}"
      shift 2
      ;;
    --ocr-lang)
      ocr_lang="${2:-}"
      shift 2
      ;;
    --keep-intermediate)
      keep_intermediate="true"
      shift
      ;;
    --chunk-words)
      chunk_words="${2:-}"
      shift 2
      ;;
    --toc-max-pages)
      toc_max_pages="${2:-}"
      shift 2
      ;;
    *)
      echo "Unknown argument: $1" >&2
      exit 2
      ;;
  esac

done

if ! is_valid_chapter_mode "$chapter_mode"; then
  echo "Invalid value for --chapter-mode: $chapter_mode" >&2
  exit 2
fi

if ! is_valid_ocr_mode "$ocr_mode"; then
  echo "Invalid value for --ocr: $ocr_mode" >&2
  exit 2
fi

if ! is_positive_int "$chunk_words"; then
  echo "Invalid value for --chunk-words: $chunk_words (must be positive integer)" >&2
  exit 2
fi

if ! is_positive_int "$toc_max_pages"; then
  echo "Invalid value for --toc-max-pages: $toc_max_pages (must be positive integer)" >&2
  exit 2
fi

if [[ -z "$input_file" ]]; then
  echo "Missing required argument: --input-file" >&2
  exit 2
fi

cmd=("$REPO_DIR/.venv/bin/python" "$REPO_DIR/main.py" "convert" "$input_file" "-o" "$outdir" "--chapter-mode" "$chapter_mode" "--ocr" "$ocr_mode" "--ocr-lang" "$ocr_lang" "--chunk-words" "$chunk_words" "--toc-max-pages" "$toc_max_pages")
if [[ "$keep_intermediate" == "true" ]]; then
  cmd+=("--keep-intermediate")
fi

exec "${cmd[@]}"
