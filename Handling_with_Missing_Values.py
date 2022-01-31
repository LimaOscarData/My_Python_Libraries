import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

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

# print(df)


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

# print(df)
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

# print(df.isnull().sum())
# id        0
# gender    0
# status    3
# dept      2
# var1      3
# var2      3
# salary    3
# dtype: int64

# print(df.isnull().sum(axis=1))
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

############### Missing value handling methods ##################

# Deleting Rows ----->if it has more than 70-75% of missing values. This
# percentage can change according to the data. So each situation should be
# evaluated case by case.
#
# Replacing With Mean/Median/Mode (Imputation)--->can be applied on a feature
# which has numeric data
#
# Assigning An Unique Category--->If a categorical feature has definite number
# of classes, we can assign another class
#
# Predicting The Missing Values---> we can predict the nulls with the help of
# a machine learning algorithm like linear regression
#
# Using Algorithms Which Support Missing Values--->KNN is a machine learning
# algorithm which works on the principle of distance measure. This algorithm
# can be used when there are nulls present in the dataset. KNN considers the
# missing values by taking the majority of the K nearest values

# Dropping :
# dropna()
# drop()

# print(df)

# print(df.dropna(axis=1, how='any', thresh=None, inplace=False))
#       id gender
# 0   P001      M
# 1   P002      F
# 2   P003      M
# 3   P004      F
# 4   P005      M
# 5   P006      F
# 6   P007      M
# 7   P008      F
# 8   P009      M
# 9   P010      F
# 10  P011      M

# print(df.dropna(axis=0, how='any', thresh=None, inplace=False))
#      id gender status dept  var1  var2  salary
# 4  P005      M     PT   DS   7.0  11.0    58.0

# print(df.dropna(axis=1, how='all', thresh=0, inplace=False))
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

# 'any' : If any NA values are present, drop that row or column.
# 'all' : If all values are NA, drop that row or column.

# default of dropna:
# axis=0, how='any', thresh=0, inplace=False.

# dropna() with default values :
# don't forget to use parentheses ().
# If you don't use it, you can't apply it correctly
# print(df.dropna())
#      id gender status dept  var1  var2  salary
# 4  P005      M     PT   DS   7.0  11.0    58.0

# subset: specifies the rows/columns to look for null values.
# Use subset inside the square brackets [] .
# print(df.dropna(subset=['status']))
#      id gender status dept  var1  var2  salary
# 0  P001      M     FT   DS   2.0   8.0     NaN
# 1  P002      F     PT   FS   3.0   NaN    54.0
# 3  P004      F     FT  AWS   NaN   8.0   120.0
# 4  P005      M     PT   DS   7.0  11.0    58.0
# 5  P006      F     PT  NaN   1.0   NaN    75.0
# 6  P007      M     FT   FS   NaN   NaN     NaN
# 8  P009      M     PT  NaN  14.0   3.0    60.0
# 9  P010      F     FT   DS   NaN   7.0   125.0


df['delete_me'] = np.nan
# print(df)
#       id gender status dept  var1  var2  salary  delete_me
# 0   P001      M     FT   DS   2.0   8.0     NaN        NaN
# 1   P002      F     PT   FS   3.0   NaN    54.0        NaN
# 2   P003      M    NaN  AWS   5.0   5.0    59.0        NaN
# 3   P004      F     FT  AWS   NaN   8.0   120.0        NaN
# 4   P005      M     PT   DS   7.0  11.0    58.0        NaN
# 5   P006      F     PT  NaN   1.0   NaN    75.0        NaN
# 6   P007      M     FT   FS   NaN   NaN     NaN        NaN
# 7   P008      F    NaN   FS  10.0   2.0   136.0        NaN
# 8   P009      M     PT  NaN  14.0   3.0    60.0        NaN
# 9   P010      F     FT   DS   NaN   7.0   125.0        NaN
# 10  P011      M    NaN  AWS   6.0   9.0     NaN        NaN

df.dropna(axis=1, how='all', thresh=None, inplace=True)
# print(df)
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


