#!/usr/bin/env python3
"""
公司财务分析计算器

用法：
1. LLM 从财报 PDF 中提取原始数据，填入 CompanyFinancials 数据结构
2. 调用各分析函数计算指标
3. 输出结果用于分析报告

支持单期和多期（趋势）分析。
"""

import json
import sys
from dataclasses import dataclass, field, asdict
from typing import Optional


# ============================================================
# 数据结构定义
# ============================================================

@dataclass
class PeriodData:
    """单期财务数据（从财报中提取的原始数据）"""

    period: str  # 期间标识，如 "2024" 或 "2024H1"

    # --- 利润表 ---
    revenue: float = 0                    # 营业收入/销售收入
    cost_of_revenue: float = 0            # 营业成本/销售成本
    gross_profit: float = 0               # 毛利润
    operating_income: float = 0           # 营业利润
    net_income: float = 0                 # 净利润（归母）
    interest_expense: float = 0           # 利息费用/财务费用
    ebit: float = 0                       # 息税前利润
    non_recurring_items: float = 0        # 非经常性损益

    # --- 资产负债表 ---
    total_assets: float = 0               # 总资产
    total_equity: float = 0               # 股东权益/所有者权益（归母）
    total_liabilities: float = 0          # 总负债
    current_assets: float = 0             # 流动资产
    current_liabilities: float = 0        # 流动负债
    cash_and_equivalents: float = 0       # 现金及等价物
    short_term_debt: float = 0            # 短期有息负债（短期借款 + 一年内到期长期负债）
    long_term_debt: float = 0             # 长期有息负债
    accounts_receivable: float = 0        # 应收账款
    inventory: float = 0                  # 存货
    accounts_payable: float = 0           # 应付账款
    goodwill: float = 0                   # 商誉
    intangible_assets: float = 0          # 无形资产

    # --- 现金流量表 ---
    operating_cashflow: float = 0         # 经营活动现金流净额
    capex: float = 0                      # 资本支出（购建固定/无形/长期资产支付的现金，取正数）
    investing_cashflow: float = 0         # 投资活动现金流净额
    financing_cashflow: float = 0         # 筹资活动现金流净额
    debt_repayment: float = 0             # 偿还债务支付的现金
    dividends_paid: float = 0             # 分配股利支付的现金
    depreciation_amortization: float = 0  # 折旧与摊销

    # --- 其他 ---
    shares_outstanding: float = 0         # 总股本（股）
    effective_tax_rate: float = 0.25      # 有效税率
    dividend_payout_ratio: float = 0      # 股利支付率
    eps: float = 0                        # 每股收益


# ============================================================
# Step 2: 成长性分析
# ============================================================

def analyze_growth(periods: list[PeriodData]) -> dict:
    """多期成长性分析"""
    if len(periods) < 2:
        return {"error": "需要至少两期数据"}

    results = []
    for i in range(1, len(periods)):
        prev, curr = periods[i - 1], periods[i]
        rev_growth = _pct_change(prev.revenue, curr.revenue)
        ni_growth = _pct_change(prev.net_income, curr.net_income)
        gp_growth = _pct_change(prev.gross_profit, curr.gross_profit)
        op_growth = _pct_change(prev.operating_income, curr.operating_income)

        # 可持续增长率
        roe = curr.net_income / curr.total_equity if curr.total_equity else None
        sustainable_growth = roe * (1 - curr.dividend_payout_ratio) if roe else None

        results.append({
            "period": f"{prev.period} → {curr.period}",
            "revenue_growth": _fmt_pct(rev_growth),
            "net_income_growth": _fmt_pct(ni_growth),
            "gross_profit_growth": _fmt_pct(gp_growth),
            "operating_income_growth": _fmt_pct(op_growth),
            "sustainable_growth_rate": _fmt_pct(sustainable_growth),
            "red_flag_earnings_gt_revenue": ni_growth is not None and rev_growth is not None and ni_growth > rev_growth,
        })

    return {"growth_analysis": results}


