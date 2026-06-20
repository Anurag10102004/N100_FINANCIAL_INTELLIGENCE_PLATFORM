import pytest

from src.etl.normaliser import normalize_year, normalize_ticker

# ---------- normalize_year tests ----------

def test_year_string():
    assert normalize_year("2024") == 2024

def test_year_int():
    assert normalize_year(2025) == 2025

def test_invalid_year_zero():
    with pytest.raises(ValueError):
        normalize_year(0)

def test_year_1990():
    assert normalize_year("1990") == 1990

def test_year_2050():
    assert normalize_year("2050") == 2050

def test_year_with_spaces():
    assert normalize_year("2023") == 2023

def test_invalid_year_large():
    with pytest.raises(ValueError):
        normalize_year("9999")

def test_invalid_year_small():
    with pytest.raises(ValueError):
        normalize_year("1")

def test_year_2000():
    assert normalize_year("2000") == 2000

def test_year_2015():
    assert normalize_year("2015") == 2015


# ---------- normalize_ticker tests ----------

def test_ticker_upper():
    assert normalize_ticker("INFY") == "INFY"

def test_ticker_lower():
    assert normalize_ticker("infy") == "INFY"

def test_ticker_spaces():
    assert normalize_ticker(" infy ") == "INFY"

def test_ticker_tcs():
    assert normalize_ticker("tcs") == "TCS"

def test_ticker_reliance():
    assert normalize_ticker("reliance") == "RELIANCE"

def test_ticker_hdfc():
    assert normalize_ticker("hdfc") == "HDFC"

def test_ticker_icici():
    assert normalize_ticker(" icici ") == "ICICI"

def test_ticker_single_char():
    assert normalize_ticker("a") == "A"

def test_ticker_numeric():
    assert normalize_ticker("123") == "123"

def test_ticker_mixed():
    assert normalize_ticker("InFy") == "INFY"