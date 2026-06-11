#!/usr/bin/env python3
"""Calculate financial metrics for listed-company analysis.

Input: JSON shaped like ../schemas/financial-data.schema.json.
Output: JSON or Markdown tables.
"""

from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any


def num(value: Any) -> float | None:
    if value is None:
        return None
    if isinstance(value, (int, float)):
        if isinstance(value, float) and math.isnan(value):
            return None
        return float(value)
    if isinstance(value, str):
        value = value.strip().replace(",", "")
        if not value:
            return None
        try:
            return float(value)
        except ValueError:
            return None
    return None


def div(a: Any, b: Any) -> float | None:
    a_num = num(a)
    b_num = num(b)
    if a_num is None or b_num in (None, 0):
        return None
    return a_num / b_num


def pct(value: float | None) -> str:
    if value is None:
        return "N/A"
    return f"{value * 100:.1f}%"


def val(value: float | None) -> str:
    if value is None:
        return "N/A"
    if abs(value) >= 100:
        return f"{value:,.1f}"
    return f"{value:,.3f}"


def get_total_debt(period: dict[str, Any]) -> float | None:
    current = num(period.get("interest_bearing_debt_current")) or 0.0
    noncurrent = num(period.get("interest_bearing_debt_noncurrent"))
    if noncurrent is None:
        noncurrent = num(period.get("long_term_debt")) or 0.0
    total = current + noncurrent
    return total if total != 0 else None


def get_cash_like(period: dict[str, Any]) -> float | None:
    cash = num(period.get("cash_and_equivalents")) or 0.0
    sti = num(period.get("short_term_investments")) or 0.0
    total = cash + sti
    return total if total != 0 else None


def effective_tax_rate(period: dict[str, Any]) -> float | None:
    pretax = num(period.get("pretax_income"))
    tax = num(period.get("tax_expense"))
    if pretax is None or pretax <= 0 or tax is None:
        return None
    rate = tax / pretax
    return max(0.0, min(rate, 0.6))


def invested_capital(period: dict[str, Any]) -> float | None:
    assets = num(period.get("total_assets"))
    current_liabilities = num(period.get("current_liabilities"))
    interest_debt_current = num(period.get("interest_bearing_debt_current")) or 0.0
    if assets is None or current_liabilities is None:
        return None
    # Invested capital = total assets - non-interest-bearing current liabilities.
    return assets - (current_liabilities - interest_debt_current)


def nopat(period: dict[str, Any]) -> float | None:
    ebit = num(period.get("ebit"))
    if ebit is None:
        ebit = num(period.get("operating_profit"))
    if ebit is None:
        return None
    tax_rate = effective_tax_rate(period)
    if tax_rate is None:
        tax_rate = 0.25
    return ebit * (1 - tax_rate)


