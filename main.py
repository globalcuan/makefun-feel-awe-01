from pathlib import Path

TEXT = "Somewhere, a river is smoothing a stone it found a million years ago. It works all night, without light, without praise, one soft pass at a time. The stone is rounder than yesterday. That is all that has happened, and it is enough."


def main():
    output = Path("/output")
    output.mkdir(parents=True, exist_ok=True)
    entry = output / "entry.txt"
    entry.write_text(TEXT, encoding="utf-8")
    entry.chmod(0o644)


if __name__ == "__main__":
    main()
