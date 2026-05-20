import pandas as pd

def extract(path):
    df = pd.read_csv(path)
    print("Data extracted")
    return df
