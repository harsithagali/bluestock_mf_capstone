-- Analytical Business Queries

-- 1. Top 5 Schemes by AUM
SELECT scheme_name, aum_crore 
FROM fact_performance 
ORDER BY aum_crore DESC 
LIMIT 5;

-- 2. Total Transaction Volume & Count by State
SELECT state, COUNT(*) AS total_transactions, SUM(amount_inr) AS total_volume_inr 
FROM fact_transactions 
GROUP BY state 
ORDER BY total_volume_inr DESC;

-- 3. Top Direct Plans with Expense Ratio < 1.0%
SELECT scheme_name, expense_ratio_pct 
FROM dim_fund 
WHERE plan = 'Direct' AND expense_ratio_pct < 1.0 
ORDER BY expense_ratio_pct ASC;

-- 4. High Sharpe Ratio Funds (> 1.0) sorted by 3-Year Returns
SELECT scheme_name, sharpe_ratio, return_3yr_pct 
FROM fact_performance 
WHERE sharpe_ratio > 1.0 
ORDER BY return_3yr_pct DESC;