# thresh=N requires that a column has at least N non-NaNs to survive.
# print(df.dropna(axis=1, how='any', thresh=9, inplace=False))
#       id gender dept
# 0   P001      M   DS
# 1   P002      F   FS
# 2   P003      M  AWS
# 3   P004      F  AWS
# 4   P005      M   DS
# 5   P006      F  NaN
# 6   P007      M   FS
# 7   P008      F   FS
# 8   P009      M  NaN
# 9   P010      F   DS
# 10  P011      M  AWS

# print(df.drop([1, 3, 5]))
#       id gender status dept  var1  var2  salary
# 0   P001      M     FT   DS   2.0   8.0     NaN
# 2   P003      M    NaN  AWS   5.0   5.0    59.0
# 4   P005      M     PT   DS   7.0  11.0    58.0
# 6   P007      M     FT   FS   NaN   NaN     NaN
# 7   P008      F    NaN   FS  10.0   2.0   136.0
# 8   P009      M     PT  NaN  14.0   3.0    60.0
# 9   P010      F     FT   DS   NaN   7.0   125.0
# 10  P011      M    NaN  AWS   6.0   9.0     NaN

# print(df.drop(index=[1, 2, 3]))
#       id gender status dept  var1  var2  salary
# 0   P001      M     FT   DS   2.0   8.0     NaN
# 4   P005      M     PT   DS   7.0  11.0    58.0
# 5   P006      F     PT  NaN   1.0   NaN    75.0
# 6   P007      M     FT   FS   NaN   NaN     NaN
# 7   P008      F    NaN   FS  10.0   2.0   136.0
# 8   P009      M     PT  NaN  14.0   3.0    60.0
# 9   P010      F     FT   DS   NaN   7.0   125.0
# 10  P011      M    NaN  AWS   6.0   9.0     NaN

# print(df.drop(['var1', 'var2'], axis=1))
#       id gender status dept  salary
# 0   P001      M     FT   DS     NaN
# 1   P002      F     PT   FS    54.0
# 2   P003      M    NaN  AWS    59.0
# 3   P004      F     FT  AWS   120.0
# 4   P005      M     PT   DS    58.0
# 5   P006      F     PT  NaN    75.0
# 6   P007      M     FT   FS     NaN
# 7   P008      F    NaN   FS   136.0
# 8   P009      M     PT  NaN    60.0
# 9   P010      F     FT   DS   125.0
# 10  P011      M    NaN  AWS     NaN

# print(df.drop(columns=['var1', 'var2']))
#       id gender status dept  salary
# 0   P001      M     FT   DS     NaN
# 1   P002      F     PT   FS    54.0
# 2   P003      M    NaN  AWS    59.0
# 3   P004      F     FT  AWS   120.0
# 4   P005      M     PT   DS    58.0
# 5   P006      F     PT  NaN    75.0
# 6   P007      M     FT   FS     NaN
# 7   P008      F    NaN   FS   136.0
# 8   P009      M     PT  NaN    60.0
# 9   P010      F     FT   DS   125.0
# 10  P011      M    NaN  AWS     NaN

########### Filling Missing Values (Imputation) #################
# fillna()
# where()
# interpolate()

# print(df)

########## a.Filling with a specific value :

# print(df.fillna(0))
#       id gender status dept  var1  var2  salary
# 0   P001      M     FT   DS   2.0   8.0     0.0
# 1   P002      F     PT   FS   3.0   0.0    54.0
# 2   P003      M      0  AWS   5.0   5.0    59.0
# 3   P004      F     FT  AWS   0.0   8.0   120.0
# 4   P005      M     PT   DS   7.0  11.0    58.0
# 5   P006      F     PT    0   1.0   0.0    75.0
# 6   P007      M     FT   FS   0.0   0.0     0.0
# 7   P008      F      0   FS  10.0   2.0   136.0
# 8   P009      M     PT    0  14.0   3.0    60.0
# 9   P010      F     FT   DS   0.0   7.0   125.0
# 10  P011      M      0  AWS   6.0   9.0     0.0

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

# print(df['var1'].fillna(0))
# 0      2.0
# 1      3.0
# 2      5.0
# 3      0.0
# 4      7.0
# 5      1.0
# 6      0.0
# 7     10.0
# 8     14.0
# 9      0.0
# 10     6.0
# Name: var1, dtype: float64

####### b.Filling with any Proper Value :

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

# print(df['var1'].mean())
# 6

