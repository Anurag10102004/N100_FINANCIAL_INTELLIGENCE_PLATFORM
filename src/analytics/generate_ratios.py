import sqlite3

conn = sqlite3.connect("nifty100.db")
cur = conn.cursor()
cur.execute("DELETE FROM financial_ratios")
cur.execute("""
SELECT
    COUNT(*)
FROM
    profitandloss p
INNER JOIN
    balancesheet b
ON
    p.company_id = b.company_id
AND
    p.year = b.year
INNER JOIN
    cashflow c
ON
    p.company_id = c.company_id
AND
    p.year = c.year
""")

print("Common Records:", cur.fetchone()[0])

from src.analytics.ratio_engine import calculate_ratios
cur.execute("""
SELECT
    p.company_id,
    p.year,

    p.sales,
    p.operating_profit,
    p.other_income,
    p.interest,
    p.net_profit,
    p.eps,
    p.dividend_payout,

    b.equity_capital,
    b.reserves,
    b.borrowings,
    b.investments,
    b.total_assets,

    c.operating_activity,
    c.investing_activity,
    c.financing_activity

FROM profitandloss p

JOIN balancesheet b
ON p.company_id=b.company_id
AND p.year=b.year

JOIN cashflow c
ON p.company_id=c.company_id
AND p.year=c.year
""")

rows = cur.fetchall()
for row in rows:

    pl = {
        "sales": row[2],
        "operating_profit": row[3],
        "other_income": row[4],
        "interest": row[5],
        "net_profit": row[6],
        "eps": row[7],
        "dividend_payout": row[8],
    }

    bs = {
        "equity_capital": row[9],
        "reserves": row[10],
        "borrowings": row[11],
        "investments": row[12],
        "total_assets": row[13],
    }

    cf = {
        "operating_activity": row[14],
        "investing_activity": row[15],
        "financing_activity": row[16],
    }
    if (
        cf["operating_activity"] is None or
        cf["investing_activity"] is None
    ):
        print("Skipping:", row[0], row[1], "Missing Cashflow")
        continue
    if(
        pl["sales"] is None or
        pl["operating_profit"] is None or
        pl["net_profit"] is None
    ):
        print("Skipping:", row[0], row[1], "Missing Profit & Loss Data")
        continue
    print("Company:", row[0], "Year:", row[1])
    print("PL:", pl)
    print("BS:", bs)
    print("CF:", cf)
    ratios = calculate_ratios(pl, bs, cf)

    cur.execute("""
    INSERT INTO financial_ratios
    (
        company_id,
        year,
        net_profit_margin_pct,
        operating_profit_margin_pct,
        return_on_equity_pct,
        return_on_assets_pct,
        return_on_capital_employed_pct,
        debt_to_equity,
        interest_coverage,
        asset_turnover,
        free_cash_flow_cr
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (
        row[0],
        row[1],
        ratios["net_profit_margin_pct"],
        ratios["operating_profit_margin_pct"],
        ratios["return_on_equity_pct"],
        ratios["return_on_assets_pct"],
        ratios["return_on_capital_employed_pct"],
        ratios["debt_to_equity"],
        ratios["interest_coverage"],
        ratios["asset_turnover"],
        ratios["free_cash_flow_cr"],
    ))

conn.commit()

print("Financial Ratios Generated:", len(rows))

print("Rows fetched:", len(rows))
conn.close()
