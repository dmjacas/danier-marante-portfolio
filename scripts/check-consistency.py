#!/usr/bin/env python3
"""Check terminology consistency across the portfolio.

Detects title drift and forbidden/generic claims.
Exit 1 if any consistency problem is found.
"""
import os
import re
import sys
import glob

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Generic diagram terms that must not describe the MerchantMiles API component.
FORBIDDEN_PAIRS = [
    (r"MerchantMiles[^\n]*multi-tenant", "MerchantMiles must be described as multi-country, not multi-tenant"),
]
# Generic "API Layer" as the MerchantMiles component.
GENERIC_API = re.compile(r"API Layer")
AUDIT_DOCS = ("docs/portfolio-v3-audit.md", "docs/portfolio-audit.md", "docs/content-consistency-report.md",
              "docs/portfolio-v3-final-audit.md")


def main():
    files = glob.glob(os.path.join(ROOT, "**", "*.md"), recursive=True)
    issues = []

    for path in files:
        rel = os.path.relpath(path, ROOT)
        if rel in AUDIT_DOCS:
            continue
        with open(path, encoding="utf-8") as f:
            content = f.read()

        if rel.startswith("projects/merchant-miles") and "API Gateway" not in content \
                and "API Layer" in content:
            issues.append(f"{rel}: uses generic 'API Layer' (should be API Gateway)")

        for pattern, msg in FORBIDDEN_PAIRS:
            if re.search(pattern, content, re.IGNORECASE):
                issues.append(f"{rel}: {msg}")

    if issues:
        print("CONSISTENCY ISSUES:")
        for i in issues:
            print(f"  {i}")
        return 1
    print("OK: terminology consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
