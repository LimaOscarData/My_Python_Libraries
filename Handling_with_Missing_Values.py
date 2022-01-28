import pandas as pd
import numpy as np
import seaborn as sn

id_no = ["P001","P002","P003","P004","P005","P006","P007","P008","P009","P010","P011"]
gender=["M","F","M","F","M","F","M","F","M","F","M"]
status = ["FT","PT","-","FT","PT","PT","FT","-","PT","FT",np.nan]
dept = ["DS","FS","AWS","AWS","DS",np.nan,"FS","FS",np.nan,"DS","AWS"]
V1 = np.array([2,3,5,np.nan,7,1,np.nan,10,14,"-",6])
V2 = np.array([8,np.nan,5,8,11,np.nan,np.nan,2,3,7,9])
salary = np.array([np.nan,54,59,120,58,75,np.nan,136,60,125,np.nan])
df = pd.DataFrame({
                   "id" : id_no,
                   "gender": gender,
                   "status": status,
                   "dept": dept,
                   "var1" : V1,
                   "var2" : V2,
                   "salary" : salary
                  })
# print(df)

#       id gender status dept var1  var2  salary
# 0   P001      M     FT   DS    2   8.0     NaN
# 1   P002      F     PT   FS    3   NaN    54.0
# 2   P003      M      -  AWS    5   5.0    59.0
# 3   P004      F     FT  AWS  nan   8.0   120.0
# 4   P005      M     PT   DS    7  11.0    58.0
# 5   P006      F     PT  NaN    1   NaN    75.0
# 6   P007      M     FT   FS  nan   NaN     NaN
# 7   P008      F      -   FS   10   2.0   136.0
# 8   P009      M     PT  NaN   14   3.0    60.0
# 9   P010      F     FT   DS    -   7.0   125.0
# 10  P011      M    NaN  AWS    6   9.0     NaN


##################### Type of NaN Values #####################

# print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 11 entries, 0 to 10
# Data columns (total 7 columns):
#  #   Column  Non-Null Count  Dtype
# ---  ------  --------------  -----
#  0   id      11 non-null     object
#  1   gender  11 non-null     object
#  2   status  10 non-null     object
#  3   dept    9 non-null      object
#  4   var1    11 non-null     object
#  5   var2    8 non-null      float64
#  6   salary  8 non-null      float64
# dtypes: float64(2), object(5)
# memory usage: 744.0+ bytes
# None

# ------------------------------------------------------------

# print(type(np.nan))
# <class 'float'>

# print(type(np.NaN))
# <class 'float'>

# print(type(None))
# <class 'NoneType'>

# ------------------------------------------------------------

# print(df['salary'])
# 0       NaN
# 1      54.0
# 2      59.0
# 3     120.0
# 4      58.0
# 5      75.0
# 6       NaN
# 7     136.0
# 8      60.0
# 9     125.0
# 10      NaN
# Name: salary, dtype: float64

# print(type(df['salary']))
# <class 'pandas.core.series.Series'>

# Nan's type is float .
# print(type(df['salary'][0]))
# <class 'numpy.float64'>

# print(type(df['salary'][1]))
# <class 'numpy.float64'>

# print(df['status'])
# 0      FT
# 1      PT
# 2       -
# 3      FT
# 4      PT
# 5      PT
# 6      FT
# 7       -
# 8      PT
# 9      FT
# 10    NaN
# Name: status, dtype: object

# print(df['status'][2])
# -

# print(type(df['status'][2]))
# <class 'str'>

# print(type(df['status'][10]))
# <class 'float'>

# print(df['var1'])
# 0       2
# 1       3
# 2       5
# 3     nan
# 4       7
# 5       1
# 6     nan
# 7      10
# 8      14
# 9       -
# 10      6
# Name: var1, dtype: object

# if there is one str value, it converts all the series to object(str).
# print(type(df['var1'][3]))
# <class 'str'>
#
# print(type(df['var1'][9]))
# <class 'str'>
# -

# print(type(df['var1']))
# <class 'pandas.core.series.Series'>

################### Detecting Missing Values #####################
# NaN, standing for not a number, is a numeric data type used to represent
# any value that is undefined or unpresentable.

# print(df)
#       id gender status dept var1  var2  salary
# 0   P001      M     FT   DS    2   8.0     NaN
# 1   P002      F     PT   FS    3   NaN    54.0
# 2   P003      M      -  AWS    5   5.0    59.0
# 3   P004      F     FT  AWS  nan   8.0   120.0
# 4   P005      M     PT   DS    7  11.0    58.0
# 5   P006      F     PT  NaN    1   NaN    75.0
# 6   P007      M     FT   FS  nan   NaN     NaN
# 7   P008      F      -   FS   10   2.0   136.0
# 8   P009      M     PT  NaN   14   3.0    60.0
# 9   P010      F     FT   DS    -   7.0   125.0
# 10  P011      M    NaN  AWS    6   9.0     NaN

