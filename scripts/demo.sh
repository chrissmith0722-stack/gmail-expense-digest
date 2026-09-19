#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
OUT="${TMPDIR:-/tmp}/gmail-expense-digest-demo.csv"

cd "$ROOT"
python3 digest.py sample_emails --out "$OUT"

# header + N data rows → report data row count
rows=$(($(wc -l < "$OUT") - 1))
echo "demo row count: $rows"

if [[ "$rows" -lt 1 ]]; then
  echo "demo failed: expected at least 1 sample row" >&2
  exit 1
fi
