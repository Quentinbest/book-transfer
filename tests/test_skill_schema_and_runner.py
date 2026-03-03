from pathlib import Path
import subprocess


REPO = Path(__file__).resolve().parents[1]
RUNNER = REPO / "skills" / "book-transfer-converter" / "scripts" / "run_book_transfer.sh"
YAML_FILE = REPO / "skills" / "book-transfer-converter" / "agents" / "openai.yaml"


def test_skill_yaml_contains_expected_interface_keys():
    text = YAML_FILE.read_text(encoding="utf-8")
    assert "display_name:" in text
    assert "short_description:" in text
    assert "default_prompt:" in text
    assert "input_schema:" in text
    assert "additionalProperties: false" in text


def test_runner_rejects_unknown_argument():
    proc = subprocess.run(["bash", str(RUNNER), "--bad-flag"], capture_output=True, text=True)
    assert proc.returncode != 0
    assert "Unknown argument" in (proc.stderr + proc.stdout)


def test_runner_rejects_invalid_enum_values():
    proc = subprocess.run(
        [
            "bash",
            str(RUNNER),
            "--input-file",
            "book.pdf",
            "--chapter-mode",
            "weird",
        ],
        capture_output=True,
        text=True,
    )
    assert proc.returncode != 0
    assert "Invalid value for --chapter-mode" in (proc.stderr + proc.stdout)


def test_skill_yaml_contains_enums_and_required_input():
    text = YAML_FILE.read_text(encoding="utf-8")
    assert "required:" in text
    assert "- input_file" in text
    assert "enum: [auto, outline, toc, heading, chunk]" in text
    assert "enum: [auto, force, off]" in text


def test_runner_rejects_invalid_numeric_values():
    proc = subprocess.run(
        [
            "bash",
            str(RUNNER),
            "--input-file",
            "book.pdf",
            "--chunk-words",
            "0",
        ],
        capture_output=True,
        text=True,
    )
    assert proc.returncode != 0
    assert "Invalid value for --chunk-words" in (proc.stderr + proc.stdout)
