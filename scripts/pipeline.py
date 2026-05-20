from extract import extract
from transform import transform
from load import load

source_path = 'data/source.csv'
target_path = 'data/target.csv'

df = extract(source_path)

df = transform(df)

load(df, target_path)

print("Pipeline completed successfully")
