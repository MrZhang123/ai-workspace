# Listed Company Analysis Framework

This framework adapts the user's notes, Peter Lynch's common-sense company classification and growth-source analysis, and the quality, moat, cash-flow, and margin-of-safety approach in The Five Rules for Successful Stock Investing.

## 0. Data and Scope

Before analysis:

- Identify company, ticker, exchange, currency, fiscal year end, and accounting standard.
- List all source documents.
- Decide whether this is a single-company report, peer comparison, or earnings update.
- Set the analysis window:
  - Full company analysis: at least 5 fiscal years plus the latest interim or quarterly period.
  - Mature or cyclical company: prefer 10 fiscal years if available.
  - Newly listed company: use all listed-company history plus prospectus history when reliable.
  - Fast-changing or loss-making growth company: use 3 to 5 years plus recent quarters.
  - Earnings update: use latest quarter, same quarter last year, year-to-date data, and last 4 to 8 quarters when available.
- Set the comparison set:
  - Self history is always required.
  - Add 2 to 5 peers when reasonable peers exist.
  - Add industry or market reference when peers are weak or business models differ.
- Extract raw data before making judgments.
- Run calculations using the bundled calculator where possible.

## 1. Business Understanding

Ask:

- How does the company make money?
- Who are the customers?
- What does the company sell?
- What are the main cost drivers?
- What industry stage is it in?
- Who are suppliers, customers, and competitors?
- Is the business within the analyst's circle of competence?

Early stop:

- If the business cannot be understood well enough, stop or mark the conclusion as low confidence.

## 2. Company Type

Classify the company using `company-types.md`.

This matters because the same ratio can mean different things:

- A low P/E can be cheap for a stable company but a value trap for a cyclical company at peak profit.
- A high P/S may be unacceptable for a mature company but explainable for a loss-making growth company if the path to profit is credible.
- P/B is central for banks but often weak for asset-light software or internet companies.

## 3. Growth Analysis

Core question: how fast is the company growing, what drives that growth, and can it continue?

Analyze:

- Revenue growth.
- Gross profit growth.
- Operating profit growth.
- Net profit growth.
- Free cash flow growth.
- Segment growth.
- Customer, volume, price, or order metrics when disclosed.

Growth sources:

1. More units or more users.
2. Higher price.
3. New products or services.
4. Acquisitions.

Warnings:

- Profit grows much faster than revenue for many years without a clear operating explanation.
- Growth comes mainly from cost cuts.
- Growth comes mainly from acquisitions.
- Growth depends on subsidies that damage unit economics.
- Revenue grows while operating cash flow weakens.

## 4. Profitability and Capital Return

Core question: how much profit does the company earn on the capital it uses?

Calculate:

- Gross margin.
- Operating margin.
- Net margin.
- ROA.
- ROE.
- ROIC.
- Free cash flow margin.
- EVA if WACC is available.

DuPont:

`ROE = Net margin x Asset turnover x Equity multiplier`

Use DuPont to identify whether ROE comes from margin, asset efficiency, or leverage.

ROIC matters more than ROE for most non-financial companies because ROE can be lifted by leverage or buybacks.

## 5. Moat and Competitive Advantage

Core question: can growth and returns last?

Common moat sources:

- Brand.
- Switching cost.
- Network effect.
- Cost advantage.
- Scale advantage.
- Regulation, license, or patents.
- Distribution or data advantage.

Validate the moat with financial evidence:

- Stable or rising margins.
- ROIC above WACC for several years.
- Low customer churn or high repeat purchase when disclosed.
- Pricing power.
- Low required sales expense for growth.
- Resilience during competition or weak macro periods.

If competition causes margins and cash flow to collapse, reduce the moat assessment even if the business sounds strong in theory.

## 6. Financial Health

Analyze:

- Cash and short-term investments.
- Interest-bearing debt.
- Net cash or net debt.
- Current ratio.
- Quick ratio.
- Debt to equity.
- Interest coverage.
- Debt maturity when disclosed.
- Operating cash flow to current liabilities.
- Cash-flow adequacy.
- Cash runway for loss-making companies.

Cash-flow lifecycle:

