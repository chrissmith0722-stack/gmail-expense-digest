# gmail-expense-digest

Turn purchase / receipt emails into a clean `expenses.csv` for bookkeeping.

Works offline on `.eml` files first (no API keys). Live Gmail API can plug in later.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt   # optional; digester is stdlib-only today
python digest.py sample_emails --out expenses.csv
```

Or run the demo smoke target:

```bash
make demo
# or
bash scripts/demo.sh
```

Both run against `sample_emails/` and print the CSV row count.

## How it works

1. Reads each `.eml` with Python’s stdlib `email` parser.
2. Pulls `Date`, `From`, and plain-text body.
3. Heuristics extract amount (`Total` / `Amount` / `Paid` / `$…`), currency, and a coarse category (software / food / travel / shopping / other).
4. Writes one CSV row per email.

Export `.eml` from Gmail (or any client): open message → ⋮ → **Download message**, drop files into a folder, point `digest.py` at that folder.

## Output columns

| Column | Meaning |
| --- | --- |
| date | Email Date header |
| merchant | From display name when present |
| amount | Parsed number string |
| currency | USD/EUR/GBP or USD if `$` seen |
| category | Heuristic bucket |
| source_file | Original `.eml` filename |

## Demo / smoke

`sample_emails/` ships three receipts (Amazon, Notion, Uber). After `make demo` you should see **3** data rows (plus a header line in the CSV).

## Troubleshooting

| Symptom | Fix |
| --- | --- |
| `No .eml files found` | Pass a folder that contains `.eml` files, or a single `.eml` path |
| Empty `amount` | Forward/export the HTML receipt as `.eml`, or ensure body includes `Total` / `$12.34` |
| Wrong merchant | Edit CSV after, or improve From display name in the mail client |
| `Permission denied` on `./scripts/demo.sh` | Run `bash scripts/demo.sh` instead |
| Want Gmail API | Not wired yet — keep using downloaded `.eml` exports |

Companion category rules: https://github.com/chrissmith0722-stack/receipt-category-rules

## Money angle

Local tool niche: sell as a simple Mac/Windows utility or wrap as a paid Notion/Sheets companion for people drowning in receipt email — not another freelancer cashflow spreadsheet.
