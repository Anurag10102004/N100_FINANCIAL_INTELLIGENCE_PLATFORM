"""
Profitability Ratio Functions
Sprint 2 - Day 08
"""

def net_profit_margin(net_profit, sales):
    """
    Net Profit Margin = (Net Profit / Sales) * 100
    """
    if sales == 0:
        return None
    return round((net_profit / sales) * 100, 2)


def operating_profit_margin(operating_profit, sales):
    """
    Operating Profit Margin = (Operating Profit / Sales) * 100
    """
    if sales == 0:
        return None
    return round((operating_profit / sales) * 100, 2)


def return_on_equity(net_profit, equity_capital, reserves):
    """
    ROE = Net Profit / (Equity Capital + Reserves) * 100
    """
    equity = equity_capital + reserves

    if equity <= 0:
        return None

    return round((net_profit / equity) * 100, 2)


def return_on_assets(net_profit, total_assets):
    """
    ROA = Net Profit / Total Assets * 100
    """
    if total_assets == 0:
        return None

    return round((net_profit / total_assets) * 100, 2)


def return_on_capital_employed(
    operating_profit,
    other_income,
    equity_capital,
    reserves,
    borrowings,
):
    """
    ROCE = EBIT / Capital Employed * 100
    EBIT = Operating Profit + Other Income
    """

    capital = equity_capital + reserves + borrowings

    if capital <= 0:
        return None

    ebit = operating_profit + other_income

    return round((ebit / capital) * 100, 2)

def debt_to_equity(borrowings, equity_capital, reserves):
    """
    Debt to Equity Ratio
    """
    equity = equity_capital + reserves

    if borrowings == 0:
        return 0

    if equity <= 0:
        return None

    return round(borrowings / equity, 2)


def high_leverage_flag(de_ratio, is_financial=False):
    """
    High leverage if D/E > 5 and company is not Financial.
    """
    if is_financial:
        return False

    return de_ratio is not None and de_ratio > 5


def interest_coverage_ratio(operating_profit, other_income, interest):
    """
    Interest Coverage Ratio
    """
    if interest == 0:
        return None

    ebit = operating_profit + other_income
    return round(ebit / interest, 2)


def icr_label(interest):
    """
    Label for debt-free companies.
    """
    if interest == 0:
        return "Debt Free"
    return None


def net_debt(borrowings, investments):
    """
    Net Debt
    """
    return borrowings - investments


def asset_turnover(sales, total_assets):
    """
    Asset Turnover Ratio
    """
    if total_assets == 0:
        return None

    return round(sales / total_assets, 2)

def debt_to_equity(borrowings, equity_capital, reserves):
    equity = equity_capital + reserves

    if borrowings == 0:
        return 0

    if equity <= 0:
        return None

    return round(borrowings / equity, 2)


def high_leverage_flag(de_ratio, is_financial=False):
    if is_financial:
        return False

    return de_ratio is not None and de_ratio > 5


def interest_coverage_ratio(operating_profit, other_income, interest):
    if interest == 0:
        return None

    ebit = operating_profit + other_income
    return round(ebit / interest, 2)


def icr_label(interest):
    if interest == 0:
        return "Debt Free"

    return None


def net_debt(borrowings, investments):
    return borrowings - investments


def asset_turnover(sales, total_assets):
    if total_assets == 0:
        return None

    return round(sales / total_assets, 2)