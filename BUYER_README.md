# Buyer README — offline `.eml` product alignment

**Who this is for:** You are packaging or sold **Gmail Expense Digest** and need the **storefront promise** to match what the buyer downloads.

**What this product is:** An **offline** digester — export receipt emails as `.eml`, run one Python command, get `expenses.csv`. **Not** a Gmail OAuth app and **not** a cashflow spreadsheet.

---

## Promise ↔ delivery map

| Marketplace claim (listing) | Must be true in the download |
| --- | --- |
| Offline / no Gmail login / no OAuth | `digest.py` runs on local `.eml` files only; no Google credentials |
| Instant digital download | Zip attaches and opens without a login wall |
| Receipt / purchase email → expenses CSV | `digest.py` writes date, merchant, amount, currency, category, source_file |
| Sample / demo included | `sample_emails/*.eml` (4 fictional receipts) + runnable demo |
| Works on Mac / Windows / Linux | Python **3.9+**; stdlib-only path documented |
| Setup / FAQ | `SETUP.md` + `FAQ.md` present in the zip |
| "What's included" bullet list | Same filenames (or clear README map) inside the zip |
| Support line | Real reply path (purchase email or stated channel) |

If a bullet is on the listing, it belongs in the zip **or** the buyer-facing README must say why it is not.

---

## Publish-ready zip (ONE SKU)

| Zip | Buyer experience | Price |
| --- | --- | ---: |
| **`Gmail-Expense-Digest.zip`** | Full buyer pack: README, README-START-HERE, SETUP, FAQ, LISTING-gumroad, demo golden CSV, samples, `digest.py` | **$19** |

**Do not dual-list** Offline / Tool as separate products. Prior `Gmail-Expense-Digest-Offline.zip` and a separate Tool tier are **superseded** — one upload only.

---

## Suggested buyer-facing README (paste into the product zip if missing)

Keep this short. Buyers skim.

```text
# Start here — Gmail Expense Digest (offline)

Thanks for buying. This tool turns downloaded receipt emails (.eml) into expenses.csv.
No Gmail login. No OAuth.

## Open these first
1. README.md — quick start
2. SETUP.md — Python install notes
3. FAQ.md — common questions

## 60-second demo
python3 digest.py sample_emails --out expenses.csv
# Expect 4 sample rows (Amazon, Notion, Starbucks, Uber)

## Your own receipts
1. Gmail → open receipt → ⋮ → Download message (.eml)
2. Put .eml files in a folder (e.g. ./inbox)
3. python3 digest.py ./inbox --out expenses.csv
4. Open expenses.csv in Sheets / Excel / Numbers

## What's in this download
- digest.py — offline digester (Python stdlib)
- sample_emails/ — demo receipts
- scripts/demo.sh + Makefile — one-command smoke test
- SETUP.md, FAQ.md, demo/expected-expenses.csv, LISTING-gumroad.md

## Support
Reply to your purchase receipt email.

## License (plain language)
MIT for your own workflow. Do not resell or redistribute this product pack as your own digital product.

## Disclaimer
Heuristic email parser for personal productivity. Not tax, accounting, or legal advice.
Spot-check amounts before bookkeeping. Sample emails are fictional. Not affiliated with Google / Gmail.
```

---

## Align before publish

1. Open the zip you will upload (`Gmail-Expense-Digest.zip`).
2. Compare listing bullets to the table above.
3. Run the demo yourself; fix copy or contents until every claim is true.
4. See [HOW_TO_SELL.md](HOW_TO_SELL.md) for publish steps.

---

## Related

- [HOW_TO_SELL.md](HOW_TO_SELL.md) — single SKU → listing → publish checklist
- [README.md](README.md) — developer / repo quick start
