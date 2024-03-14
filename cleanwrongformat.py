import pandas as pd

df = pd.read_csv('datax.csv')

df['Date'] = pd.to_datetime(df['Date'])

print(df.to_string())