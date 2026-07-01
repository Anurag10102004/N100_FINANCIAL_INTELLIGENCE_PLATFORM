import pandas as pd
import sqlite3

conn = sqlite3.connect("nifty100.db")

# Load Excel Files
pl = pd.read_excel("data/profitandloss.xlsx", header=1)
bs = pd.read_excel("data/balancesheet.xlsx", header=1)
cf = pd.read_excel("data/cashflow.xlsx", header=1)

# Load into SQLite
pl.to_sql("profitandloss", conn, if_exists="replace", index=False)
bs.to_sql("balancesheet", conn, if_exists="replace", index=False)
cf.to_sql("cashflow", conn, if_exists="replace", index=False)

print("Profit & Loss Rows :", len(pl))
print("Balance Sheet Rows :", len(bs))
print("Cashflow Rows      :", len(cf))

conn.close()

print("Financial tables loaded successfully.")