# ============================================================
# Step 3: 收益性分析
# ============================================================

def analyze_profitability(data: PeriodData) -> dict:
    """单期收益性指标计算"""

    # 基础指标
    gross_margin = data.gross_profit / data.revenue if data.revenue else None
    net_margin = data.net_income / data.revenue if data.revenue else None
    roa = data.net_income / data.total_assets if data.total_assets else None
    roe = data.net_income / data.total_equity if data.total_equity else None

    # ROIC
    nopat = data.operating_income * (1 - data.effective_tax_rate)
    invested_capital = data.total_assets - (data.current_liabilities - data.short_term_debt)
    roic = nopat / invested_capital if invested_capital else None

    # FCF
    fcf = data.operating_cashflow - data.capex
    fcf_margin = fcf / data.revenue if data.revenue else None

    # 基础杜邦
    asset_turnover = data.revenue / data.total_assets if data.total_assets else None
    equity_multiplier = data.total_assets / data.total_equity if data.total_equity else None
    dupont_check = (net_margin or 0) * (asset_turnover or 0) * (equity_multiplier or 0)

    # 高级杜邦（区分经营与融资）
    net_assets = data.total_assets - data.total_liabilities + data.long_term_debt + data.short_term_debt  # 净经营资产近似
    net_debt = data.long_term_debt + data.short_term_debt - data.cash_and_equivalents
    operating_roa = nopat / net_assets if net_assets else None
    after_tax_interest_rate = (data.interest_expense * (1 - data.effective_tax_rate)) / net_debt if net_debt and net_debt > 0 else None
    spread = (operating_roa - after_tax_interest_rate) if operating_roa is not None and after_tax_interest_rate is not None else None
    net_financial_leverage = net_debt / data.total_equity if data.total_equity and net_debt else None
    leverage_effect = spread * net_financial_leverage if spread is not None and net_financial_leverage is not None else None

    # 营运效率
    ar_turnover_days = 365 / (data.revenue / data.accounts_receivable) if data.accounts_receivable and data.revenue else None
    inv_turnover_days = 365 / (data.cost_of_revenue / data.inventory) if data.inventory and data.cost_of_revenue else None
    ap_turnover_days = 365 / (data.cost_of_revenue / data.accounts_payable) if data.accounts_payable and data.cost_of_revenue else None
    cash_conversion_cycle = None
    if ar_turnover_days is not None and inv_turnover_days is not None and ap_turnover_days is not None:
        cash_conversion_cycle = ar_turnover_days + inv_turnover_days - ap_turnover_days

    # 营业营运资本
    operating_working_capital = (data.current_assets - data.cash_and_equivalents) - (data.current_liabilities - data.short_term_debt)
    owc_to_revenue = operating_working_capital / data.revenue if data.revenue else None

    # EVA
    wacc = 0.10  # 默认 10%，实际使用时应根据公司情况调整
    eva = nopat - invested_capital * wacc if invested_capital else None

    return {
        "period": data.period,
        "gross_margin": _fmt_pct(gross_margin),
        "net_margin": _fmt_pct(net_margin),
        "ROA": _fmt_pct(roa),
        "ROE": _fmt_pct(roe),
        "ROIC": _fmt_pct(roic),
        "NOPAT": _fmt_num(nopat),
        "invested_capital": _fmt_num(invested_capital),
        "FCF": _fmt_num(fcf),
        "FCF_margin": _fmt_pct(fcf_margin),
        "dupont": {
            "net_margin": _fmt_pct(net_margin),
            "asset_turnover": _fmt_ratio(asset_turnover),
            "equity_multiplier": _fmt_ratio(equity_multiplier),
            "dupont_ROE_check": _fmt_pct(dupont_check),
        },
        "advanced_dupont": {
            "operating_ROA": _fmt_pct(operating_roa),
            "after_tax_interest_rate": _fmt_pct(after_tax_interest_rate),
            "spread": _fmt_pct(spread),
            "net_financial_leverage": _fmt_ratio(net_financial_leverage),
            "leverage_effect": _fmt_pct(leverage_effect),
            "note": "spread > 0 说明借债创造价值" if spread and spread > 0 else "spread <= 0 说明借债可能毁灭价值" if spread is not None else None,
        },
        "efficiency": {
            "AR_turnover_days": _fmt_ratio(ar_turnover_days),
            "inventory_turnover_days": _fmt_ratio(inv_turnover_days),
            "AP_turnover_days": _fmt_ratio(ap_turnover_days),
            "cash_conversion_cycle": _fmt_ratio(cash_conversion_cycle),
            "operating_working_capital": _fmt_num(operating_working_capital),
            "OWC_to_revenue": _fmt_pct(owc_to_revenue),
        },
        "EVA": _fmt_num(eva),
        "EVA_note": "EVA > 0 创造超额价值" if eva and eva > 0 else "EVA <= 0 毁灭股东价值" if eva is not None else None,
    }


