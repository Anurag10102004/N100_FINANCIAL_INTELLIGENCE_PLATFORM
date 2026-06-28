from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_assets,
    return_on_capital_employed,
    debt_to_equity,
    high_leverage_flag,
    interest_coverage_ratio,
    icr_label,
    net_debt,
    asset_turnover,
)


def test_net_profit_margin():
    assert net_profit_margin(100, 1000) == 10.00


def test_net_profit_margin_zero_sales():
    assert net_profit_margin(100, 0) is None


def test_operating_profit_margin():
    assert operating_profit_margin(200, 1000) == 20.00


def test_roe():
    assert return_on_equity(100, 200, 300) == 20.00


def test_roe_negative_equity():
    assert return_on_equity(100, -200, 100) is None


def test_roa():
    assert return_on_assets(100, 1000) == 10.00


def test_roa_zero_assets():
    assert return_on_assets(100, 0) is None


def test_roce():
    assert return_on_capital_employed(
        200,
        50,
        500,
        500,
        500,
    ) == 16.67


def test_debt_to_equity():
    assert debt_to_equity(200, 100, 100) == 1.0


def test_debt_to_equity_debt_free():
    assert debt_to_equity(0, 100, 100) == 0


def test_interest_coverage():
    assert interest_coverage_ratio(200, 50, 50) == 5.0


def test_interest_zero():
    assert interest_coverage_ratio(200, 50, 0) is None


def test_icr_label():
    assert icr_label(0) == "Debt Free"


def test_net_debt():
    assert net_debt(500, 200) == 300


def test_asset_turnover():
    assert asset_turnover(1000, 500) == 2.0


def test_high_leverage():
    assert high_leverage_flag(6.0, False) is True