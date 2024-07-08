import pandas as pd
import numpy as np

# data frame data types.......
print("\nPrint random numbers.........")
df=pd.DataFrame(np.random.rand(22,5), index=np.arange(22))
print(df)

# check data types....
print("\nprint data types...........")
print(type(df))

# for knowing the column.........
print("\nfor knowing the column.........")
print(df.columns)

# convert into array........
arr=df.to_numpy()
print("\nconvert into array........")
print(arr)
print(type(arr))

# Starting Record.......
print("\nStarting Record.......")
print(df.head())

# Ending Record..........
print("\nEnding Record..........")
print(df.tail())