# ============================================================
# Step 5: 财务健康状况
# ============================================================

def analyze_financial_health(data: PeriodData) -> dict:
    """单期财务健康指标"""

    debt_to_equity = data.long_term_debt / data.total_equity if data.total_equity else None
    total_debt_to_equity = (data.long_term_debt + data.short_term_debt) / data.total_equity if data.total_equity else None
    tie = data.ebit / data.interest_expense if data.interest_expense else None
    current_ratio = data.current_assets / data.current_liabilities if data.current_liabilities else None
    quick_ratio = (data.current_assets - data.inventory) / data.current_liabilities if data.current_liabilities else None

    # 现金流覆盖
    ocf_to_cl = data.operating_cashflow / data.current_liabilities if data.current_liabilities else None
    total_obligations = data.capex + data.debt_repayment + data.dividends_paid
    cashflow_adequacy = data.operating_cashflow / total_obligations if total_obligations else None
    revenue_cash_content = data.operating_cashflow / data.revenue if data.revenue else None

    # 净现金/净债务
    net_cash = data.cash_and_equivalents - data.long_term_debt - data.short_term_debt

    return {
        "period": data.period,
        "solvency": {
            "debt_to_equity_LT": _fmt_ratio(debt_to_equity),
            "debt_to_equity_total": _fmt_ratio(total_debt_to_equity),
            "interest_coverage_TIE": _fmt_ratio(tie),
            "current_ratio": _fmt_ratio(current_ratio),
            "quick_ratio": _fmt_ratio(quick_ratio),
            "current_ratio_status": _judge(current_ratio, 1.5, "≥1.5 安全", "<1.5 偏低"),
            "quick_ratio_status": _judge(quick_ratio, 1.0, "≥1.0 安全", "<1.0 偏低"),
        },
        "cashflow_coverage": {
            "OCF_to_current_liabilities": _fmt_ratio(ocf_to_cl),
            "cashflow_adequacy_ratio": _fmt_ratio(cashflow_adequacy),
            "adequacy_status": _judge(cashflow_adequacy, 1.0, ">1 安全", "≤1 危险") if cashflow_adequacy else None,
            "revenue_cash_content": _fmt_pct(revenue_cash_content),
        },
        "net_cash_position": _fmt_num(net_cash),
        "net_cash_note": "净现金" if net_cash and net_cash > 0 else "净负债",
    }


# ============================================================
# Step 6: 财务伪装识别（量化红旗检测）
# ============================================================

