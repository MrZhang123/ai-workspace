---
name: listed-company-financial-analysis
description: Analyze listed companies, stocks, annual reports, quarterly results, prospectuses, financial statements, valuation, business quality, cash flow quality, and investment risk. Use this skill whenever the user asks to analyze a public company, compare listed companies, interpret financial reports, judge valuation, assess financial health, or produce a stock/company research report. The final deliverable should normally be a structured HTML report with charts, tables, sources, calculation notes, valuation range, risks, and tracking checklist.
---

# Listed Company Financial Analysis

Use this skill to analyze public companies from original financial disclosures and produce a clear HTML report. The goal is not to make a price prediction. The goal is to turn reliable data into a disciplined business, financial, valuation, and risk assessment.

## Core Principles

1. Prefer original disclosures: annual reports, interim reports, quarterly results, prospectuses, investor presentations, company IR pages, exchange filings, and regulator filings.
2. Treat web search as a way to find primary documents. Do not use search snippets, news summaries, blogs, or AI summaries as the source of key financial numbers.
3. Separate facts, calculations, and judgment:
   - Facts are numbers or statements from identified sources.
   - Calculations come from `scripts/financial_calculator.py` or clearly shown formulas.
   - Judgment is the analyst's interpretation based on facts and calculations.
4. Every key number used in the final conclusion must show source, period, currency, accounting basis, and whether it is GAAP/IFRS or adjusted.
5. Keep raw financial data in the company's original reporting currency. For a single-company report, the final HTML report should normally use the company's reporting currency as the main display currency.
6. If key data conflicts, pause the valuation and report the conflict. Do not force a conclusion from uncertain data.
7. The final answer should be a short summary plus the path to the generated HTML report. The full analysis belongs in the HTML file.

## When Starting

Clarify or infer the following:

- Company name and ticker.
- Listing market.
- Analysis date.
- Whether this is a single-company report, comparison report, or quick earnings review.
- Whether the user provided local files. If not, look for original public filings.
- Whether current price and market data are required. If yes, record the quote source and retrieval date.
- Presentation currency. For a single-company report, default to the company's reporting currency. For a comparison report, apply the comparison currency rules below unless the user specifies another currency.

If the user asks for "latest", "current", "today", valuation based on current price, or market data, fetch current information before analysis.

## Currency Rules

- Preserve source data in the original reporting currency and original unit in the standardized JSON.
- For a single-company report, use the company's published financial-statement currency as the main display currency for financial-statement monetary charts, tables, market cap, enterprise value, net cash, and calculation details.
- In the top conclusion block and any stock-price comparison view, show current price, per-share value range, and margin-of-safety price first in the listing market's quote currency. For a Hong Kong-listed stock, use HKD first; for a U.S.-listed stock, use USD first. If the reporting currency differs, show the reporting-currency equivalent in the note, for example `HK$173.4 (about RMB 150.9)`.
- For valuation tables, include both the reporting-currency per-share value and the listing-currency equivalent when the two differ.
- For a comparison report, standardize display currency only for cross-company comparison:
  - Hong Kong-listed peer set: use HKD.
  - U.S.-listed peer set: use USD.
  - Mixed HKD, USD, RMB, or other currencies: use HKD by default.
  - If the comparison has a clearly dominant non-HKD market or the user specifies a currency, explain the chosen currency.
- Record every exchange rate used in the JSON `exchange_rates` section with source currency, target currency, rate, date, source, and use case.
- In single-company reports, only translate amounts needed for quote comparison or source-currency reconciliation. In comparison reports, prefer annual average FX rates for income-statement and cash-flow display, period-end FX rates for balance-sheet display, and quote-date spot FX rates for market price and valuation display. If complete period-specific rates are not practical, use a clearly labeled spot rate for display only.
- Run business growth, margin, ROE, ROIC, working-capital days, and red-flag calculations on the original reporting currency. Do not calculate operating trends from translated USD amounts unless the report explicitly analyzes FX translation.
- If reliable FX data cannot be verified, keep the affected monetary section in original currency and mark the data limitation in the report.

## Readability Rules