# print(df['var1'].fillna(df['var1'].mean()))
# 0      2.0
# 1      3.0
# 2      5.0
# 3      6.0
# 4      7.0
# 5      1.0
# 6      6.0
# 7     10.0
# 8     14.0
# 9      6.0
# 10     6.0
# Name: var1, dtype: float64

# print(df['var1'].median())
# 5.5

# print(df['var1'].fillna(df['var1'].median()))
# 0      2.0
# 1      3.0
# 2      5.0
# 3      5.5
# 4      7.0
# 5      1.0
# 6      5.5
# 7     10.0
# 8     14.0
# 9      5.5
# 10     6.0
# Name: var1, dtype: float64

# FutureWarning: Dropping of nuisance columns in DataFrame reductions
# (with 'numeric_only=None') is deprecated; in a future version this
# will raise TypeError.  Select only valid columns before calling the reduction.

# print(df.mean(numeric_only=True))
# var1       6.000
# var2       6.625
# salary    85.875
# dtype: float64

# print(df.fillna(df.mean(numeric_only=True)))
#       id gender status dept  var1    var2   salary
# 0   P001      M     FT   DS   2.0   8.000   85.875
# 1   P002      F     PT   FS   3.0   6.625   54.000
# 2   P003      M    NaN  AWS   5.0   5.000   59.000
# 3   P004      F     FT  AWS   6.0   8.000  120.000
# 4   P005      M     PT   DS   7.0  11.000   58.000
# 5   P006      F     PT  NaN   1.0   6.625   75.000
# 6   P007      M     FT   FS   6.0   6.625   85.875
# 7   P008      F    NaN   FS  10.0   2.000  136.000
# 8   P009      M     PT  NaN  14.0   3.000   60.000
# 9   P010      F     FT   DS   6.0   7.000  125.000
# 10  P011      M    NaN  AWS   6.0   9.000   85.875

# filling columns with a specified values :
# print(df.fillna({'status': 'other', 'var1': df['var1'].mean(), 'var2': df['var2'].median()}))
#       id gender status dept  var1  var2  salary
# 0   P001      M     FT   DS   2.0   8.0     NaN
# 1   P002      F     PT   FS   3.0   7.5    54.0
# 2   P003      M  other  AWS   5.0   5.0    59.0
# 3   P004      F     FT  AWS   6.0   8.0   120.0
# 4   P005      M     PT   DS   7.0  11.0    58.0
# 5   P006      F     PT  NaN   1.0   7.5    75.0
# 6   P007      M     FT   FS   6.0   7.5     NaN
# 7   P008      F  other   FS  10.0   2.0   136.0
# 8   P009      M     PT  NaN  14.0   3.0    60.0
# 9   P010      F     FT   DS   6.0   7.0   125.0
# 10  P011      M  other  AWS   6.0   9.0     NaN

############### where() : Replace values where the condition is False #############

# print(df.notna())
#       id  gender  status   dept   var1   var2  salary
# 0   True    True    True   True   True   True   False
# 1   True    True    True   True   True  False    True
# 2   True    True   False   True   True   True    True
# 3   True    True    True   True  False   True    True
# 4   True    True    True   True   True   True    True
# 5   True    True    True  False   True  False    True
# 6   True    True    True   True  False  False   False
# 7   True    True   False   True   True   True    True
# 8   True    True    True  False   True   True    True
# 9   True    True    True   True  False   True    True
# 10  True    True   False   True   True   True   False

# You must use the axis= , option . Because it hasn't a default value.
# print(df.where(cond=df.notna(), other=df.mean(numeric_only=True), axis=1))
#       id gender status dept  var1    var2   salary
# 0   P001      M     FT   DS   2.0   8.000   85.875
# 1   P002      F     PT   FS   3.0   6.625   54.000
# 2   P003      M    NaN  AWS   5.0   5.000   59.000
# 3   P004      F     FT  AWS   6.0   8.000  120.000
# 4   P005      M     PT   DS   7.0  11.000   58.000
# 5   P006      F     PT  NaN   1.0   6.625   75.000
# 6   P007      M     FT   FS   6.0   6.625   85.875
# 7   P008      F    NaN   FS  10.0   2.000  136.000
# 8   P009      M     PT  NaN  14.0   3.000   60.000
# 9   P010      F     FT   DS   6.0   7.000  125.000
# 10  P011      M    NaN  AWS   6.0   9.000   85.875

