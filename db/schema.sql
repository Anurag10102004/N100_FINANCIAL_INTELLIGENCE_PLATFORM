CREATE TABLE IF NOT EXISTS companies (
    company_id INTEGER PRIMARY KEY,
    company_name TEXT NOT NULL,
    ticker TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS profitandloss (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company_id INTEGER,
    year INTEGER,
    sales REAL,
    profit REAL,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);