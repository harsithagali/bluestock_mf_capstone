import pandas as pd

def recommend_funds(risk_appetite='Moderate', top_n=3):
    perf = pd.read_csv('07_scheme_performance (1).csv')
    master = pd.read_csv('01_fund_master.csv')
    
    merged = perf.merge(master[['amfi_code', 'risk_category']], on='amfi_code')
    filtered = merged[merged['risk_category'].str.lower() == risk_appetite.lower()]
    
    # Sort funds by Sharpe Ratio
    top_funds = filtered.sort_values('sharpe_ratio', ascending=False).head(top_n)
    return top_funds[['amfi_code', 'scheme_name', 'category', 'sharpe_ratio', 'return_3yr_pct']]

if __name__ == "__main__":
    print("Recommended Funds for Moderate Risk Profile:")
    print(recommend_funds('Moderate'))