# If there isn't any value before or after a value, interpolate can't calculate it.
# print(df.interpolate())
#       id gender status dept  var1  var2  salary
# 0   P001      M     FT   DS   2.0   8.0     NaN
# 1   P002      F     PT   FS   3.0   6.5    54.0
# 2   P003      M    NaN  AWS   5.0   5.0    59.0
# 3   P004      F     FT  AWS   6.0   8.0   120.0
# 4   P005      M     PT   DS   7.0  11.0    58.0
# 5   P006      F     PT  NaN   1.0   8.0    75.0
# 6   P007      M     FT   FS   5.5   5.0   105.5
# 7   P008      F    NaN   FS  10.0   2.0   136.0
# 8   P009      M     PT  NaN  14.0   3.0    60.0
# 9   P010      F     FT   DS  10.0   7.0   125.0
# 10  P011      M    NaN  AWS   6.0   9.0   125.0

########### c.Filling the Missing Values of Categorical Variables ##########
# print(df['dept'].mode())
# 0    AWS
# 1     DS
# 2     FS
# dtype: object

# print(df['dept'].mode()[0])
# AWS

# print(df['dept'].fillna(df['dept'].mode()[0]))
# 0      DS
# 1      FS
# 2     AWS
# 3     AWS
# 4      DS
# 5     AWS
# 6      FS
# 7      FS
# 8     AWS
# 9      DS
# 10    AWS
# Name: dept, dtype: object

# method: Literal["backfill", "bfill", "ffill", "pad"]
# print(df['dept'].fillna(method='bfill'))
# 0      DS
# 1      FS
# 2     AWS
# 3     AWS
# 4      DS
# 5      FS
# 6      FS
# 7      FS
# 8      DS
# 9      DS
# 10    AWS
# Name: dept, dtype: object

# print(df['dept'].fillna(method='ffill'))
# 0      DS
# 1      FS
# 2     AWS
# 3     AWS
# 4      DS
# 5      DS
# 6      FS
# 7      FS
# 8      FS
# 9      DS
# 10    AWS
# Name: dept, dtype: object


########### d.Filling by condition & by Group of the Categorical Variables ############
# df['dept'].fillna(method='ffill', inplace=True)
# print(df)
#       id gender status dept  var1  var2  salary
# 0   P001      M     FT   DS   2.0   8.0     NaN
# 1   P002      F     PT   FS   3.0   NaN    54.0
# 2   P003      M    NaN  AWS   5.0   5.0    59.0
# 3   P004      F     FT  AWS   NaN   8.0   120.0
# 4   P005      M     PT   DS   7.0  11.0    58.0
# 5   P006      F     PT   DS   1.0   NaN    75.0
# 6   P007      M     FT   FS   NaN   NaN     NaN
# 7   P008      F    NaN   FS  10.0   2.0   136.0
# 8   P009      M     PT   FS  14.0   3.0    60.0
# 9   P010      F     FT   DS   NaN   7.0   125.0
# 10  P011      M    NaN  AWS   6.0   9.0     NaN

# print(df.loc[df['salary'] >= 100, 'status'])
# 3     FT
# 7    NaN
# 9     FT
# Name: status, dtype: object

# In Loc :
# 1. write the condition,
# 2. then write which column that you want.
# print(df.loc[df['var1'] >= 4 , ['id', 'gender', 'status', 'salary']])
#       id gender status  salary
# 2   P003      M    NaN    59.0
# 4   P005      M     PT    58.0
# 7   P008      F    NaN   136.0
# 8   P009      M     PT    60.0
# 10  P011      M    NaN     NaN

# print(df.loc[df['var1'] >= 4 , 'id':'dept'])
#       id gender status dept
# 2   P003      M    NaN  AWS
# 4   P005      M     PT   DS
# 7   P008      F    NaN   FS
# 8   P009      M     PT  NaN
# 10  P011      M    NaN  AWS

# nothing changed :
# df.loc[df['salary'] >= 100, 'status'].fillna(df.loc[df['salary'] >= 100, 'status'].mode()[0], inplace=True)
# df.loc[df['salary'] < 100, 'status'].fillna(df.loc[df['salary'] < 100, 'status' ].mode()[0], inplace=True)
# print(df)
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

