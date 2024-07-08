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

# change indexing.....
print("\nChanging index.........")
df.index=['first','second','third','fourth','fifth']
print(df)

# print all index.......
print(df.index)

# print all columns.....
print(df.columns)

# convert into numpy.....
print("\nconvert into numpy.....")
num=df.to_numpy()
print(num)
print(type(num))

# transform row is column, & column is row.......
ser=pd.DataFrame(np.random.rand(20,5))
print(ser)
print('transform row is column, & column is........')
print(ser.T)

# sorting........
s=ser.sort_index(axis=1,ascending=False)
print("desendong........")
print(s)

# print type(ser[0]).........
print(type(ser[0]))