def detect_red_flags(periods: list[PeriodData]) -> dict:
    """基于多期数据的量化红旗检测"""
    if len(periods) < 2:
        return {"error": "需要至少两期数据"}

    flags = []

    for i in range(1, len(periods)):
        prev, curr = periods[i - 1], periods[i]
        period_label = f"{prev.period} → {curr.period}"

        # 1. 现金流 vs 利润背离
        ni_growth = _pct_change(prev.net_income, curr.net_income)
        ocf_growth = _pct_change(prev.operating_cashflow, curr.operating_cashflow)
        if ni_growth is not None and ocf_growth is not None:
            if ni_growth > 0 and ocf_growth < 0:
                flags.append({
                    "period": period_label,
                    "flag": "现金流衰退",
                    "severity": "HIGH",
                    "detail": f"净利润增长 {_fmt_pct(ni_growth)}，但经营现金流下降 {_fmt_pct(ocf_growth)}",
                })

        # 2. 应收账款增长 > 收入增长
        ar_growth = _pct_change(prev.accounts_receivable, curr.accounts_receivable)
        rev_growth = _pct_change(prev.revenue, curr.revenue)
        if ar_growth is not None and rev_growth is not None:
            if ar_growth > rev_growth + 0.05:  # 超过收入增速5个百分点以上
                flags.append({
                    "period": period_label,
                    "flag": "应收账款增速异常",
                    "severity": "HIGH",
                    "detail": f"应收增长 {_fmt_pct(ar_growth)} > 收入增长 {_fmt_pct(rev_growth)}",
                })

        # 3. 存货增长 > 收入增长
        inv_growth = _pct_change(prev.inventory, curr.inventory)
        if inv_growth is not None and rev_growth is not None:
            if inv_growth > rev_growth + 0.05:
                flags.append({
                    "period": period_label,
                    "flag": "存货增速异常",
                    "severity": "MEDIUM",
                    "detail": f"存货增长 {_fmt_pct(inv_growth)} > 收入增长 {_fmt_pct(rev_growth)}",
                })

        # 4. 盈利增长持续超过收入增长
        if ni_growth is not None and rev_growth is not None:
            if ni_growth > rev_growth + 0.1:  # 净利润增速高出收入10个百分点以上
                flags.append({
                    "period": period_label,
                    "flag": "盈利增长显著超过收入增长",
                    "severity": "MEDIUM",
                    "detail": f"净利润增长 {_fmt_pct(ni_growth)} >> 收入增长 {_fmt_pct(rev_growth)}，可能是人造增长",
                })

        # 5. 经营指数偏离
        if curr.operating_income and curr.operating_cashflow:
            operating_index = curr.operating_cashflow / curr.operating_income
            if operating_index < 0.5:
                flags.append({
                    "period": curr.period,
                    "flag": "经营指数过低",
                    "severity": "HIGH",
                    "detail": f"经营指数 = {operating_index:.2f}（经营现金流/经营利润），远低于1，盈利质量存疑",
                })

        # 6. 销售收入现金含量偏低
        if curr.revenue and curr.operating_cashflow:
            cash_content = curr.operating_cashflow / curr.revenue
            if cash_content < 0.05:
                flags.append({
                    "period": curr.period,
                    "flag": "销售收入现金含量极低",
                    "severity": "MEDIUM",
                    "detail": f"经营现金流/收入 = {_fmt_pct(cash_content)}，收入变现能力差",
                })

    # 连续三年经营现金流入不敷出
    negative_ocf_years = [p.period for p in periods if p.operating_cashflow < 0]
    if len(negative_ocf_years) >= 3:
        flags.append({
            "period": ", ".join(negative_ocf_years),
            "flag": "连续多年经营现金流为负",
            "severity": "CRITICAL",
            "detail": f"经营现金流连续 {len(negative_ocf_years)} 期为负，严重警告",
        })

    return {
        "red_flags": flags,
        "total_flags": len(flags),
        "critical": len([f for f in flags if f["severity"] == "CRITICAL"]),
        "high": len([f for f in flags if f["severity"] == "HIGH"]),
        "medium": len([f for f in flags if f["severity"] == "MEDIUM"]),
    }


