import pandas as pd
datestrs = ['01/01/2017', '02/01/2017']

df = pd.to_datetime(datestrs)
print (df)

idx = pd.to_datetime(datestrs + [None, ''])
print (idx)

print (idx[2]) 
print (idx[3]) 

print (pd.isnull(idx))

