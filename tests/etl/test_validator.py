import pandas as pd
from src.etl.validator import (
    check_duplicate_company_ids,
    check_duplicate_company_year,
    check_null_company_ids
)

def test_duplicate_company_ids():
    df = pd.DataFrame({
        "company_id": [1, 1, 2]
    })

    result = check_duplicate_company_ids(df)
    assert len(result) == 1

def test_duplicate_company_year():
    df = pd.DataFrame({
        "company_id": [1, 1],
        "year": [2024, 2024]
    })

    result = check_duplicate_company_year(df)
    assert len(result) == 1

def test_null_company_ids():
    df = pd.DataFrame({
        "company_id": [1, None, 2]
    })

    result = check_null_company_ids(df)
    assert len(result) == 1