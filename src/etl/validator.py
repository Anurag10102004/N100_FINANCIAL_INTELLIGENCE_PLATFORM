import pandas as pd

def check_duplicate_company_ids(df):
    return df[df["company_id"].duplicated()]

def check_duplicate_company_year(df):
    return df[df.duplicated(["company_id", "year"])]

def check_null_company_ids(df):
    return df[df["company_id"].isnull()]