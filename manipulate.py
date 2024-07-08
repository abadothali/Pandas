import numpy as np
import pandas as pd

# data frame data types.......
df=pd.DataFrame(np.random.rand(22,5))
print("Random data's.........")
print(df)

# for knowing value of the specifix place......
print('\nValues of 0,2 is.........')
print(df.loc[0,2])

# change column name.......
print("\nChange column names.........")
df.columns=list('ABCDE')
print(df)

# for knowing value of the specifix place......
print('\nValues of 7,C is.........')
print(df.loc[7,'C'])

# Drop column......
print("\nDrop column.....")
df=df.drop('A',axis=1)
print(df)

# Drop Row.......
print("\nDrop row......")
df=df.drop(7,axis=0)
print(df)

# iloc: working accoding to index.......
print("\nWorking in iloc...........")
df=df.iloc[0,0]
print(df)
