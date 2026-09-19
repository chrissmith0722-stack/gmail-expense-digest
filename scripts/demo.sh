#!/usr/bin/env bash
# Smoke demo: digest sample_emails → temp CSV, print data-row count.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${TMPDIR:-/tmp}/gmail-expense-digest-demo.csv"

cd "$ROOT"

if [[ ! -d sample_emails ]]; then
  echo "demo failed: sample_emails/ missing" >&2
  exit 1
fi

shopt -s nullglob
emls=(sample_emails/*.eml)
shopt -u nullglob
if [[ ${#emls[@]} -lt 1 ]]; then
  echo "demo failed: no .eml files in sample_emails/" >&2
  exit 1
fi

python3 digest.py sample_emails --out "$OUT"

# header + N data rows → report data row count
rows=$(($(wc -l < "$OUT") - 1))
echo "demo row count: $rows (from ${#emls[@]} .eml files)"

if [[ "$rows" -lt 1 ]]; then
  echo "demo failed: expected at least 1 sample row" >&2
  exit 1
fi

# Soft expectation: ship ≥3 samples; warn (don't fail) if fewer than files parsed
if [[ "$rows" -ne "${#emls[@]}" ]]; then
  echo "warning: row count ($rows) != eml count (${#emls[@]})" >&2
fi

echo "demo ok"