| Stage | Operating cash flow | Investing cash flow | Financing cash flow |
|---|---|---|---|
| Startup | Negative | Large outflow | Main source of funds |
| Growth | Improving but tight | Outflow | External funding may remain |
| Mature | Strong | Reinvestment or investment | Buybacks/dividends/debt repayment |
| Decline or stress | Falling or negative | Asset sales may appear | Funding weakens |

## 7. Accounting Quality and Warning Signs

Start with:

- Net profit versus operating cash flow.
- Revenue versus accounts receivable.
- Gross margin changes.
- Inventory growth versus revenue.
- One-off charges.
- Auditor or CFO changes.
- Related-party transactions.
- Capitalized expenses.
- Goodwill and impairment.
- Tax expense versus reported profit.

Common red flags:

- Net profit rises while operating cash flow falls.
- Accounts receivable grows faster than revenue.
- Inventory grows faster than revenue and cost of sales.
- Repeated "one-time" charges.
- Frequent acquisitions.
- Major auditor or CFO changes.
- Large year-end sales adjustments.
- Related-party revenue or unusual transactions.
- Large gap between reported profit and taxable income.

Early stop:

- If accounting quality has unresolved material red flags, stop before valuation.

## 8. Management and Capital Allocation

Analyze:

- Founder or professional management.
- Ownership and voting control.
- Compensation and incentives.
- Share dilution.
- Buybacks and dividends.
- Major acquisitions or divestitures.
- Debt use.
- Whether management's prior statements matched results.

Good capital allocation should show up in per-share value, not only company size.

**State-owned enterprise (SOE) governance risk:** If the company is controlled by a local government (municipal or provincial SASAC) that created it from scratch and remains the dominant shareholder, additionally reference `references/governance-risks.md`. Standard "rational actor" assumptions about profit maximization, capital discipline, and management incentives may not fully apply.

## 9. Short Case / Negative Case

This is the user's "空头情形" step. It is not only a generic risk list. Stand on the opposite side of the thesis and ask why the investment could fail, why investors may sell or short the stock, and what evidence would prove the short case right.

List why the investment case could fail:

- Competition.
- Regulation.
- Technology change.
- Customer concentration.
- Supplier constraint.
- Margin pressure.
- Weakening cash flow.
- Dilution.
- Financing risk.
- Valuation already reflecting optimistic assumptions.

Also check market short data when reliable sources are available:

- Short-selling turnover.
- Disclosed short positions or short interest.
- Borrow cost or securities lending pressure when a reliable source is available.
- Large changes in short activity around earnings, regulatory events, or accounting concerns.

Keep these market indicators separate from the fundamental short case. Short-selling turnover does not equal outstanding short interest, and a high short-selling ratio does not by itself prove the company is weak.

This section should be specific and measurable. For each risk, identify a future indicator that would confirm or reduce the risk. If negative evidence clearly outweighs the positive case, stop before valuation or mark the conclusion as avoid / cannot conclude.

## 10. Valuation

Use the company type to choose methods.

Common methods:

- P/E for stable profitable companies.
- EV/EBIT or EV/EBITDA for operating businesses.
- FCF yield for cash-generative businesses.
- DCF for companies with reasonably forecastable cash flows.
- P/S and path-to-profit for loss-making growth companies.
- P/B and ROE for financial companies.
- Mid-cycle earnings for cyclicals.
- NAV or sum-of-the-parts for asset-based companies.

DCF rules:

- Use optimistic, base, and pessimistic scenarios.
- Show discount rate, terminal growth, FCF base, growth rates, net cash, share count.
- Do not produce a single-point valuation without sensitivity analysis.
- If FCF is currently negative, explain why and when it can turn positive before using DCF.

## 11. Margin of Safety

Determine required margin of safety:

- Strong, understandable, cash-generative company with durable moat: about 20% or more.
- Average company: about 30% to 40%.
- High-risk, weak moat, high uncertainty, or loss-making company: about 50% to 60% or more.

`Buyable price = intrinsic value x (1 - margin of safety)`

Do not confuse "good company" with "good price".

## 12. Tracking Checklist

End the report with 5 to 10 indicators to track in future reports:

- Revenue growth.
- Segment growth.
- Margin trend.
- ROIC or FCF margin.
- Operating cash flow.
- Cash and debt.
- Customer or unit metrics.
- Competitive pricing or subsidy intensity.
- Capital expenditure.
- Share dilution or buyback.
