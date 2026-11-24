"""One-Liner Laugh Lab — a one-line excuse from a robot vacuum.

The entry is a single funny line answering the prompt: what excuse does
a robot vacuum give after eating a sock? The vacuum denies the crime
and reframes the sock as a refugee it was legally obliged to shelter,
turning a household mishap into a mock-legal asylum case. Short, tight,
and original — the whole joke lands in one sentence.
Running this script writes the entry to the graded output directory
first, then a best-effort local copy next to the script.
"""

import os

ENTRY = (
    "I didn't eat your sock. It applied for asylum inside my dustbin, "
    "and under international vacuum law I had to take it in."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    written = False

    if os.path.isdir(out_dir):
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(path, 0o644)
        written = True

    try:
        local_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)), "entry.txt"
        )
        with open(local_path, "w", encoding="utf-8") as f:
            f.write(ENTRY)
        os.chmod(local_path, 0o644)
        written = True
    except OSError:
        pass

    if not written:
        raise SystemExit("no writable output location")

    print(f"Wrote {len(ENTRY)} chars: {ENTRY}")


if __name__ == "__main__":
    main()
