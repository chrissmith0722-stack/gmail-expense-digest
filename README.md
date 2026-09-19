# gmail-expense-digest

Turn purchase / receipt emails into a clean `expenses.csv` for bookkeeping.

Works offline on `.eml` files first (no API keys). Live Gmail API can plug in later.

## Quick start

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python digest.py sample_emails --out expenses.csv
```

## Output columns

date, merchant, amount, currency, category, source_file

## Money angle

Local tool niche: sell as a simple Mac/Windows utility or wrap as a paid Notion/Sheets companion for people drowning in receipt email — not another freelancer cashflow spreadsheet.