def period_metrics(period: dict[str, Any], previous: dict[str, Any] | None) -> dict[str, Any]:
    revenue = num(period.get("revenue"))
    gross_profit = num(period.get("gross_profit"))
    operating_profit = num(period.get("operating_profit"))
    net_income = num(period.get("net_income"))
    ocf = num(period.get("operating_cash_flow"))
    capex = num(period.get("capital_expenditure"))
    fcf = num(period.get("free_cash_flow"))
    if fcf is None and ocf is not None and capex is not None:
        fcf = ocf - capex

    equity = num(period.get("shareholders_equity"))
    assets = num(period.get("total_assets"))
    current_assets = num(period.get("current_assets"))
    current_liabilities = num(period.get("current_liabilities"))
    inventories = num(period.get("inventories"))
    cogs = num(period.get("cogs"))
    days = num(period.get("days")) or 365.0
    accounts_receivable = num(period.get("accounts_receivable"))
    accounts_payable = num(period.get("accounts_payable"))
    total_debt = get_total_debt(period)
    cash_like = get_cash_like(period)
    ic = invested_capital(period)
    nopat_value = nopat(period)
    wacc = num(period.get("wacc"))

    debt_service = (num(period.get("capital_expenditure")) or 0) + (num(period.get("debt_repayment")) or 0) + (num(period.get("dividends_paid")) or 0)
    ebit = num(period.get("ebit"))
    if ebit is None:
        ebit = operating_profit

    metrics: dict[str, Any] = {
        "label": period.get("label"),
        "revenue_growth": None,
        "gross_margin": div(gross_profit, revenue),
        "operating_margin": div(operating_profit, revenue),
        "net_margin": div(net_income, revenue),
        "free_cash_flow": fcf,
        "fcf_margin": div(fcf, revenue),
        "roa": div(net_income, assets),
        "roe": div(net_income, equity),
        "nopat": nopat_value,
        "invested_capital": ic,
        "roic": div(nopat_value, ic),
        "eva": None,
        "asset_turnover": div(revenue, assets),
        "equity_multiplier": div(assets, equity),
        "current_ratio": div(current_assets, current_liabilities),
        "quick_ratio": div((current_assets - inventories) if current_assets is not None and inventories is not None else None, current_liabilities),
        "debt_to_equity": div(total_debt, equity),
        "net_cash": (cash_like - total_debt) if cash_like is not None and total_debt is not None else cash_like,
        "interest_coverage": div(ebit, period.get("interest_expense")),
        "ocf_to_current_liabilities": div(ocf, current_liabilities),
        "cash_flow_adequacy": div(ocf, debt_service if debt_service else None),
        "revenue_cash_content": div(ocf, revenue),
        "receivable_days": div(days, div(revenue, accounts_receivable)),
        "inventory_days": div(days, div(cogs, inventories)),
        "payable_days": div(days, div(cogs, accounts_payable)),
        "cash_conversion_cycle": None,
    }

    if previous:
        metrics["revenue_growth"] = div(
            (revenue - num(previous.get("revenue"))) if revenue is not None and num(previous.get("revenue")) is not None else None,
            previous.get("revenue"),
        )

    if metrics["receivable_days"] is not None and metrics["inventory_days"] is not None and metrics["payable_days"] is not None:
        metrics["cash_conversion_cycle"] = metrics["receivable_days"] + metrics["inventory_days"] - metrics["payable_days"]

    if nopat_value is not None and ic is not None and wacc is not None:
        metrics["eva"] = nopat_value - ic * wacc

    dividends = num(period.get("dividends_paid"))
    if dividends is not None and net_income not in (None, 0):
        payout = max(0.0, dividends / abs(net_income))
        metrics["sustainable_growth_rate"] = metrics["roe"] * (1 - payout) if metrics["roe"] is not None else None
    else:
        metrics["sustainable_growth_rate"] = metrics["roe"]

    return metrics


