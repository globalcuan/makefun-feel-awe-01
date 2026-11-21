from pathlib import Path

TEXT = """Someone carries you in from the car half asleep.
Your cheek rests where a shoulder gives.
Steps. A gate. Night air. Warm cloth.
Below the house, far below the hill, the old stone of the earth is turning in its sleep, slow as a held breath.
Everything you love is already home."""


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
