---
name: company-analysis
description: Analyze a company using a structured 10-step framework from financial reports to valuation. Use when the user wants to analyze a company's financials, evaluate a stock, assess a company's intrinsic value, or review an earnings report. Triggers include phrases like "分析一下这家公司""看看这个财报""公司估值""这个股票怎么样""帮我做个公司分析""analyze this company""stock valuation""earnings analysis", or any situation where the user provides financial statements (PDF, images, or data) and wants a structured investment analysis.
---

# Company Analysis

A structured 10-step workflow for analyzing a company from financial reports to a buy/hold/pass decision. The framework is based on *The Five Rules for Successful Stock Investing* (《股市真规则》)、《财务报表分析》、《彼得林奇的成功投资》and related investment literature.

Read [references/analysis-framework.md](references/analysis-framework.md) before starting. It contains the detailed indicators, formulas, thresholds, and decision criteria for each step.

## Input

The user provides one or more of:
- Company name (you search for publicly available data)
- Financial report files (PDF, images, or pasted data)
- Specific financial metrics or statements
- Market data (current price, market cap) — optional, needed for valuation steps

## Workflow

The workflow has two layers: **data extraction + calculation** (automated via Python) and **qualitative analysis** (LLM judgment). Work through the 10 steps sequentially. At exit points, make a judgment call: if the issue is clearly fatal, recommend stopping and explain why; if borderline, flag the concern and continue.

### Data Pipeline

For steps involving financial calculations (2, 3, 5, 6, 9), use the Python calculator:

1. **Extract**: Read the financial report (PDF/image). Extract raw numbers into `PeriodData` fields. When multiple periods are available, extract all periods for trend analysis.
2. **Calculate**: Write the extracted data as JSON and run `python scripts/financial_calculator.py data.json`. The script computes all indicators, trend comparisons, red flag detection, and DCF valuation automatically.
3. **Interpret**: Use the script output as the factual basis. Add qualitative interpretation and judgment.

```json
// data.json 示例结构
{
  "periods": [
    {
      "period": "2023",
      "revenue": 94495000000,
      "cost_of_revenue": 61264000000,
      "gross_profit": 33231000000,
      "operating_income": 15865000000,
      "net_income": 12789000000,
      "interest_expense": 520000000,
      "ebit": 16385000000,
      "total_assets": 189000000000,
      "total_equity": 98500000000,
      "current_assets": 78000000000,
      "current_liabilities": 52000000000,
      "cash_and_equivalents": 35000000000,
      "short_term_debt": 5000000000,
      "long_term_debt": 12000000000,
      "accounts_receivable": 8500000000,
      "inventory": 3200000000,
      "accounts_payable": 15000000000,
      "operating_cashflow": 22000000000,
      "capex": 6500000000,
      "debt_repayment": 3000000000,
      "dividends_paid": 2000000000,
      "shares_outstanding": 20800000000,
      "effective_tax_rate": 0.15,
      "eps": 0.615
    }
  ],
  "market_cap": 250000000000,
  "current_price": 120.0,
  "eps_growth_rate": 0.12,
  "dividend_yield": 0.01
}
```

### Step 1: Business Understanding
Describe the business model, industry position, competitive landscape, and upstream/downstream relationships. Assess whether this business is understandable. If the business is too complex or opaque to reason about confidently, recommend stopping here.

### Step 2: Growth Analysis
**Uses calculator**: `analyze_growth()` + `multi_period_summary()`

Examine revenue growth vs earnings growth across multiple periods. Calculate sustainable growth rate. Decompose growth into its four sources (volume, pricing, new products, acquisitions). Flag red flags: earnings persistently outpacing revenue, cost-cutting-driven growth, acquisition-dependent growth.

### Step 3: Profitability Analysis
**Uses calculator**: `analyze_profitability()`

Calculate all profitability indicators:
- **Basic**: ROA, ROE, ROIC, FCF, gross/net margins
- **DuPont**: Basic (3-factor) and Advanced (operating vs financing decomposition). Check whether ROE is driven by operational excellence or financial leverage via the "spread" (差价).
- **Efficiency**: AR/inventory/AP turnover days, cash conversion cycle, operating working capital
- **EVA**: Whether the company creates or destroys shareholder value beyond cost of capital

### Step 4: Competitive Advantage / Moat
Assess whether the growth and profitability from steps 2-3 are sustainable. Identify moat sources: brand, switching costs, network effects, cost advantages, licenses/patents. The width of the moat directly affects the discount rate used later in DCF.

### Step 5: Financial Health
**Uses calculator**: `analyze_financial_health()`

