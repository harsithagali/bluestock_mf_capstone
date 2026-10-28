import sqlite3
import pandas as pd

def run_etl():
    # Load all 10 CSV datasets
    fund_master = pd.read_csv('01_fund_master.csv')
    nav_history = pd.read_csv('02_nav_history.csv')
    aum_by_fund_house = pd.read_csv('03_aum_by_fund_house.csv')
    monthly_sip_inflows = pd.read_csv('04_monthly_sip_inflows.csv')
    category_inflows = pd.read_csv('05_category_inflows.csv')
    industry_folio_count = pd.read_csv('06_industry_folio_count.csv')
    performance = pd.read_csv('07_scheme_performance.csv')
    transactions = pd.read_csv('08_investor_transactions.csv')
    portfolio_holdings = pd.read_csv('09_portfolio_holdings.csv')
    benchmark_indices = pd.read_csv('10_benchmark_indices.csv')
    
    # Preprocess & Clean Data
    nav_history['date'] = pd.to_datetime(nav_history['date'])
    nav_history = nav_history.sort_values(['amfi_code', 'date'])
    nav_history['nav'] = nav_history.groupby('amfi_code')['nav'].ffill()
    
    transactions['transaction_date'] = pd.to_datetime(transactions['transaction_date'])
    transactions['annual_income_lakh'] = transactions['annual_income_lakh'].fillna(transactions['annual_income_lakh'].median())
    
    # Save all tables to SQLite Database
    conn = sqlite3.connect('bluestock_mf.db')
    fund_master.to_sql('dim_fund', conn, if_exists='replace', index=False)
    nav_history.to_sql('fact_nav', conn, if_exists='replace', index=False)
    aum_by_fund_house.to_sql('fact_aum', conn, if_exists='replace', index=False)
    monthly_sip_inflows.to_sql('fact_sip_monthly', conn, if_exists='replace', index=False)
    category_inflows.to_sql('fact_category_inflows', conn, if_exists='replace', index=False)
    industry_folio_count.to_sql('fact_folios', conn, if_exists='replace', index=False)
    performance.to_sql('fact_performance', conn, if_exists='replace', index=False)
    transactions.to_sql('fact_transactions', conn, if_exists='replace', index=False)
    portfolio_holdings.to_sql('fact_holdings', conn, if_exists='replace', index=False)
    benchmark_indices.to_sql('fact_benchmarks', conn, if_exists='replace', index=False)
    
    print("ETL execution finished. All 10 dataset tables updated in bluestock_mf.db successfully!")

if __name__ == "__main__":
    run_etl()