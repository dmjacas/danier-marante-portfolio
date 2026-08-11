#!/usr/bin/env python3
"""Validate internal Markdown links in the portfolio.

Exit 1 if any internal link target does not exist.
"""
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main():
    broken = []
    files = glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)
    for path in files:
        rel = os.path.relpath(path, ROOT)
        base = os.path.dirname(path)
        with open(path, encoding="utf-8") as f:
            content = f.read()
        for link in re.findall(r"\[[^\]]*\]\(([^)]+)\)", content):
            if link.startswith(("http://", "https://", "#", "mailto:")):
                continue
            target = link.split("#")[0]
            if not target:
                continue
            if not os.path.exists(os.path.normpath(os.path.join(base, target))):
                broken.append(f"{rel}: {link}")

    if broken:
        print(f"BROKEN LINKS ({len(broken)}):")
        for b in broken:
            print(f"  {b}")
        return 1
    print("OK: no broken links")
    return 0


if __name__ == "__main__":
    sys.exit(main())
