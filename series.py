import pandas as pd
import numpy as np

# Series datatypes........
ser=pd.Series(np.random.rand(22))
print(ser)

# Check series types.....
print(type(ser))

# For knowing index........
print(ser.index)

# Check data types........
print(ser.dtype)

# for knowing starting elements.....
print(ser.head(7))

# for knowing last elements.......
print(ser.tail(9))
