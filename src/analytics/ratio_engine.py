from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_assets,
    return_on_capital_employed,
    debt_to_equity,
    interest_coverage_ratio,
    asset_turnover,
)

from src.analytics.cashflow_kpis import (
    free_cash_flow,
    cfo_quality_score,
    capex_intensity,
    fcf_conversion,
    capital_allocation_pattern,
)
from src.analytics.cagr import calculate_cagr
import sqlite3
def calculate_ratios(pl, bs, cf):
    """
    Calculate all financial ratios for one company-year.
    """

    ratios = {}

    # ---------- Profitability ----------
    ratios["net_profit_margin_pct"] = net_profit_margin(
        pl["net_profit"],
        pl["sales"],
    )

    ratios["operating_profit_margin_pct"] = operating_profit_margin(
        pl["operating_profit"],
        pl["sales"],
    )

    ratios["return_on_equity_pct"] = return_on_equity(
        pl["net_profit"],
        bs["equity_capital"],
        bs["reserves"],
    )

    ratios["return_on_assets_pct"] = return_on_assets(
        pl["net_profit"],
        bs["total_assets"],
    )

    ratios["return_on_capital_employed_pct"] = (
        return_on_capital_employed(
            pl["operating_profit"],
            pl["other_income"],
            bs["equity_capital"],
            bs["reserves"],
            bs["borrowings"],
        )
    )

    # ---------- Leverage ----------
    ratios["debt_to_equity"] = debt_to_equity(
        bs["borrowings"],
        bs["equity_capital"],
        bs["reserves"],
    )

    ratios["interest_coverage"] = interest_coverage_ratio(
        pl["operating_profit"],
        pl["other_income"],
        pl["interest"],
    )

    ratios["asset_turnover"] = asset_turnover(
        pl["sales"],
        bs["total_assets"],
    )
   

   # ---------- Cashflow ----------

    print(cf)
    print(cf["operating_activity"])
    print(cf["investing_activity"])

    ratios["free_cash_flow_cr"] = free_cash_flow(
        cf["operating_activity"],
        cf["investing_activity"],
    )

    return ratios