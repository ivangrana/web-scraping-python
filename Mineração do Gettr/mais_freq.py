import pandas as pd

frame = pd.read_csv('Guerra Civil.csv')

print(frame['username'].value_counts()) 