df.loc[df["salary"]>=100, "status"] = df.loc[df["salary"]>=100, "status"].fillna(df.loc[df["salary"]>=100, "status"].mode()[0])
df.loc[df["salary"]<100, "status"] = df.loc[df["salary"]<100, "status"].fillna(df.loc[df["salary"]<100, "status"].mode()[0])
# print(df)
#       id gender status dept  var1  var2  salary
# 0   P001      M     FT   DS   2.0   8.0     NaN
# 1   P002      F     PT   FS   3.0   NaN    54.0
# 2   P003      M     PT  AWS   5.0   5.0    59.0
# 3   P004      F     FT  AWS   NaN   8.0   120.0
# 4   P005      M     PT   DS   7.0  11.0    58.0
# 5   P006      F     PT  NaN   1.0   NaN    75.0
# 6   P007      M     FT   FS   NaN   NaN     NaN
# 7   P008      F     FT   FS  10.0   2.0   136.0
# 8   P009      M     PT  NaN  14.0   3.0    60.0
# 9   P010      F     FT   DS   NaN   7.0   125.0
# 10  P011      M    NaN  AWS   6.0   9.0     NaN

# print(df.groupby(['gender','dept'])['status'].apply(lambda x : x.mode()[0]))
# gender  dept
# F       AWS     FT
#         DS      FT
#         FS      FT
# M       AWS     PT
#         DS      FT
#         FS      FT
# Name: status, dtype: object

# print(df.groupby(['gender', 'dept'])['status'].transform(lambda x : x.mode()[0]))
# 0     FT
# 1     FT
# 2     PT
# 3     FT
# 4     FT
# 6     FT
# 7     FT
# 9     FT
# 10    PT
# Name: status, dtype: object

#  XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# df['trans_status'] didn't accept the new assigned data. look at it again.
df['trans_status'] = df.groupby(['gender', 'dept'])['status'].transform(lambda x : x.mode()[0])
# print(df)
#       id gender status dept  var1  var2  salary trans_status
# 0   P001      M     FT   DS   2.0   8.0     NaN           FT
# 1   P002      F     PT   FS   3.0   NaN    54.0           FT
# 2   P003      M     PT  AWS   5.0   5.0    59.0           PT
# 3   P004      F     FT  AWS   NaN   8.0   120.0           FT
# 4   P005      M     PT   DS   7.0  11.0    58.0           FT
# 5   P006      F     PT  NaN   1.0   NaN    75.0          NaN
# 6   P007      M     FT   FS   NaN   NaN     NaN           FT
# 7   P008      F     FT   FS  10.0   2.0   136.0           FT
# 8   P009      M     PT  NaN  14.0   3.0    60.0          NaN
# 9   P010      F     FT   DS   NaN   7.0   125.0           FT
# 10  P011      M    NaN  AWS   6.0   9.0     NaN           PT

df["status"].fillna(df.groupby(["gender", "dept"])["status"].transform(lambda x : x.mode()[0]), inplace=True)
# print(df)
#       id gender status dept  var1  var2  salary trans_status
# 0   P001      M     FT   DS   2.0   8.0     NaN           FT
# 1   P002      F     PT   FS   3.0   NaN    54.0           FT
# 2   P003      M     PT  AWS   5.0   5.0    59.0           PT
# 3   P004      F     FT  AWS   NaN   8.0   120.0           FT
# 4   P005      M     PT   DS   7.0  11.0    58.0           FT
# 5   P006      F     PT  NaN   1.0   NaN    75.0          NaN
# 6   P007      M     FT   FS   NaN   NaN     NaN           FT
# 7   P008      F     FT   FS  10.0   2.0   136.0           FT
# 8   P009      M     PT  NaN  14.0   3.0    60.0          NaN
# 9   P010      F     FT   DS   NaN   7.0   125.0           FT
# 10  P011      M     PT  AWS   6.0   9.0     NaN           PT

# print(df.groupby("dept")["salary"].mean())
# dept
# AWS    89.5
# DS     91.5
# FS     95.0
# Name: salary, dtype: float64

