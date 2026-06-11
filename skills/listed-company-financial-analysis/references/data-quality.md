# Data Quality Rules

## Source Priority

Use this order when collecting data:

1. Company original disclosures: annual report, interim report, quarterly result, prospectus, investor presentation, official IR page.
2. Exchange or regulator filings: HKEX, SEC EDGAR, SSE, SZSE, BSE, company announcement systems.
3. Market data providers: exchange quote, Yahoo Finance, StockAnalysis, TradingView, Webull, S&P, Wind, Bloomberg, FactSet, Refinitiv, or similar.
4. News, sell-side notes, blogs, social posts, and AI summaries.

Rules:

- Financial statement numbers should come from levels 1 or 2 whenever available.
- Market price, market cap, EV, and analyst forecasts can come from level 3, but must show source and retrieval date.
- Level 4 sources are leads only. Do not use them as the source for key financial numbers unless they point back to primary documents and those documents are checked.

## Required Metadata for Key Numbers

For each key number used in the conclusion, record:

- Company and ticker.
- Source file or URL.
- Filing date or report date.
- Financial period.
- Currency.
- Unit.
- Accounting basis: IFRS, US GAAP, PRC GAAP, non-GAAP, non-IFRS, adjusted, or management metric.
- Whether the number is as reported or calculated.

## Common Error Sources

Check these before analysis:

- Similar company names or wrong ticker.
- Different listing lines, such as HKD/RMB counters or ADR/ordinary shares.
- Fiscal year versus calendar year.
- Quarterly, half-year, TTM, and annual periods mixed together.
- RMB, HKD, USD, JPY, EUR, or local currency mixed together.
- GAAP/IFRS numbers mixed with adjusted numbers.
- ADS-to-ordinary-share conversion.
- Weighted average shares versus period-end shares.
- Restatements, discontinued operations, asset sales, or accounting policy changes.
- Segment reporting changes.
- Negative free cash flow hidden by asset sales or investment redemptions.
- Share-based compensation and dilution not considered.

## Conflict Handling

If sources disagree:

1. Prefer the company's original filing over third-party pages.
2. Prefer the latest restated filing over the original filing.
3. Prefer the period-specific report over a summary page.
4. If the conflict remains material, mark the data as unresolved and do not use it for valuation.

## Data Confidence Labels

Use these labels in the final report:

- High: key financials come from original filings, calculations are reproducible, market data has date and source.
- Medium: original filings are available but some market or forecast data comes from third parties.
- Low: key financials or valuation assumptions depend on unverified secondary sources.
