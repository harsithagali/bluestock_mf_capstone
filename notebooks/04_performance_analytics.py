import pandas as pd
import numpy as np
import scipy.stats as stats

# Load datasets
fund_master = pd.read_csv('01_fund_master.csv')
nav_history = pd.read_csv('02_nav_history.csv')
benchmarks = pd.read_csv('10_benchmark_indices.csv')

# Clean dates & sort
nav_history['date'] = pd.to_datetime(nav_history['date'])
benchmarks['date'] = pd.to_datetime(benchmarks['date'])
nav_history = nav_history.sort_values(['amfi_code', 'date'])

# Risk-free rate (6.5% standard for India repo rate)
rf = 0.065

metrics_list = []

for amfi, group in nav_history.groupby('amfi_code'):
    group = group.copy()
    group['daily_return'] = group['nav'].pct_change()
    
    # 1. CAGR calculation
    years = (group['date'].iloc[-1] - group['date'].iloc[0]).days / 365.25
    cagr = ((group['nav'].iloc[-1] / group['nav'].iloc[0]) ** (1 / years)) - 1
    
    # 2. Annualized Volatility
    ann_vol = group['daily_return'].std() * np.sqrt(252)
    
    # 3. Sharpe Ratio
    sharpe = (cagr - rf) / ann_vol if ann_vol != 0 else 0
    
    # 4. Sortino Ratio (Downside std dev)
    downside_returns = group[group['daily_return'] < 0]['daily_return']
    downside_std = downside_returns.std() * np.sqrt(252)
    sortino = (cagr - rf) / downside_std if downside_std != 0 else 0
    
    # 5. Max Drawdown
    group['peak'] = group['nav'].cummax()
    group['drawdown'] = (group['nav'] - group['peak']) / group['peak']
    max_dd = group['drawdown'].min()
    
    metrics_list.append({
        'amfi_code': amfi,
        'cagr_pct': round(cagr * 100, 2),
        'annual_volatility_pct': round(ann_vol * 100, 2),
        'sharpe_ratio': round(sharpe, 2),
        'sortino_ratio': round(sortino, 2),
        'max_drawdown_pct': round(max_dd * 100, 2)
    })

# Save to CSV in reports
df_metrics = pd.DataFrame(metrics_list)
df_metrics.to_csv('reports/fund_risk_performance_metrics.csv', index=False)
print("Performance & Risk Metrics computed and saved to reports/fund_risk_performance_metrics.csv!")