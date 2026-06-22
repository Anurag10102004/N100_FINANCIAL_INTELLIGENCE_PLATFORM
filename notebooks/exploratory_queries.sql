-- Total Companies
SELECT COUNT(*) FROM companies;

-- Top 10 Companies by Sales
SELECT company_id, sales
FROM profitandloss
ORDER BY sales DESC
LIMIT 10;

-- Top 10 Companies by Net Profit
SELECT company_id, net_profit
FROM profitandloss
ORDER BY net_profit DESC
LIMIT 10;

-- Companies with Highest ROE
SELECT company_id, roe
FROM financial_ratios
ORDER BY roe DESC
LIMIT 10;

-- Companies with Highest PE Ratio
SELECT company_id, pe_ratio
FROM financial_ratios
ORDER BY pe_ratio DESC
LIMIT 10;

-- Total Rows in Profit & Loss
SELECT COUNT(*) FROM profitandloss;

-- Total Rows in Balance Sheet
SELECT COUNT(*) FROM balancesheet;

-- Total Rows in Cashflow
SELECT COUNT(*) FROM cashflow;

-- Total Rows in Stock Prices
SELECT COUNT(*) FROM stock_prices;

-- Distinct Years Available
SELECT DISTINCT year
FROM profitandloss
ORDER BY year;