# ============================================================
# Step 9: 估值
# ============================================================

def dcf_valuation(
    fcf_base: float,
    growth_rates: dict[str, float],  # {"optimistic": 0.15, "neutral": 0.10, "pessimistic": 0.05}
    discount_rate: float,
    terminal_growth: float,
    shares: float,
    projection_years: int = 10,
) -> dict:
    """DCF 估值（三组假设）"""
    results = {}

    for scenario, growth in growth_rates.items():
        yearly = []
        fcf = fcf_base
        total_pv = 0

        for year in range(1, projection_years + 1):
            fcf = fcf * (1 + growth)
            pv = fcf / (1 + discount_rate) ** year
            total_pv += pv
            yearly.append({
                "year": year,
                "FCF": round(fcf, 2),
                "PV": round(pv, 2),
            })

        # 永续价值
        terminal_value = fcf * (1 + terminal_growth) / (discount_rate - terminal_growth)
        terminal_pv = terminal_value / (1 + discount_rate) ** projection_years

        equity_value = total_pv + terminal_pv
        per_share = equity_value / shares if shares else 0

        results[scenario] = {
            "growth_rate": _fmt_pct(growth),
            "yearly_projections": yearly,
            "sum_of_discounted_FCF": round(total_pv, 2),
            "terminal_value": round(terminal_value, 2),
            "terminal_value_discounted": round(terminal_pv, 2),
            "total_equity_value": round(equity_value, 2),
            "per_share_value": round(per_share, 2),
        }

    return {
        "dcf_valuation": results,
        "assumptions": {
            "base_FCF": fcf_base,
            "discount_rate": _fmt_pct(discount_rate),
            "terminal_growth": _fmt_pct(terminal_growth),
            "projection_years": projection_years,
            "shares_outstanding": shares,
        },
    }


def relative_valuation(
    data: PeriodData,
    market_cap: float,
    current_price: float,
    eps_growth_rate: float,
    dividend_yield: float = 0,
) -> dict:
    """相对估值指标计算"""
    fcf = data.operating_cashflow - data.capex
    ev = market_cap + data.long_term_debt + data.short_term_debt - data.cash_and_equivalents

    pe = market_cap / data.net_income if data.net_income and data.net_income > 0 else None
    pb = market_cap / data.total_equity if data.total_equity else None
    ps = market_cap / data.revenue if data.revenue else None
    peg = pe / (eps_growth_rate * 100) if pe and eps_growth_rate else None

    # 彼得林奇改良 PEG
    lynch_peg = (eps_growth_rate * 100 + dividend_yield * 100) / pe if pe and pe > 0 else None

    cash_yield = fcf / ev if ev and ev > 0 else None

    return {
        "period": data.period,
        "market_cap": _fmt_num(market_cap),
        "EV": _fmt_num(ev),
        "P/E": _fmt_ratio(pe),
        "P/B": _fmt_ratio(pb),
        "P/S": _fmt_ratio(ps),
        "PEG": _fmt_ratio(peg),
        "lynch_PEG": _fmt_ratio(lynch_peg),
        "lynch_PEG_note": _lynch_peg_verdict(lynch_peg),
        "cash_yield": _fmt_pct(cash_yield),
        "FCF": _fmt_num(fcf),
    }


