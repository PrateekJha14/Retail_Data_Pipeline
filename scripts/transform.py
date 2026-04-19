import pandas as pd

def transform_data(df):
    # Clean column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Remove duplicates
    df = df.drop_duplicates()

    # Drop missing values
    df = df.dropna()

    # Convert data types
    df['sales'] = df['sales'].astype(float)
    df['profit'] = df['profit'].astype(float)
    df['quantity'] = df['quantity'].astype(int)

    # Feature engineering
    df['profit_margin'] = df['profit'] / df['sales']

    # Remove invalid values
    df = df[df['sales'] > 0]

    print("Transformed:", df.shape)
    return df