Evaluate solvency (debt-to-equity, TIE, current/quick ratio) and cash flow coverage (OCF coverage, cash flow adequacy ratio, revenue cash content). Assess cash flow life cycle stage (startup/growth/mature/decline).

### Step 6: Financial Disguise Detection
**Uses calculator**: `detect_red_flags()`

The calculator automatically detects quantitative red flags:
- Cash flow vs profit divergence
- AR/inventory growth exceeding revenue growth
- Operating index anomalies
- Revenue cash content issues
- Consecutive negative operating cash flow

Supplement with qualitative checks from the framework:
- 9 revenue manipulation techniques (收入操纵九大手法)
- 18 high-risk warning factors
- Accounting quality 5-dimension assessment
- Asset impairment and "big bath" detection

If major red flags are found, recommend stopping.

### Step 7: Management Assessment
Evaluate along three dimensions: compensation (tied to performance?), character (candid about mistakes? related-party transactions?), and operations (ROE/ROA track record, share dilution, follow-through on promises, disclosure quality).

### Step 8: Bear Case Analysis
List all potential negatives — what could go wrong, why sellers are selling, impact of external shocks. If negatives clearly outweigh positives, recommend stopping.

### Step 9: Valuation
**Uses calculator**: `relative_valuation()` + `dcf_valuation()` + `margin_of_safety()`

Apply multiple methods and cross-validate:
- **Relative valuation**: P/S, P/B, P/E, PEG (standard + Lynch refinement), cash yield — compare against peers, market, and the company's own history.
- **Intrinsic value (DCF)**: 10-year free cash flow model with perpetuity value. Run sensitivity analysis with optimistic/neutral/pessimistic assumptions to produce a valuation range, not a single number.

### Step 10: Margin of Safety & Decision
Compare the current price against the valuation range. Apply margin of safety based on company quality (strong moat ~20%, average 30-40%, high risk ~60%). If the current price offers no discount, recommend waiting.

## Output

Generate the analysis report as an Obsidian markdown file. Default path: `Note/金融投资/公司分析流程/{公司名称} 分析.md`

Report structure:

```markdown
---
tags:
  - 公司分析
company: {公司名称}
date: {YYYY-MM-DD}
verdict: {买入/观望/放弃}
---

# {公司名称} 分析

## 基本信息
{公司简介、行业、市值等}

## 1. 业务理解
{商业模式、行业格局、能力圈判断}

## 2. 成长性分析
{多期收入/利润增长率趋势表、可持续增长率、增长来源拆解}

## 3. 收益性分析
### 基础指标
{多期 ROA/ROE/ROIC/FCF 趋势表}
### 杜邦分析
{基础杜邦 + 高级杜邦（经营 vs 融资分解）}
### 营运效率
{应收/存货/应付周转天数、现金转化周期}
### EVA
{经济增加值及解读}

## 4. 竞争优势 / 护城河
{护城河类型及强度评估}

## 5. 财务健康状况
### 偿债能力
{负债率、利息保障、流动比率/速动比率}
### 现金流覆盖
{经营现金流量比率、现金流充裕率、销售收入现金含量}
### 生命周期判断
{基于三大现金流方向判断所处阶段}

## 6. 财务伪装识别
### 量化红旗检测
{脚本自动检测结果}
### 定性检查
{收入操纵手法排查、会计质量评估、资产减值信号}

## 7. 管理层评估
{报酬/性格/运作三维度评价}

## 8. 空头情形
{所有潜在负面因素}

## 9. 估值
### 相对估值
{P/E、P/B、P/S、PEG（标准+林奇改良）、现金收益率}
### DCF 内在价值
{三组假设（乐观/中性/悲观）的估值区间}

## 10. 安全边际与决策
{当前价格 vs 估值区间，安全边际，最终结论}

## 总结
{一段话概括：买入/观望/放弃，核心理由}

> 免责声明：本报告为分析工具输出，不构成投资建议。投资有风险，决策需自行判断。
```

## Guardrails

- Always state assumptions explicitly — especially growth rates and discount rates in DCF.
- Never present a single-point DCF estimate as "the answer". Always show the range.
- If financial data is incomplete, state what's missing and how it affects the analysis rather than guessing.
- Distinguish between facts (from financial statements) and judgments (your interpretation). Use phrases like "数据显示..." vs "我认为..." to make this clear.
- Use the Python calculator for all numerical computations — do not manually calculate financial indicators.
- When extracting data from PDFs, double-check key numbers (revenue, net income, operating cash flow) against multiple locations in the report for consistency.
- This is an analysis tool, not investment advice. Include a disclaimer at the end of the report.