# both of them gives the same values :
# print(df.isnull())
# print(df.isna())
#        id  gender  status   dept   var1   var2  salary
# 0   False   False   False  False  False  False    True
# 1   False   False   False  False  False   True   False
# 2   False   False   False  False  False  False   False
# 3   False   False   False  False  False  False   False
# 4   False   False   False  False  False  False   False
# 5   False   False   False   True  False   True   False
# 6   False   False   False  False  False   True    True
# 7   False   False   False  False  False  False   False
# 8   False   False   False   True  False  False   False
# 9   False   False   False  False  False  False   False
# 10  False   False    True  False  False  False    True

# both gives the same results :
# print(df.notnull())
# print(df.notna())
#       id  gender  status   dept  var1   var2  salary
# 0   True    True    True   True  True   True   False
# 1   True    True    True   True  True  False    True
# 2   True    True    True   True  True   True    True
# 3   True    True    True   True  True   True    True
# 4   True    True    True   True  True   True    True
# 5   True    True    True  False  True  False    True
# 6   True    True    True   True  True  False   False
# 7   True    True    True   True  True   True    True
# 8   True    True    True  False  True   True    True
# 9   True    True    True   True  True   True    True
# 10  True    True   False   True  True   True   False

# notnull without brackets () . It returns the same dataframe inside the
# angle brackets <> :
# print(df.notnull)
# <bound method DataFrame.notnull of       id gender status dept var1  var2  salary
# 0   P001      M     FT   DS    2   8.0     NaN
# 1   P002      F     PT   FS    3   NaN    54.0
# 2   P003      M      -  AWS    5   5.0    59.0
# 3   P004      F     FT  AWS  nan   8.0   120.0
# 4   P005      M     PT   DS    7  11.0    58.0
# 5   P006      F     PT  NaN    1   NaN    75.0
# 6   P007      M     FT   FS  nan   NaN     NaN
# 7   P008      F      -   FS   10   2.0   136.0
# 8   P009      M     PT  NaN   14   3.0    60.0
# 9   P010      F     FT   DS    -   7.0   125.0
# 10  P011      M    NaN  AWS    6   9.0     NaN>

# don't forget to use brackets/parentheses ().
# without parentheses() gives Attribute error :
# If any one of the relevant column has a null value, it returns True :
# print(df.isnull().any(axis=0))
# id        False
# gender    False
# status     True
# dept       True
# var1      False
# var2       True
# salary     True
# dtype: bool

# if any one of the rows has a null value it returns True :
# print(df.isnull().any(axis=1))
# 0      True
# 1      True
# 2     False
# 3     False
# 4     False
# 5      True
# 6      True
# 7     False
# 8      True
# 9     False
# 10     True
# dtype: bool

# finding the sum of relevant column :
# print(df.isnull().sum())
# id        0
# gender    0
# status    1
# dept      2
# var1      0
# var2      3
# salary    3
# dtype: int64

# default value of sum's axis=0, if you change it to axis=1 you can obtain the sum of rows:
# print(df.isnull().sum(axis=1))
# 0     1
# 1     1
# 2     0
# 3     0
# 4     0
# 5     2
# 6     2
# 7     0
# 8     1
# 9     0
# 10    2
# dtype: int64

# finding the sum of all null values inside a dataframe :
# print(df.isnull().sum().sum())
# 9

# find the salary column's is null condition, it returns the boolean value :
# print(df['salary'].isnull().any())
# True

# print(df['salary'].isnull().all())
# False

# Finding the sum of salary column's null value.
# print(df['salary'].isnull().sum())
# 3

# dataframe's columns total nulls :
# default value of sum is axis=0
# print(df.isnull().sum())
# id        0
# gender    0
# status    1
# dept      2
# var1      0
# var2      3
# salary    3
# dtype: int64

# print(df.isnull().sum(axis=1))
# 0     1
# 1     1
# 2     0
# 3     0
# 4     0
# 5     2
# 6     2
# 7     0
# 8     1
# 9     0
# 10    2
# dtype: int64

# print(len(df))
# 11

# percentage of null values for columns :
# print(df.isnull().sum()/ len(df)*100)
# id         0.000000
# gender     0.000000
# status     9.090909
# dept      18.181818
# var1       0.000000
# var2      27.272727
# salary    27.272727
# dtype: float64

# it shows the rows if there is a null value in any one of the colums
# (checks right direction)
# print(df.loc[df.isnull().any(axis=1)])
#       id gender status dept var1  var2  salary
# 0   P001      M     FT   DS    2   8.0     NaN
# 1   P002      F     PT   FS    3   NaN    54.0
# 5   P006      F     PT  NaN    1   NaN    75.0
# 6   P007      M     FT   FS  nan   NaN     NaN
# 8   P009      M     PT  NaN   14   3.0    60.0
# 10  P011      M    NaN  AWS    6   9.0     NaN

# ~ tilda character returns the opposite condition.
# below , there is no Null value :
# print(df.loc[~df.isnull().any(axis=1)])
#      id gender status dept var1  var2  salary
# 2  P003      M      -  AWS    5   5.0    59.0
# 3  P004      F     FT  AWS  nan   8.0   120.0
# 4  P005      M     PT   DS    7  11.0    58.0
# 7  P008      F      -   FS   10   2.0   136.0
# 9  P010      F     FT   DS    -   7.0   125.0

