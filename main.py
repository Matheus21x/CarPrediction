import pandas as pd

df = pd.read_csv(r'C:\Users\Matheus\OneDrive\Desktop\ML-CARPRED\CarPrice_Assignment.csv')

print(df[df.isna().any(axis=1)])