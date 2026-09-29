#!/usr/bin/env python3
"""Verify that every relative link in the repo's Markdown resolves.

Scans all tracked ``*.md`` files for Markdown links (``[text](target)``) and
inline HTML ``href``/``src`` attributes. External links (http, https, mailto,
tel), pure anchors (``#section``), and anything inside fenced or inline code
are ignored. Relative targets are resolved against the file that contains
them; a target that points at a path which does not exist is reported.

Exits non-zero if any relative link is broken, so CI can gate on it.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", ".pytest_cache"}

LINK_RE = re.compile(r"\[[^\]]*\]\(\s*<?([^)\s>]+)>?[^)]*\)")
HREF_RE = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", re.IGNORECASE)
FENCE_RE = re.compile(r"```.*?```|~~~.*?~~~", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]*`")
SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")


def strip_code(text: str) -> str:
    """Remove fenced and inline code so example links aren't checked as real."""
    text = FENCE_RE.sub("", text)
    return INLINE_CODE_RE.sub("", text)


def is_external(target: str) -> bool:
    return bool(SCHEME_RE.match(target)) or target.startswith("//")


def broken_target(md_file: Path, target: str) -> str | None:
    """Return the missing resolved path, or None if the link is fine/ignored."""
    target = target.strip()
    if not target or target.startswith("#") or is_external(target):
        return None
    path_part = re.split(r"[#?]", target, maxsplit=1)[0]
    if not path_part:
        return None
    resolved = (md_file.parent / path_part).resolve()
    return None if resolved.exists() else str(resolved)


def main() -> int:
    md_files = [
        p
        for p in ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in p.parts)
    ]
    broken: list[tuple[Path, str, str]] = []
    for md in sorted(md_files):
        text = strip_code(md.read_text(encoding="utf-8"))
        for target in LINK_RE.findall(text) + HREF_RE.findall(text):
            missing = broken_target(md, target)
            if missing:
                broken.append((md.relative_to(ROOT), target, missing))

    if broken:
        print(f"Found {len(broken)} broken relative link(s):\n")
        for src, link, resolved in broken:
            print(f"  {src}: [{link}] -> missing {resolved}")
        return 1

    print(f"All relative links resolve across {len(md_files)} Markdown files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
