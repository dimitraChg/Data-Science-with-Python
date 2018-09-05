import numpy as np
import pandas as pd 
from pandas import Series, DataFrame

missing_value = np.nan

series_obj = Series(['row 1', 'row 2', missing_value, 'row 4', 'row 5', 'row 6', missing_value, 'row 8'])
print(series_obj)

print(series_obj.isnull())

np.random.seed(25)
DF_obj = DataFrame(np.random.randn(36).reshape(6, 6))
print(DF_obj)

DF_obj.ix[3:5, 0] = missing_value
DF_obj.ix[1:4, 5] = missing_value
print(DF_obj)

print(DF_obj.isnull().sum())

# In order to fill the missing values in a DataFrame object there are 3 methods shown below:

# Method 1
filled_DF_with_method_1 = DF_obj.fillna(0)
print(filled_DF_with_method_1)

# Method 2
filled_DF_with_method_2 = DF_obj.fillna({0: 0.1, 5: 1.25})
print(filled_DF_with_method_2)

# Method 3
filled_DF_with_method_3 = DF_obj.fillna(method='ffill')
print(filled_DF_with_method_3)

DF_no_NaN = DF_obj.dropna(axis=1)
print(DF_no_NaN)

print(DF_obj.dropna(how='all'))