# all :
# it returns a result if all columns have null values.
# print(df.loc[df.isnull().all(axis=1)])
# Empty DataFrame
# Columns: [id, gender, status, dept, var1, var2, salary]
# Index: []

# it returns the columns if any one of salary column has a null value :
# print(df.loc[df['salary'].isnull()])
#       id gender status dept var1  var2  salary
# 0   P001      M     FT   DS    2   8.0     NaN
# 6   P007      M     FT   FS  nan   NaN     NaN
# 10  P011      M    NaN  AWS    6   9.0     NaN

# print(df.isnull().any(axis=0))
# # id        False
# # gender    False
# # status     True
# # dept       True
# # var1      False
# # var2       True
# # salary     True
# # dtype: bool

# print(df.isnull().any(axis=1))
# # 0      True
# # 1      True
# # 2     False
# # 3     False
# # 4     False
# # 5      True
# # 6      True
# # 7     False
# # 8      True
# # 9     False
# # 10     True
# # dtype: bool

#################### Converting inappropriate values to NaN values #####################
# map()
# replace()

print(df)


# Values in Series that are not in the dictionary
# (as keys) are converted to NaN.
# print(df['var1'].map({'-':np.nan}))
# 0    NaN
# 1    NaN
# 2    NaN
# 3    NaN
# 4    NaN
# 5    NaN
# 6    NaN
# 7    NaN
# 8    NaN
# 9    NaN
# 10   NaN
# Name: var1, dtype: float64
# Notes: When arg is a dictionary, values in Series that are not in the dictionary
# (as keys) are converted to NaN. However, if the dictionary is a dict subclass that
# defines missing (i.e. provides a method for default values), then this default is
# used rather than NaN.

# print(df['var1'].replace(to_replace='-', value=np.nan))
# 0       2
# 1       3
# 2       5
# 3     nan
# 4       7
# 5       1
# 6     nan
# 7      10
# 8      14
# 9     NaN
# 10      6
# Name: var1, dtype: object

# print(df['var1'].replace(to_replace='-', value=np.nan).astype('float'))
# 0      2.0
# 1      3.0
# 2      5.0
# 3      NaN
# 4      7.0
# 5      1.0
# 6      NaN
# 7     10.0
# 8     14.0
# 9      NaN
# 10     6.0
# Name: var1, dtype: float64

# The "to_replace" value's UPPER or lower case is not important .
# you can write 'nan' or 'NaN', it understand as NaN.
# print(df['var1'].replace(to_replace=['-', 'nan'], value=np.nan).astype(float))
# 0      2.0
# 1      3.0
# 2      5.0
# 3      NaN
# 4      7.0
# 5      1.0
# 6      NaN
# 7     10.0
# 8     14.0
# 9      NaN
# 10     6.0
# Name: var1, dtype: float64

# You can assign it to a column for saving original data frame.
df['var1'] = df['var1'].replace(to_replace='-', value=np.nan).astype('float')
# print(df['var1'])
# 0      2.0
# 1      3.0
# 2      5.0
# 3      NaN
# 4      7.0
# 5      1.0
# 6      NaN
# 7     10.0
# 8     14.0
# 9      NaN
# 10     6.0
# Name: var1, dtype: float64


df['status'] = df['status'].replace(to_replace='-', value=np.nan)
# print(df['status'])
# 0      FT
# 1      PT
# 2     NaN
# 3      FT
# 4      PT
# 5      PT
# 6      FT
# 7     NaN
# 8      PT
# 9      FT
# 10    NaN
# Name: status, dtype: object

print(df)
#       id gender status dept  var1  var2  salary
# 0   P001      M     FT   DS   2.0   8.0     NaN
# 1   P002      F     PT   FS   3.0   NaN    54.0
# 2   P003      M    NaN  AWS   5.0   5.0    59.0
# 3   P004      F     FT  AWS   NaN   8.0   120.0
# 4   P005      M     PT   DS   7.0  11.0    58.0
# 5   P006      F     PT  NaN   1.0   NaN    75.0
# 6   P007      M     FT   FS   NaN   NaN     NaN
# 7   P008      F    NaN   FS  10.0   2.0   136.0
# 8   P009      M     PT  NaN  14.0   3.0    60.0
# 9   P010      F     FT   DS   NaN   7.0   125.0
# 10  P011      M    NaN  AWS   6.0   9.0     NaN

print(df.isnull().sum())
# id        0
# gender    0
# status    3
# dept      2
# var1      3
# var2      3
# salary    3
# dtype: int64

print(df.isnull().sum(axis=1))
# 0     1
# 1     1
# 2     1
# 3     1
# 4     0
# 5     2
# 6     3
# 7     1
# 8     1
# 9     1
# 10    2
# dtype: int64


# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
# ------------------------------------------------------------