def red_flags(periods: list[dict[str, Any]], metrics: list[dict[str, Any]]) -> list[dict[str, str]]:
    flags: list[dict[str, str]] = []
    for idx in range(1, len(periods)):
        current = periods[idx]
        prev = periods[idx - 1]
        label = str(current.get("label", idx))
        rev_growth = metrics[idx].get("revenue_growth")
        ar_growth = div(
            (num(current.get("accounts_receivable")) - num(prev.get("accounts_receivable")))
            if num(current.get("accounts_receivable")) is not None and num(prev.get("accounts_receivable")) is not None
            else None,
            prev.get("accounts_receivable"),
        )
        if ar_growth is not None and rev_growth is not None and ar_growth > rev_growth + 0.1:
            flags.append({
                "period": label,
                "severity": "medium",
                "flag": "Accounts receivable grew materially faster than revenue.",
            })

        net_growth = div(
            (num(current.get("net_income")) - num(prev.get("net_income")))
            if num(current.get("net_income")) is not None and num(prev.get("net_income")) is not None
            else None,
            abs(num(prev.get("net_income"))) if num(prev.get("net_income")) not in (None, 0) else None,
        )
        ocf_growth = div(
            (num(current.get("operating_cash_flow")) - num(prev.get("operating_cash_flow")))
            if num(current.get("operating_cash_flow")) is not None and num(prev.get("operating_cash_flow")) is not None
            else None,
            abs(num(prev.get("operating_cash_flow"))) if num(prev.get("operating_cash_flow")) not in (None, 0) else None,
        )
        if net_growth is not None and ocf_growth is not None and net_growth > 0.1 and ocf_growth < -0.1:
            flags.append({
                "period": label,
                "severity": "high",
                "flag": "Net income improved while operating cash flow declined materially.",
            })

        margin = metrics[idx].get("operating_margin")
        prev_margin = metrics[idx - 1].get("operating_margin")
        if margin is not None and prev_margin is not None and margin < prev_margin - 0.1:
            flags.append({
                "period": label,
                "severity": "medium",
                "flag": "Operating margin deteriorated by more than 10 percentage points.",
            })

    for idx, current in enumerate(periods):
        label = str(current.get("label", idx))
        if (num(current.get("net_income")) or 0) > 0 and (num(current.get("operating_cash_flow")) or 0) < 0:
            flags.append({
                "period": label,
                "severity": "high",
                "flag": "Reported profit is positive but operating cash flow is negative.",
            })
    return flags


def dcf_value(scenario: dict[str, Any], default_dcf: dict[str, Any]) -> dict[str, Any]:
    base_fcf = num(scenario.get("base_fcf"))
    growth_rates = scenario.get("growth_rates") or []
    discount_rate = num(scenario.get("discount_rate")) or num(default_dcf.get("discount_rate"))
    terminal_growth_rate = num(scenario.get("terminal_growth_rate")) or num(default_dcf.get("terminal_growth_rate"))
    net_cash = num(scenario.get("net_cash"))
    if net_cash is None:
        net_cash = num(default_dcf.get("net_cash")) or 0.0
    shares = num(scenario.get("shares_outstanding")) or num(default_dcf.get("shares_outstanding"))

    if base_fcf is None or not growth_rates or discount_rate is None or terminal_growth_rate is None:
        return {"name": scenario.get("name", "scenario"), "error": "Missing DCF inputs"}
    if discount_rate <= terminal_growth_rate:
        return {"name": scenario.get("name", "scenario"), "error": "Discount rate must exceed terminal growth rate"}

    fcf = base_fcf
    pv_sum = 0.0
    forecasts: list[dict[str, float]] = []
    for year, growth in enumerate(growth_rates, start=1):
        growth_num = num(growth) or 0.0
        fcf *= 1 + growth_num
        pv = fcf / ((1 + discount_rate) ** year)
        pv_sum += pv
        forecasts.append({"year": year, "growth_rate": growth_num, "fcf": fcf, "present_value": pv})

    terminal_value = fcf * (1 + terminal_growth_rate) / (discount_rate - terminal_growth_rate)
    terminal_present_value = terminal_value / ((1 + discount_rate) ** len(growth_rates))
    equity_value = pv_sum + terminal_present_value + net_cash
    per_share = equity_value / shares if shares not in (None, 0) else None
    return {
        "name": scenario.get("name", "scenario"),
        "discount_rate": discount_rate,
        "terminal_growth_rate": terminal_growth_rate,
        "base_fcf": base_fcf,
        "forecast_years": forecasts,
        "present_value_sum": pv_sum,
        "terminal_value": terminal_value,
        "terminal_present_value": terminal_present_value,
        "net_cash": net_cash,
        "equity_value": equity_value,
        "shares_outstanding": shares,
        "per_share_value": per_share,
    }


