import pandas as pd

df = pd.read_csv('stars.csv')

print (df.isnull().sum())
modifiedDF = df.dropna()
modifiedDF.to_csv('ms.csv',index=False)