import sqlite3

conn = sqlite3.connect("nifty100.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS companies (
    company_id INTEGER PRIMARY KEY,
    company_name TEXT NOT NULL,
    ticker TEXT UNIQUE
)
""")

cursor.execute("""
INSERT OR IGNORE INTO companies
(company_id, company_name, ticker)
VALUES
(1,'Reliance Industries','RELIANCE'),
(2,'TCS','TCS'),
(3,'Infosys','INFY')
""")

conn.commit()

print("Sample Data Loaded Successfully")

conn.close()