def margin_of_safety(
    intrinsic_value: float,
    current_price: float,
    company_quality: str = "average",
    net_cash_per_share: float = 0.0,
    core_biz_value_per_share: float = 0.0,
) -> dict:
    """安全边际计算（双底法）

    Args:
        intrinsic_value: DCF估值区间中位数（每股）
        current_price: 当前股价
        company_quality: 护城河状态，可选值：
            "wide_stable"   → 宽且稳定（15-20%）
            "moderate"      → 中等或受压（25-35%）
            "narrow"        → 窄且收缩（40-50%）
            "none"          → 无护城河（50-60%）
            以下为旧版兼容值：
            "strong_moat"   → 映射到 wide_stable
            "average"       → 映射到 moderate
            "high_risk"     → 映射到 none
        net_cash_per_share: 每股净现金（现金+短期理财-有息负债）/ 总股本
        core_biz_value_per_share: 核心盈利业务保守估值（每股），通常 = 核心业务收入 × 保守P/S / 总股本
    """
    # 安全边际分级（取区间中位数）
    margins = {
        "wide_stable": 0.175,
        "moderate": 0.30,
        "narrow": 0.45,
        "none": 0.55,
        # 旧版兼容
        "strong_moat": 0.175,
        "average": 0.30,
        "high_risk": 0.55,
    }
    margin = margins.get(company_quality, 0.30)

    # 盈利底
    earnings_floor = intrinsic_value * (1 - margin)

    # 资产底（仅当净现金占股价比 > 20% 时触发）
    asset_floor = net_cash_per_share + core_biz_value_per_share
    use_asset_floor = (
        asset_floor > 0
        and current_price > 0
        and net_cash_per_share / current_price > 0.20
    )

    if use_asset_floor:
        buy_price = max(earnings_floor, asset_floor)
        method_used = "资产底" if asset_floor >= earnings_floor else "盈利底"
    else:
        buy_price = earnings_floor
        method_used = "盈利底"

    current_discount = 1 - current_price / intrinsic_value if intrinsic_value else None

    return {
        "intrinsic_value": round(intrinsic_value, 2),
        "current_price": round(current_price, 2),
        "moat_category": company_quality,
        "required_margin": _fmt_pct(margin),
        "earnings_floor": round(earnings_floor, 2),
        "asset_floor": round(asset_floor, 2) if use_asset_floor else "N/A（净现金占比≤25%，未触发）",
        "buy_price": round(buy_price, 2),
        "method_used": method_used,
        "current_discount": _fmt_pct(current_discount),
        "verdict": "可买入" if current_discount and current_discount >= margin else "等待更低价格",
    }


# ============================================================
# 多期趋势汇总
# ============================================================

def multi_period_summary(periods: list[PeriodData]) -> dict:
    """多期财务数据趋势汇总表"""
    summary = []
    for p in periods:
        fcf = p.operating_cashflow - p.capex
        roe = p.net_income / p.total_equity if p.total_equity else None
        roa = p.net_income / p.total_assets if p.total_assets else None
        gross_margin = p.gross_profit / p.revenue if p.revenue else None
        net_margin = p.net_income / p.revenue if p.revenue else None

        summary.append({
            "period": p.period,
            "revenue": _fmt_num(p.revenue),
            "gross_profit": _fmt_num(p.gross_profit),
            "gross_margin": _fmt_pct(gross_margin),
            "operating_income": _fmt_num(p.operating_income),
            "net_income": _fmt_num(p.net_income),
            "net_margin": _fmt_pct(net_margin),
            "ROA": _fmt_pct(roa),
            "ROE": _fmt_pct(roe),
            "operating_cashflow": _fmt_num(p.operating_cashflow),
            "FCF": _fmt_num(fcf),
            "total_assets": _fmt_num(p.total_assets),
            "total_equity": _fmt_num(p.total_equity),
            "total_debt": _fmt_num(p.long_term_debt + p.short_term_debt),
            "cash": _fmt_num(p.cash_and_equivalents),
        })

    return {"trend_summary": summary}


# ============================================================
# 辅助函数
# ============================================================

def _pct_change(old: float, new: float) -> Optional[float]:
    if old and old != 0:
        return (new - old) / abs(old)
    return None

def _fmt_pct(value: Optional[float]) -> Optional[str]:
    if value is None:
        return None
    return f"{value * 100:.2f}%"

def _fmt_ratio(value: Optional[float]) -> Optional[str]:
    if value is None:
        return None
    return f"{value:.2f}"

