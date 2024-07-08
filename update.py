import numpy as np
import pandas as pd

# we read a csv files....
data=pd.read_csv('data.csv')
print(data)

# access values...
print("\nPrint all roll from data.csv files....")
print(data['Roll'])

# access specifix values...
print("\nAccess specifix values......")
print(data['Roll'][0])
print(data['Name'][4])

# update values.....
print("\nUpdate values....")
data['Name'][4]='Anand'
print(data)

# Save as updated value in csv file.....
df=pd.DataFrame(data)
print(df)
df=data.to_csv('data.csv')
print(df)

