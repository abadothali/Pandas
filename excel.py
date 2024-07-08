import numpy as np
import pandas as pd

# read excle files..........
data=pd.read_excel('data.xlsx')
print(data)

# update excle files.....
data['Name'][0]='abadoth'
print(data)

# Save update in excel file....
data.to_excel('data.xlsx')
print(data)

# read update values....
data=pd.read_excel('data.xlsx',)
print(data)
