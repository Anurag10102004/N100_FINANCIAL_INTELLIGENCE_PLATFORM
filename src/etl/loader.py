import pandas as pd
import sqlite3

conn = sqlite3.connect("nifty100.db")

df = pd.read_excel("data/companies.xlsx", header=1)

# Purana data delete
conn.execute("DELETE FROM companies")

# Companies load
for index, row in df.iterrows():
    conn.execute(
        """
        INSERT INTO companies
        (company_id, company_name, ticker)
        VALUES (?, ?, ?)
        """,
        (
            index + 1,
            row["company_name"],
            row["id"]
        )
    )

conn.commit()

cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM companies")
print("Companies Loaded:", cursor.fetchone()[0])

conn.close()