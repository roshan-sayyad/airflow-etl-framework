def transform(df):
    df['customer_name'] = df['customer_name'].str.upper()
    print("Transformation completed")
    return df
