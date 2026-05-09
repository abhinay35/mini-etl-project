import pandas as pd
import sqlite3

def extract():
    print("Extracting data...")
    return pd.read_csv('../data/sales.csv')

def transform(df):
    print("Transforming data...")
    
    # Remove duplicates
    df.drop_duplicates(inplace=True)
    
    # Remove null values
    df.dropna(inplace=True)
    
    # Add total price column
    df['total_price'] = df['price'] * df['quantity']
    
    # Add category column
    df['category'] = df['product'].apply(lambda x: 'Electronics')
    
    return df

def load(df):
    print("Loading data into database...")
    conn = sqlite3.connect('../output/sales.db')
    df.to_sql('sales_data', conn, if_exists='replace', index=False)
    conn.close()

def main():
    df = extract()
    df = transform(df)
    load(df)
    print("ETL Pipeline Completed Successfully ✅")

if __name__ == "__main__":
    main()