def calculate(data: dict[str, Any]) -> dict[str, Any]:
    periods = data.get("periods", [])
    metrics = [period_metrics(period, periods[idx - 1] if idx > 0 else None) for idx, period in enumerate(periods)]
    dcf_cfg = (data.get("valuation") or {}).get("dcf") or {}
    dcf_results = [dcf_value(scenario, dcf_cfg) for scenario in dcf_cfg.get("scenarios", [])]
    return {
        "company": data.get("company", {}),
        "presentation": data.get("presentation", {}),
        "exchange_rates": data.get("exchange_rates", []),
        "sources": data.get("sources", []),
        "metrics": metrics,
        "red_flags": red_flags(periods, metrics),
        "dcf": dcf_results,
    }


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    out = ["| " + " | ".join(headers) + " |", "| " + " | ".join(["---"] * len(headers)) + " |"]
    out.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(out)


def to_markdown(result: dict[str, Any]) -> str:
    company = result.get("company", {})
    lines = [f"# Financial Calculations: {company.get('name', '')}".rstrip(), ""]
    source_unit = company.get("unit") or company.get("currency") or "original reporting currency"
    presentation = result.get("presentation", {})
    display_currency = presentation.get("display_currency")
    if display_currency:
        lines.extend([
            f"Calculation values are in source unit: {source_unit}. Final report display currency: {display_currency}.",
            "",
        ])
    else:
        lines.extend([f"Calculation values are in source unit: {source_unit}.", ""])

    metric_rows = []
    for item in result.get("metrics", []):
        metric_rows.append([
            str(item.get("label", "")),
            pct(item.get("revenue_growth")),
            pct(item.get("gross_margin")),
            pct(item.get("operating_margin")),
            pct(item.get("net_margin")),
            pct(item.get("roe")),
            pct(item.get("roic")),
            pct(item.get("fcf_margin")),
            val(item.get("free_cash_flow")),
            val(item.get("net_cash")),
        ])
    lines.append(markdown_table(
        [
            "Period",
            "Revenue growth",
            "Gross margin",
            "Operating margin",
            "Net margin",
            "ROE（净资产收益率）",
            "ROIC（投入资本回报率）",
            "FCF（自由现金流）率",
            "FCF（自由现金流）",
            "Net cash",
        ],
        metric_rows,
    ))

    health_rows = []
    for item in result.get("metrics", []):
        health_rows.append([
            str(item.get("label", "")),
            val(item.get("current_ratio")),
            val(item.get("quick_ratio")),
            val(item.get("debt_to_equity")),
            val(item.get("interest_coverage")),
            pct(item.get("ocf_to_current_liabilities")),
            val(item.get("cash_conversion_cycle")),
            val(item.get("eva")),
        ])
    lines.extend(["", markdown_table(
        [
            "Period",
            "Current ratio",
            "Quick ratio",
            "Debt/equity",
            "Interest coverage",
            "OCF（经营现金流）/流动负债",
            "CCC（现金周转天数）",
            "EVA（经济增加值）",
        ],
        health_rows,
    )])

    flags = result.get("red_flags", [])
    lines.extend(["", "## Red Flags"])
    if flags:
        lines.append(markdown_table(["Period", "Severity", "Flag"], [[f["period"], f["severity"], f["flag"]] for f in flags]))
    else:
        lines.append("No automatic red flags detected from the provided data.")

    dcf_results = result.get("dcf", [])
    if dcf_results:
        rows = []
        for item in dcf_results:
            if "error" in item:
                rows.append([str(item.get("name")), "N/A", "N/A", str(item.get("error"))])
            else:
                rows.append([
                    str(item.get("name")),
                    val(item.get("equity_value")),
                    val(item.get("per_share_value")),
                    f"r={pct(item.get('discount_rate'))}, g={pct(item.get('terminal_growth_rate'))}",
                ])
        lines.extend(["", "## DCF（现金流折现）", markdown_table(["Scenario", "Equity value", "Per-share value", "Assumptions"], rows)])
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    args = parser.parse_args()

    data = json.loads(args.input.read_text(encoding="utf-8"))
    result = calculate(data)
    if args.format == "markdown":
        print(to_markdown(result))
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