# print(df.groupby("dept")["salary"].transform("mean"))
# 0     91.5
# 1     95.0
# 2     89.5
# 3     89.5
# 4     91.5
# 5      NaN
# 6     95.0
# 7     95.0
# 8      NaN
# 9     91.5
# 10    89.5
# Name: salary, dtype: float64

# print(df.groupby(["status", "dept"])["salary"].mean())
# status  dept
# FT      AWS     120.0
#         DS      125.0
#         FS      136.0
# PT      AWS      59.0
#         DS       58.0
#         FS       54.0
# Name: salary, dtype: float64

# print(df.groupby(["status", "dept"])["salary"].transform("mean"))
# 0     125.0
# 1      54.0
# 2      59.0
# 3     120.0
# 4      58.0
# 5       NaN
# 6     136.0
# 7     136.0
# 8       NaN
# 9     125.0
# 10     59.0
# Name: salary, dtype: float64

df["trans_salary"] = df.groupby(["status","dept"])["salary"].transform("mean")
# print(df)
#       id gender status dept  var1  var2  salary trans_status  trans_salary
# 0   P001      M     FT   DS   2.0   8.0     NaN           FT         125.0
# 1   P002      F     PT   FS   3.0   NaN    54.0           FT          54.0
# 2   P003      M     PT  AWS   5.0   5.0    59.0           PT          59.0
# 3   P004      F     FT  AWS   NaN   8.0   120.0           FT         120.0
# 4   P005      M     PT   DS   7.0  11.0    58.0           FT          58.0
# 5   P006      F     PT  NaN   1.0   NaN    75.0          NaN           NaN
# 6   P007      M     FT   FS   NaN   NaN     NaN           FT         136.0
# 7   P008      F     FT   FS  10.0   2.0   136.0           FT         136.0
# 8   P009      M     PT  NaN  14.0   3.0    60.0          NaN           NaN
# 9   P010      F     FT   DS   NaN   7.0   125.0           FT         125.0
# 10  P011      M     PT  AWS   6.0   9.0     NaN           PT          59.0

df["salary"].fillna(df.groupby(["status","dept"])["salary"].transform("mean"), inplace=True)
# print(df)
#       id gender status dept  var1  var2  salary trans_status  trans_salary
# 0   P001      M     FT   DS   2.0   8.0   125.0           FT         125.0
# 1   P002      F     PT   FS   3.0   NaN    54.0           FT          54.0
# 2   P003      M     PT  AWS   5.0   5.0    59.0           PT          59.0
# 3   P004      F     FT  AWS   NaN   8.0   120.0           FT         120.0
# 4   P005      M     PT   DS   7.0  11.0    58.0           FT          58.0
# 5   P006      F     PT  NaN   1.0   NaN    75.0          NaN           NaN
# 6   P007      M     FT   FS   NaN   NaN   136.0           FT         136.0
# 7   P008      F     FT   FS  10.0   2.0   136.0           FT         136.0
# 8   P009      M     PT  NaN  14.0   3.0    60.0          NaN           NaN
# 9   P010      F     FT   DS   NaN   7.0   125.0           FT         125.0
# 10  P011      M     PT  AWS   6.0   9.0    59.0           PT          59.0

######### Filling with interpolation ######################
flights = sns.load_dataset('flights')
# print(flights)
#      year month  passengers
# 0    1949   Jan         112
# 1    1949   Feb         118
# 2    1949   Mar         132
# 3    1949   Apr         129
# 4    1949   May         121
# ..    ...   ...         ...
# 139  1960   Aug         606
# 140  1960   Sep         508
# 141  1960   Oct         461
# 142  1960   Nov         390
# 143  1960   Dec         432
#
# [144 rows x 3 columns]

# print(flights.isnull().sum())
# year          0
# month         0
# passengers    0
# dtype: int64

flights['passengers'].plot()
# plt.show()

flights_copy = flights.copy()
flights_copy.loc[np.random.randint(1, 144, 20), 'passengers']=None
# print(flights_copy.isnull().sum())
# year           0
# month          0
# passengers    20
# dtype: int64

flights_copy['passengers'].plot()
# plt.show()

flights_copy['passengers'].interpolate().plot()
# plt.show()

flights['passengers'].plot()
# plt.show()

# ------------------------------------------------------------