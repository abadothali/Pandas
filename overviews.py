import numpy as np
import pandas as pd

# Csv files Operations..........
dict1={
  'Name':['monirul','rupsa','rahul','krishna','gautom'],
  'Roll':[56,88,17,55,34],
  'City':['bankura','kolkata','mednipur','kolkata','jharkhand']
}

# Dict1 connect to pandas.....
df=pd.DataFrame(dict1)
print(df)

# Convert csv files....
df=df.to_csv('data.csv',index=False)
print(df)

# Read csv files.........
print("\nRead csv files........")
df=pd.read_csv('data.csv')
print(df)

# Read starting value....
x=df.head(2)
print("\nRead starting value....")
print(x)

# Read ending value.......
y=df.tail(2)
print("\nRead ending value....")
print(y)

# Describe data's.......
z=df.describe()
print("\nDescribes values.......")
print(z)

# Explain info..........
print('\nExplain info............')
print(df.info())

# Describe mean.........
print('\nDescribe mean........')
print(df.mean)