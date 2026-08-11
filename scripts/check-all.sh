#!/usr/bin/env bash
# Portfolio documentation validation suite.
set -u

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
fail=0

echo "== Links =="
python3 "$ROOT/scripts/check-links.py" || fail=1
echo

echo "== Placeholders / availability claims =="
python3 "$ROOT/scripts/check-placeholders.py" || fail=1
echo

echo "== Terminology consistency =="
python3 "$ROOT/scripts/check-consistency.py" || fail=1
echo

if [ "$fail" -eq 0 ]; then
    echo "ALL CHECKS PASSED"
else
    echo "CHECKS FAILED"
fi
exit $fail
