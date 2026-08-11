#!/usr/bin/env python3
"""Check for placeholder markers and unauthorized availability claims.

- Placeholders ([TBD], [Metric to validate], [Confidential], ...) are expected
  in tracking/audit docs and produce a warning.
- Unauthorized availability/SLA/uptime percentages (e.g. "99.9% availability")
  are never acceptable and produce an error (exit 1).
"""
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PLACEHOLDER_RE = re.compile(r"\[TBD\]|\[Metric to validate\]|\[To validate\]|\[Confidential\]|\[TODO\]")
SLA_RE = re.compile(r"\b\d{1,2}(?:\.\d+)?%?\s*(availability|uptime|SLA)\b", re.IGNORECASE)
# Allow the sentence that documents the policy itself.
ALLOWED_SLA_SENTENCES = ("availability metrics are not publicly disclosed",
                         "no availability percentage",
                         "no sla", "no uptime")


def main():
    files = glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)
    placeholders = []
    unauthorized = []

    for path in files:
        rel = os.path.relpath(path, ROOT)
        with open(path, encoding="utf-8") as f:
            content = f.read()

        for m in PLACEHOLDER_RE.finditer(content):
            placeholders.append(f"{rel}: {m.group(0)!r}")

        for m in SLA_RE.finditer(content):
            line_start = content.rfind("\n", 0, m.start()) + 1
            line = content[line_start:content.find("\n", m.start())]
            if any(allow in line.lower() for allow in ALLOWED_SLA_SENTENCES):
                continue
            unauthorized.append(f"{rel}: {m.group(0)!r}")

    if placeholders:
        print(f"PLACEHOLDERS ({len(placeholders)}) — expected in tracking/audit docs:")
        for p in placeholders:
            print(f"  {p}")
        print()

    if unauthorized:
        print(f"UNAUTHORIZED AVAILABILITY CLAIMS ({len(unauthorized)}):")
        for u in unauthorized:
            print(f"  {u}")
        return 1

    print("OK: no unauthorized availability/SLA/uptime claims")
    return 0


if __name__ == "__main__":
    sys.exit(main())
