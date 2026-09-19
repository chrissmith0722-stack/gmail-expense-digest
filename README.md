# gmail-expense-digest

Turn purchase / receipt emails into a clean `expenses.csv` for bookkeeping.

Works **offline on `.eml` files** first (no API keys). Live Gmail API can plug in later.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt   # optional today; deps reserved for Gmail API
python digest.py sample_emails --out expenses.csv
```

You should see something like `Wrote 3 rows to expenses.csv`.

## Output columns

| Column | Meaning |
| --- | --- |
| `date` | Email Date header |
| `merchant` | Parsed From display name |
| `amount` | First total/amount/$ match |
| `currency` | USD/EUR/GBP if present, else USD when `$` seen |
| `category` | Heuristic: software / food / travel / shopping / other |
| `source_file` | Source `.eml` filename |

## Sample inbox

`sample_emails/` includes Amazon, Notion, and Uber receipts so you can demo without connecting Gmail.

Export more from any client as `.eml` and drop them in a folder.

## Security notes

- Do **not** commit real mailbox exports; `expenses.csv` is already gitignored.
- This tool only reads local files; it does not send data anywhere.

## Roadmap toward shippable / sellable

1. Add Gmail API OAuth path behind a `--gmail` flag (deps already sketched in `requirements.txt`).
2. Harden amount parsing (multi-currency, tax lines, refunds) + a tiny test suite on `sample_emails/`.
3. Package as a one-command CLI (`pipx` / PyInstaller) with a short Gumroad/Etsy listing.

## Money angle

Local tool niche: sell as a simple Mac/Windows utility or wrap as a paid Notion/Sheets companion for people drowning in receipt email — not another freelancer cashflow spreadsheet.

## License

MIT — see [LICENSE](LICENSE).
