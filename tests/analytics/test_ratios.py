import pytest

from src.analytics.ratios import (
    net_profit_margin,
    operating_profit_margin,
    return_on_equity,
    return_on_assets,
    return_on_capital_employed,
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
    assert (
        return_on_capital_employed(
            200,
            50,
            500,
            500,
            500,
        )
        == 16.67
    )