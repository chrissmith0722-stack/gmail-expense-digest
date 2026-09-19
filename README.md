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
./scripts/demo.sh
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

`sample_emails/` ships sample receipts (Amazon, Notion, Uber, Starbucks). After `make demo` you should see **4** data rows (plus a header line in the CSV).

```bash
./scripts/demo.sh
# → demo row count: 4 (from 4 .eml files)
# → demo ok
```

## Troubleshooting

| Problem | What to try |
| --- | --- |
| `Inbox path not found` | Pass a real folder or `.eml` path: `python digest.py ./sample_emails --out out.csv` |
| `demo row count: 0` | Ensure `sample_emails/*.eml` exist and are plain-text receipts with a `$` amount |
| Amount blank in CSV | Body should include `Total:`, `Amount`, `Paid`, `charged`, or a `$12.34`-style amount on its own |
| Wrong category | Categories are keyword heuristics (e.g. `amazon`→shopping, `uber`→travel, `starbucks`→food). Edit `CATEGORY_HINTS` in `digest.py` for your merchants |
| `Permission denied: ./scripts/demo.sh` | `chmod +x scripts/demo.sh` or run `bash scripts/demo.sh` / `make demo` |
| Multipart / HTML-only mail | Digester prefers `text/plain` parts. Re-export as `.eml` with a plain-text body, or add a plain part |
| Encoding garbage | Files are read as bytes then decoded with replacement; re-save the `.eml` as UTF-8 if needed |
| Want live Gmail | Not built-in yet — export `.eml` manually or wire the Gmail API later; keep secrets out of the repo |

## Money angle

Local tool niche: sell as a simple Mac/Windows utility or wrap as a paid Notion/Sheets companion for people drowning in receipt email — not another freelancer cashflow spreadsheet.

## License

MIT
