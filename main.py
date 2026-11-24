"""One Line, One Chill - make.fun entry.

Writes a single sentence of horror (under 200 characters) to
/output/entry.txt, where the judge reads it.
"""

from pathlib import Path

LINE = "The voicemail from my dead mother ended with her whispering my new address, the one I moved to yesterday."

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Gate: one sentence, 1 to 200 characters, not only whitespace.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line must be 1 to 200 characters")
    if LINE.count(".") != 1 or not LINE.endswith("."):
        raise ValueError("entry line must be a single sentence")
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")
    print(LINE)


if __name__ == "__main__":
    main()
