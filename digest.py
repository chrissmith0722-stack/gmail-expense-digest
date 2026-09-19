#!/usr/bin/env python3
"""Digest .eml receipt emails into expenses.csv."""

from __future__ import annotations

import argparse
import csv
import re
from email import policy
from email.parser import BytesParser
from pathlib import Path

AMOUNT_RE = re.compile(
    r"(?:total|amount|charged|paid)[:\s]*\$?\s*([0-9]+(?:\.[0-9]{2})?)",
    re.I,
)
FALLBACK_MONEY_RE = re.compile(r"\$\s*([0-9]+(?:\.[0-9]{2})?)")
CURRENCY_RE = re.compile(r"\b(USD|EUR|GBP)\b", re.I)

CATEGORY_HINTS = {
    "software": ["github", "aws", "openai", "notion", "adobe", "spotify"],
    "food": ["uber eats", "doordash", "grubhub", "starbucks"],
    "travel": ["uber", "lyft", "airline", "hotel", "airbnb"],
    "shopping": ["amazon", "target", "walmart"],
}


def guess_category(text: str) -> str:
    lower = text.lower()
    for category, needles in CATEGORY_HINTS.items():
        if any(n in lower for n in needles):
            return category
    return "other"


def extract_amount(text: str) -> tuple[str, str]:
    m = AMOUNT_RE.search(text) or FALLBACK_MONEY_RE.search(text)
    amount = m.group(1) if m else ""
    cur = CURRENCY_RE.search(text)
    currency = cur.group(1).upper() if cur else ("USD" if "$" in text else "")
    return amount, currency


def parse_eml(path: Path) -> dict:
    with path.open("rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)
    subject = msg.get("subject", "") or ""
    from_hdr = msg.get("from", "") or ""
    date = msg.get("date", "") or ""
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                body += part.get_content() or ""
    else:
        body = msg.get_content() or ""
    blob = f"{subject}\n{from_hdr}\n{body}"
    amount, currency = extract_amount(blob)
    merchant = from_hdr
    if "<" in from_hdr:
        merchant = from_hdr.split("<")[0].strip().strip('"') or from_hdr
    return {
        "date": date,
        "merchant": merchant,
        "amount": amount,
        "currency": currency,
        "category": guess_category(blob),
        "source_file": path.name,
    }


def collect_emls(inbox: Path) -> list[Path]:
    if inbox.is_file() and inbox.suffix.lower() == ".eml":
        return [inbox]
    return sorted(inbox.glob("*.eml"))


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("inbox", type=Path, help="Folder of .eml files or one .eml")
    parser.add_argument("--out", type=Path, default=Path("expenses.csv"))
    args = parser.parse_args()

    paths = collect_emls(args.inbox)
    if not paths:
        raise SystemExit(f"No .eml files found under {args.inbox}")

    rows = [parse_eml(p) for p in paths]
    fields = ["date", "merchant", "amount", "currency", "category", "source_file"]
    with args.out.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Wrote {len(rows)} rows to {args.out}")


if __name__ == "__main__":
    main()
