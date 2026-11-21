from pathlib import Path

TEXT = "Somewhere, a river is smoothing a stone it found a million years ago. It works all night, without light, without praise, one soft pass at a time. The stone is rounder than yesterday. That is all that has happened, and it is enough."


def write_entry(output_dir: Path = Path("/output")) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    entry = output_dir / "entry.txt"
    entry.write_text(TEXT, encoding="utf-8")
    entry.chmod(0o644)
    content = entry.read_text(encoding="utf-8")
    assert content == TEXT
    assert 1 <= len(content) <= 280
    return entry


def main():
    write_entry()


if __name__ == "__main__":
    main()
