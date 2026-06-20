CREATE TABLE IF NOT EXISTS companies (
    company_id INTEGER PRIMARY KEY,
    company_name TEXT NOT NULL,
    ticker TEXT UNIQUE
);

CREATE TABLE IF NOT EXISTS profitandloss (
    company_id INTEGER,
    year INTEGER,
    sales REAL,
    profit REAL,
    PRIMARY KEY (company_id, year),
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE IF NOT EXISTS balancesheet (
    company_id INTEGER,
    year INTEGER,
    assets REAL,
    liabilities REAL,
    PRIMARY KEY (company_id, year),
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE IF NOT EXISTS cashflow (
    company_id INTEGER,
    year INTEGER,
    operating_cf REAL,
    PRIMARY KEY (company_id, year),
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE IF NOT EXISTS sectors (
    sector_id INTEGER PRIMARY KEY,
    sector_name TEXT
);

CREATE TABLE IF NOT EXISTS stock_prices (
    company_id INTEGER,
    trade_date DATE,
    close_price REAL,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE IF NOT EXISTS financial_ratios (
    company_id INTEGER,
    year INTEGER,
    pe_ratio REAL,
    roe REAL,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE IF NOT EXISTS analysis (
    analysis_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    remarks TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE IF NOT EXISTS documents (
    document_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    document_name TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);

CREATE TABLE IF NOT EXISTS peer_groups (
    peer_group_id INTEGER PRIMARY KEY,
    company_id INTEGER,
    peer_company TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(company_id)
);