- When a table, chart, list, or conclusion uses an English financial abbreviation, add a short Chinese explanation the first time it appears in that section or directly in the header, for example `ROIC（投入资本回报率）`, `FCF（自由现金流）`, `OCF（经营现金流）`, `EPS（每股收益）`, `EV（企业价值）`, `DCF（现金流折现）`.
- For repeated table columns, prefer descriptive headers over unexplained abbreviations. Keep currency codes, stock tickers, and official brand or product names unchanged unless explanation is needed for readability.
- Wide tables should scroll horizontally inside their card or table container instead of compressing columns. Use a wrapper such as `.table-scroll`, set a practical `min-width` on the table, and keep key numeric/table headers on one line.
- Do not let chart labels, bars, legends, or table text overflow their card or section. Use `width: 100%`, `display: block`, `max-width: 100%`, responsive viewBox dimensions, and enough right-side padding for value labels.
- Before delivering an HTML report, check that charts fit inside their cards on both desktop and narrow widths when practical.

## Required Workflow

### 1. Build the source list

Create a source list before calculating:

| Source | Type | Period | Currency | Accounting basis | Use |
|---|---|---|---|---|---|
| Company annual report | Primary | FY2025 | RMB | IFRS | Financial statements |
| Exchange announcement | Primary | 2026 Q1 | RMB | IFRS | Latest quarter |
| Stock quote page | Market data | 2026-05-30 | HKD | N/A | Price and market cap |
| FX rate source | Market data | 2026-05-30 | HKD/RMB | N/A | Quote comparison or peer currency conversion |
| Exchange or regulator short-selling data | Market data | 2026-05-30 | N/A | N/A | Short-selling turnover, disclosed short positions, or data limitation |

Use source reliability levels from `references/data-quality.md`.

For short-selling data, use only exchange, regulator, broker, or other clearly identified market-data sources. Keep it separate from the fundamental bearish case. Short-selling turnover is not the same as outstanding short interest or disclosed short positions; label the metric exactly and avoid treating one as the other.

### 2. Set the analysis window and comparison set

Use comparison by default. A single year rarely shows business quality.

Default analysis window:

- Full company analysis: at least 5 fiscal years of annual data plus the latest interim or quarterly period.
- Mature or cyclical company: prefer 10 fiscal years if filings are available, so a full cycle is visible.
- Newly listed company: use all available listed-company history plus prospectus historical financials when reliable.
- Fast-changing or loss-making growth company: use 3 to 5 years plus every available recent quarter, because cash burn and margin change matter more than old history.
- Earnings update: use the latest quarter, the same quarter last year, year-to-date data, and the last 4 to 8 quarters when available.

Default comparison set:

- Self history: compare the company against its own past margins, ROE, ROIC, free cash flow, debt, and valuation.
- Peer comparison: include 2 to 5 peers when good peers exist.
- Industry or market reference: include one broad reference when peers are weak or business models differ.

Peer selection rules:

- Prefer companies with similar business model, customer base, accounting period, and geography.
- If direct peers do not exist, use adjacent peers but explain the limitation.
- Do not force direct ratio comparison when accounting standards, fiscal year ends, or segment definitions make the numbers misleading.
- For cross-market peers, separate operating comparison from valuation comparison, because market discount rates can differ.

### 3. Extract standardized data

Extract raw financial data into the JSON shape described in `schemas/financial-data.schema.json`.

Keep data extraction conservative:

- Preserve original units and currency first.
- Convert units only after recording the original.
- Add `presentation.display_currency` and `exchange_rates` when the report translates market quotes or standardizes currencies for comparison.
- Do not mix fiscal years and calendar years without noting it.
- Do not mix GAAP/IFRS with non-GAAP/non-IFRS in the same trend table unless clearly labeled.
- For ADS, ordinary shares, split shares, and weighted average shares, show the conversion basis.

### 4. Run calculations

Use:

```bash
python3 scripts/financial_calculator.py input.json --format markdown
python3 scripts/financial_calculator.py input.json --format json
```

The script calculates:

- Growth rates.
- Margins.
- ROA, ROE, ROIC, FCF margin.
- Basic DuPont metrics.
- Working-capital days and cash conversion cycle.
- Leverage and liquidity ratios.
- Cash-flow coverage.
- EVA if WACC is provided.
- Basic red flags.
- DCF scenarios if inputs are provided.

Never rely on mental arithmetic for important ratios or valuation ranges. If a calculation is not supported by the script, show the formula, input values, and result in the report.

### 5. Classify the company

Before valuation, classify the company. Use `references/company-types.md`.

Common types:

- Stable profitable company.
- High-quality compounder.
- Fast grower.
- Loss-making growth company.
- Cyclical company.
- Turnaround company.
- Asset-based company.
- Financial company.

