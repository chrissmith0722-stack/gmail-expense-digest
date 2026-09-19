# How to sell Gmail Expense Digest

Short path: package the **offline `.eml` digester** (this repo), upload **one** publish-ready zip, list on Gumroad (or Etsy). **No Gmail OAuth** in the sellable product.

## 1. One SKU only

| Zip (publish-ready) | Role | Price |
| --- | --- | ---: |
| **`Gmail-Expense-Digest.zip`** | **Only sellable product** — full buyer pack (README + START-HERE + SETUP + FAQ + listing + golden demo CSV) | **$19** |

**Morning / first-dollar rule:** list **one** SKU — **`Gmail-Expense-Digest.zip` @ $19**. Do **not** dual-list Offline vs Tool. Prior Offline ($15) / Tool ($29) ladder is **void / superseded**.

Publish-ready filename (attach this to the listing):

- `Gmail-Expense-Digest.zip`

Listing paste: `LISTING-gumroad.md` inside the zip.

## 2. Align the listing with the zip

Every bullet on the storefront must exist in the download (or be removed from the listing). Use [BUYER_README.md](BUYER_README.md).

**Must-claim (true for offline product):**

- Offline `.eml` → `expenses.csv`
- No Gmail login / no OAuth / no Google Cloud / no API keys
- Python 3.9+ stdlib only
- Sample receipts + one-command demo

**Must not claim:**

- Live Gmail sync or auto-inbox access
- Tax / accounting / legal advice
- Affiliation with Google / Gmail

## 3. Ship checklist

1. Unzip `Gmail-Expense-Digest.zip` yourself; run `python3 digest.py sample_emails --out expenses.csv` (expect **4** data rows).
2. Confirm listing bullets ↔ filenames (see BUYER_README promise map).
3. Attach cover(s) if you have them; set price **$19**; enable instant download.
4. Publish → save public URL. Stop condition: live listing with price > $0.

## 4. Publish

| Channel | Action |
| --- | --- |
| **Gumroad** | New digital product → upload **`Gmail-Expense-Digest.zip`** → paste listing → **$19** → Publish |
| **Etsy** | Digital download → same promise + tags → Publish (optional second channel) |

## 5. After first sale

- Reply to purchase-email support questions (FAQ covers OAuth, Windows, accuracy).
- Cross-sell cashflow / ledger kits for people who already have the CSV.
- Keep this GitHub repo as source / MIT reference — sell the **zip**, not “clone the repo for $19”.

## What not to do

- Do not market OAuth / Gmail API as included
- Do not invent features (bulk Takeout conversion, mobile app, cloud sync) that are not in the zip
- Do not dual-publish Offline + Tool (or any second digester SKU)
- Do not wait for a perfect funnel — one live paid listing beats a polished draft
