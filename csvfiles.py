import numpy as np
import pandas as pd

dict1={
  'Name':['monirul',"rahul","rupsa"],
  'Roll':[45,46,23],
  'Marks':[56,98,53],
  'City':["Bankura","kolkata","mednipur"]
}

df=pd.DataFrame(dict1)
print(df)

# Convert into excel sheet.........
newdf=df.to_csv('data.csv')
print(newdf)

# read csv files..........
csv=pd.read_csv('data.csv')
print(csv)

# Removing index in csv files........
newcsv=df.to_csv('NoIndex.csv',index=False)
print(newcsv)

# without indexing csv files.......
print("\nReading csv fles.........\n")
print(pd.read_csv('NoIndex.csv'))