Different types need different valuation methods. Do not apply one valuation template to every company.

### 6. Analyze business and financial quality

Use `references/framework.md` as the main structure:

1. Business understanding and circle of competence.
2. Company type.
3. Growth and growth sources.
4. Profitability and capital return.
5. Moat and whether financial data supports it.
6. Financial health.
7. Accounting quality and warning signs.
8. Management and capital allocation.
9. Short case / negative case.
10. Valuation.
11. Margin of safety.
12. Tracking checklist.

The short case is required for full company analysis. It means standing on the opposite side of the thesis and listing why the investment could fail, why investors may sell or short the stock, which facts would confirm that view, and whether the negative evidence outweighs the positive evidence. If reliable market short-selling data is available, include it as a separate market-sentiment subsection; if not, state that it was not verified.

Allow early stop decisions:

- Stop if the business cannot be understood well enough.
- Stop if financial data has major unresolved inconsistencies.
- Stop if accounting quality has material red flags.
- Stop if valuation depends mostly on unverifiable long-range assumptions.
- Stop if current price has no reasonable margin of safety.

### 7. Build the HTML report

Final deliverable is normally a single-file HTML report:

- Inline CSS and JavaScript.
- No external CDN unless unavoidable.
- Charts should render from embedded data.
- Chart SVG elements must be sized by their container, not by a fixed intrinsic width that can overflow a card.
- Tables should be readable, numbers right-aligned, and wide tables horizontally scrollable instead of visually squeezed.
- Include a "Sources and Method" section.
- Include a currency note that explains original reporting currency, display currency, FX source, FX date, and which sections use translated amounts.
- Include formulas or calculation notes for key ratios.
- Include a clear disclaimer that the report is not investment advice.

Use `templates/report-template.html` as the starting structure. Adapt it to the company and report type.

Recommended charts:

- Revenue and growth trend.
- Operating profit, net profit, and margins.
- Operating cash flow and free cash flow.
- ROE, ROIC, and FCF margin.
- Segment revenue and segment profit.
- Cash, debt, and net cash/net debt.
- Current price versus valuation range.
- Peer comparison by default: revenue growth, margins, ROE/ROIC, FCF margin, leverage, valuation multiples, and company type differences.

If generating a local web report for the user, also generate a first-screen PNG preview when practical.

## Report Requirements

The report must start with a conclusion block:

- Current judgment: attractive, reasonable, expensive, wait, avoid, or cannot conclude.
- Reasonable per-share value range in the listing market's quote currency in the top conclusion block, with reporting-currency details in the valuation section when different.
- Current price in the listing market's quote currency, with the reporting-currency equivalent in the note when different, and quote date if used.
- Margin of safety price in the listing market's quote currency, with the reporting-currency equivalent in the note when different.
- Three strongest supporting points.
- Three main risks.
- Data confidence: high, medium, or low.

Then provide structured sections:

1. Scope and source list.
2. Business model.
3. Financial snapshot.
4. Growth analysis.
5. Profitability and capital return.
6. Cash flow and financial health.
7. Accounting quality checks.
8. Moat and competition.
9. Management and capital allocation.
10. Short case / negative case.
11. Valuation and sensitivity analysis.
12. Tracking checklist.
13. Sources, formulas, and disclaimers.

The short case / negative case section should include:

- Fundamental bearish arguments.
- Why market participants may sell or short the stock.
- Which operating or financial indicators would confirm the bearish view.
- Official short-selling or short-position data when reliable and relevant, clearly separated from the fundamental analysis.
- A final judgment on whether the negative evidence outweighs the positive evidence.

## Important Output Rules

- Keep the chat reply short. Do not paste the whole report into the chat.
- Link to the HTML file path.
- Mention whether calculations were run and whether any data could not be verified.
- If market data was used, state the retrieval date.
- Do not present uncertain numbers as confirmed.
- Do not provide personalized investment advice. Use analysis language, not instructions to buy or sell.

## Bundled Files

- `references/framework.md`: Analysis framework based on the user's notes, Peter Lynch, and The Five Rules for Successful Stock Investing.
- `references/data-quality.md`: Data source hierarchy and common data errors.
- `references/company-types.md`: Company classification and valuation method selection.
- `schemas/financial-data.schema.json`: Standard data input schema for calculations.
- `scripts/financial_calculator.py`: Deterministic financial metric and DCF calculator.
- `templates/report-template.html`: Single-file HTML report scaffold.
