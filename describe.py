import numpy as np
import pandas as pd

dict1={
  'Name':['monirul','rahul','sarfaraj','gautom'],
  'Roll':[12,45,67,99],
  'Marks':[45,78,67,98]
}

# describes values.........
des2=pd.DataFrame(dict1)
print("\nDescribes data........")
print(des2.describe())