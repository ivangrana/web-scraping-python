import pandas as pd

df = pd.read_csv('convocação nacional.csv')

print(df.nickname.value_counts())