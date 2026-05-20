def load(df, path):
    df.to_csv(path, index=False)
    print("Data loaded successfully")
