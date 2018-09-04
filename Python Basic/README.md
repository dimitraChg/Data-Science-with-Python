# Python

In this folder you will find some examples of how to create pandas Series and DataFrames in Python. In addition you will see how
to create some charts with these objects. Also, in this section you will see the results of the code.

This is the output of the Working with pandas Series and DataFrames.py file:

series_obj=
row 1    0
row 2    1
row 3    2
row 4    3
row 5    4
row 6    5
row 7    6
row 8    7
dtype: int32

series_obj['row 7']=
6

series_obj[[0, 7]]=
row 1    0
row 8    7
dtype: int32

series_obj['row 3': 'row 7']=
row 3    2
row 4    3
row 5    4
row 6    5
row 7    6
dtype: int32


DF_obj=
       column 1  column 2  column 3  column 4  column 5  column 6
row 1  0.870124  0.582277  0.278839  0.185911  0.411100  0.117376
row 2  0.684969  0.437611  0.556229  0.367080  0.402366  0.113041
row 3  0.447031  0.585445  0.161985  0.520719  0.326051  0.699186
row 4  0.366395  0.836375  0.481343  0.516502  0.383048  0.997541
row 5  0.514244  0.559053  0.034450  0.719930  0.421004  0.436935
row 6  0.281701  0.900274  0.669612  0.456069  0.289804  0.525819

DF_obj.ix[['row 2', 'row 5'], ['column 5', 'column 2']]=
       column 5  column 2
row 2  0.402366  0.437611
row 5  0.421004  0.559053

