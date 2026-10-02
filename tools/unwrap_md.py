#!/usr/bin/env python3
"""Unwrap hard-wrapped prose in the repo's Markdown files.

Joins "soft-wrapped" continuation lines (a paragraph or list item that was
broken at ~120 columns) back onto the line they continue, so each paragraph /
list item is a single source line. Markdown renders a soft line break as a
space, so the rendered output is unchanged - only the source gets cleaner.

Left untouched: fenced code, indented code, tables, headings, horizontal
rules / setext underlines, HTML lines, link reference definitions, and hard
line breaks (two trailing spaces or a trailing backslash). Blockquotes are
unwrapped recursively inside their `>` prefix.

Usage:
    python tools/unwrap_md.py            # rewrite every tracked *.md file
    python tools/unwrap_md.py --check    # list files that would change; exit 1 if any
    python tools/unwrap_md.py FILE...    # only the given files
"""
import argparse
import re
import subprocess
import sys
from pathlib import Path

FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})")
QUOTE = re.compile(r"^( {0,3}> ?)")
HEADING = re.compile(r"^#{1,6}(\s|$)")
LIST_ITEM = re.compile(r"^([-+*]|\d{1,9}[.)])(\s|$)")
HRULE = re.compile(r"^([-*_])(\s*\1){2,}\s*$")
SETEXT = re.compile(r"^(=+|-+)\s*$")
LINK_DEF = re.compile(r"^\[[^\]]+\]:\s")
TABLE_DELIM = re.compile(r"^\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*$")
HARD_BREAK = re.compile(r"(  |\\)$")


def starts_block(stripped: str) -> bool:
    """True if a line (leading spaces removed) opens a new block and so must not be joined."""
    return bool(
        HEADING.match(stripped)
        or LIST_ITEM.match(stripped)
        or HRULE.match(stripped)
        or SETEXT.match(stripped)
        or LINK_DEF.match(stripped)
        or FENCE.match(stripped)
        or stripped.startswith(("|", "<", ">"))
    )


def unwrap(lines: list[str]) -> list[str]:
    out: list[str] = []
    fence = None          # closing-fence prefix while inside a fenced code block
    in_table = False
    joinable = False      # can the last output line absorb a continuation?
    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.lstrip(" ")
        indent = len(line) - len(stripped)

        if fence:
            out.append(line)
            if stripped.rstrip().startswith(fence) and not stripped.strip(fence[0]).strip():
                fence = None
            i += 1
            continue

        m = FENCE.match(line)
        if m:
            fence = m.group(1)
            out.append(line)
            joinable = in_table = False
            i += 1
            continue

        if not line.strip():
            out.append(line)
            joinable = in_table = False
            i += 1
            continue

        if QUOTE.match(line):
            # Unwrap a run of blockquote lines recursively inside the `>` prefix.
            prefix = QUOTE.match(line).group(1)
            group = []
            while i < len(lines) and QUOTE.match(lines[i]):
                group.append(lines[i][QUOTE.match(lines[i]).end():])
                i += 1
            for inner in unwrap(group):
                out.append(prefix + inner if inner.strip() else prefix.rstrip())
            joinable = in_table = False
            continue

        nxt = lines[i + 1] if i + 1 < len(lines) else ""
        if in_table or TABLE_DELIM.match(stripped) or ("|" in line and TABLE_DELIM.match(nxt.strip())):
            out.append(line)
            in_table = True
            joinable = False
            i += 1
            continue

        if joinable and not starts_block(stripped) and not HARD_BREAK.search(out[-1]):
            out[-1] = out[-1].rstrip() + " " + stripped.rstrip()
            i += 1
            continue

        out.append(line)
        if indent >= 4 and not LIST_ITEM.match(stripped):
            joinable = False  # possible indented code block: leave it alone
        else:
            joinable = not (
                HEADING.match(stripped) or HRULE.match(stripped) or SETEXT.match(stripped)
                or LINK_DEF.match(stripped) or stripped.startswith("<")
            )
        i += 1
    return out


def process(path: Path, check: bool) -> bool:
    raw = path.read_bytes().decode("utf-8")
    eol = "\r\n" if "\r\n" in raw else "\n"
    lines = raw.split(eol)
    new = eol.join(unwrap(lines))
    if new == raw:
        return False
    if not check:
        path.write_bytes(new.encode("utf-8"))
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("files", nargs="*", type=Path)
    ap.add_argument("--check", action="store_true", help="report only, don't write")
    args = ap.parse_args()

    root = Path(__file__).resolve().parent.parent
    files = args.files or [
        root / f for f in subprocess.run(
            ["git", "ls-files", "*.md"], cwd=root, capture_output=True, text=True, check=True
        ).stdout.splitlines()
    ]
    changed = [f for f in files if process(f, args.check)]
    for f in changed:
        print(("would unwrap: " if args.check else "unwrapped: ") + str(f))
    print(f"{len(changed)}/{len(files)} file(s) {'need unwrapping' if args.check else 'changed'}")
    return 1 if (args.check and changed) else 0


if __name__ == "__main__":
    sys.exit(main())