def _fmt_num(value: Optional[float]) -> Optional[str]:
    if value is None:
        return None
    if abs(value) >= 1e8:
        return f"{value / 1e8:.2f} 亿"
    elif abs(value) >= 1e4:
        return f"{value / 1e4:.2f} 万"
    return f"{value:.2f}"

def _judge(value: Optional[float], threshold: float, pass_msg: str, fail_msg: str) -> Optional[str]:
    if value is None:
        return None
    return pass_msg if value >= threshold else fail_msg

def _lynch_peg_verdict(value: Optional[float]) -> Optional[str]:
    if value is None:
        return None
    if value >= 2.0:
        return "非常值得投资 (≥2.0)"
    elif value >= 1.5:
        return "还不错 (≈1.5)"
    elif value >= 1.0:
        return "一般"
    else:
        return "股票比较差 (<1.0)"


# ============================================================
# CLI 入口：从 JSON 文件读取数据并运行全部分析
# ============================================================

def run_full_analysis(periods: list[PeriodData], market_cap: float = 0, current_price: float = 0, eps_growth_rate: float = 0, dividend_yield: float = 0) -> dict:
    """运行完整分析流程，返回所有结果"""
    results = {}

    # 多期趋势
    results["trend"] = multi_period_summary(periods)

    # 成长性（需要至少2期）
    if len(periods) >= 2:
        results["growth"] = analyze_growth(periods)

    # 收益性（每期）
    results["profitability"] = [analyze_profitability(p) for p in periods]

    # 财务健康（每期）
    results["financial_health"] = [analyze_financial_health(p) for p in periods]

    # 红旗检测
    if len(periods) >= 2:
        results["red_flags"] = detect_red_flags(periods)

    # 估值（如果有市场数据）
    latest = periods[-1]
    if market_cap > 0:
        results["relative_valuation"] = relative_valuation(
            latest, market_cap, current_price, eps_growth_rate, dividend_yield
        )

    # DCF（使用最新期FCF作为基础）
    fcf_base = latest.operating_cashflow - latest.capex
    if fcf_base > 0 and latest.shares_outstanding > 0:
        results["dcf"] = dcf_valuation(
            fcf_base=fcf_base,
            growth_rates={"optimistic": 0.15, "neutral": 0.10, "pessimistic": 0.05},
            discount_rate=0.10,
            terminal_growth=0.03,
            shares=latest.shares_outstanding,
        )

    return results


def main():
    """CLI 入口：python financial_calculator.py <data.json>"""
    if len(sys.argv) < 2:
        print("用法: python financial_calculator.py <data.json>")
        print()
        print("data.json 格式示例:")
        example = {
            "periods": [
                {
                    "period": "2023",
                    "revenue": 1000000,
                    "cost_of_revenue": 600000,
                    "gross_profit": 400000,
                    "operating_income": 200000,
                    "net_income": 150000,
                    "total_assets": 2000000,
                    "total_equity": 1000000,
                    "current_assets": 800000,
                    "current_liabilities": 400000,
                    "cash_and_equivalents": 300000,
                    "operating_cashflow": 250000,
                    "capex": 50000,
                    "shares_outstanding": 100000,
                    "...": "更多字段见 PeriodData 定义",
                }
            ],
            "market_cap": 3000000,
            "current_price": 30.0,
            "eps_growth_rate": 0.15,
            "dividend_yield": 0.02,
        }
        print(json.dumps(example, ensure_ascii=False, indent=2))
        sys.exit(0)

    with open(sys.argv[1], "r", encoding="utf-8") as f:
        raw = json.load(f)

    periods = [PeriodData(**p) for p in raw["periods"]]
    results = run_full_analysis(
        periods,
        market_cap=raw.get("market_cap", 0),
        current_price=raw.get("current_price", 0),
        eps_growth_rate=raw.get("eps_growth_rate", 0),
        dividend_yield=raw.get("dividend_yield", 0),
    )

    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
