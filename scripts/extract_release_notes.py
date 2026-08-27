#!/usr/bin/env python3
"""Print the CHANGELOG.md section for one release version.

Used by ``.github/workflows/release.yml`` to turn the changelog entry for a tag
into the body of the GitHub Release, so the release notes and the changelog can
never drift apart.

Usage::

    python scripts/extract_release_notes.py v1.2.3
    python scripts/extract_release_notes.py 1.2.3

Exits 1 when the changelog has no section for the requested version, or when
that section is empty. Tagging a version that was never written up in the
changelog is therefore a hard error rather than an empty release.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CHANGELOG = Path(__file__).resolve().parent.parent / "CHANGELOG.md"
HEADING_RE = re.compile(r"^##\s+\[([^\]]+)\]")


def normalize(version: str) -> str:
    return version.strip().lstrip("vV").strip()


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("usage: extract_release_notes.py <version>", file=sys.stderr)
        return 2

    wanted = normalize(argv[1])
    if not wanted:
        print("error: no version given", file=sys.stderr)
        return 2

    lines = CHANGELOG.read_text(encoding="utf-8").splitlines()

    start: int | None = None
    end = len(lines)
    available: list[str] = []

    for index, line in enumerate(lines):
        match = HEADING_RE.match(line)
        if not match:
            continue

        heading = match.group(1)
        available.append(heading)

        if start is None:
            if normalize(heading).lower() == wanted.lower():
                start = index + 1
        else:
            end = index
            break

    if start is None:
        print(
            f"error: CHANGELOG.md has no '## [{wanted}]' section. "
            f"Sections present: {', '.join(available) or 'none'}",
            file=sys.stderr,
        )
        return 1

    body = "\n".join(lines[start:end]).strip("\n")
    if not body.strip():
        print(f"error: the '## [{wanted}]' section of CHANGELOG.md is empty", file=sys.stderr)
        return 1

    print(body)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
