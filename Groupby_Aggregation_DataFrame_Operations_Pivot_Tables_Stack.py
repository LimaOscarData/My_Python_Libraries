import numpy as np
import pandas as pd
import seaborn as sns

#############################################################################
######################### Basic aggregation methods #########################
#############################################################################


# np.random.seed(42)
# df = pd.DataFrame(np.random.randint(0,100,size=(7,5)),
#                   columns=["x1","x2","x3","x4","x5"])
# print(df)
#    x1  x2  x3  x4  x5
# 0  51  92  14  71  60
# 1  20  82  86  74  74
# 2  87  99  23   2  21
# 3  52   1  87  29  37
# 4   1  63  59  20  32
# 5  75  57  21  88  48
# 6  90  58  41  91  59
# ------------------------------------------------------------

# counts of columns' sum
# print(df.count())
# x1    7
# x2    7
# x3    7
# x4    7
# x5    7
# dtype: int64
# ------------------------------------------------------------

# count of selected column:
# print(df['x1'].count())
# 7

# ------------------------------------------------------------

# mean of all columns' means :
# print(df.mean())
# x1    53.714286
# x2    64.571429
# x3    47.285714
# x4    53.571429
# x5    47.285714
# dtype: float64

# ------------------------------------------------------------

# mean of selected column x2:
# print(df['x2'].mean())
# 64.57142857142857

# ------------------------------------------------------------

# median of all columns :
# print(df.median())
# x1    52.0
# x2    63.0
# x3    41.0
# x4    71.0
# x5    48.0
# dtype: float64

# ------------------------------------------------------------

# min values of all columns:
# print(df.min())
# x1     1
# x2     1
# x3    14
# x4     2
# x5    21
# dtype: int64

# ------------------------------------------------------------

# position of all columns max value :
# print(df.idxmax())
# x1    6
# x2    2
# x3    3
# x4    6
# x5    1
# dtype: int64

#df.argmax() gives an error , because it only works with series.

# ------------------------------------------------------------

# position of selected columns' max value :
# print(df["x3"].idxmax())
# 3

# ------------------------------------------------------------

# Return int position of the {value} value in the Series
# print(df["x2"].argmax())
# 2

# ------------------------------------------------------------

# std deviation of all columns :
# print(df.std())
# x1    33.673502
# x2    32.623392
# x3    30.663302
# x4    35.818325
# x5    18.454577
# dtype: float64

# ------------------------------------------------------------

# sum function works with single selected column.
# print(df['x1'].std())
# 33.67350237062907

# if you use it with double brackets it returns a series
# print(df[['x1']].std())
# x1    33.673502
# dtype: float64

# If you want to find selected two or more columns std deviation
# you must use double brackets [] .
# print(df[["x1", "x2"]].std())
# x1    33.673502
# x2    32.623392
# dtype: float64

# if you use sum with a single square brackets gives key error
# print(df["x1", "x2"].std())
# key error

# ------------------------------------------------------------

# print(df.var())
# x1    1133.904762
# x2    1064.285714
# x3     940.238095
# x4    1282.952381
# x5     340.571429
# dtype: float64

# ------------------------------------------------------------

# if you want take df.var() as a dataframe you must use
# pd.dataframe .

# print(pd.DataFrame(df.var()))
#               0
# x1  1133.904762
# x2  1064.285714
# x3   940.238095
# x4  1282.952381
# x5   340.571429

# ------------------------------------------------------------

# if you want to take sums of columns sum use axis=0
# print(df.sum(axis=0))
# x1    376
# x2    452
# x3    331
# x4    375
# x5    331
# dtype: int64

# it gives rows sum, axis=1.
# print(df.sum(axis=1))
# 0    288
# 1    336
# 2    232
# 3    206
# 4    175
# 5    289
# 6    339
# dtype: int64

# explanation of axis' directions :
# →→ a x i s - 1 →→→→→→→→→→→
# ↓
# ↓       x1  x2  x3  x4  x5
# a    0  51  92  14  71  60
# x    1  20  82  86  74  74
# i    2  87  99  23   2  21
# s    3  52   1  87  29  37
# -    4   1  63  59  20  32
# 0    5  75  57  21  88  48
#      6  90  58  41  91  59
# ↓
# ↓



#############################################################################
########################### Groupby & Aggregation ###########################
#############################################################################

########################### DataFrame.groupby() ###########################
# The groupby method allows you to group rows of data together and call
# aggregate functions
#
# Now you can use the .groupby() method to group rows together based off
# of a column name. This will create a DataFrameGroupBy object:

# df=sns.load_dataset('iris')
# print(df)
#      sepal_length  sepal_width  petal_length  petal_width    species
# 0             5.1          3.5           1.4          0.2     setosa
# 1             4.9          3.0           1.4          0.2     setosa
# 2             4.7          3.2           1.3          0.2     setosa
# 3             4.6          3.1           1.5          0.2     setosa
# 4             5.0          3.6           1.4          0.2     setosa
# ..            ...          ...           ...          ...        ...
# 145           6.7          3.0           5.2          2.3  virginica
# 146           6.3          2.5           5.0          1.9  virginica
# 147           6.5          3.0           5.2          2.0  virginica
# 148           6.2          3.4           5.4          2.3  virginica
# 149           5.9          3.0           5.1          1.8  virginica
#
# [150 rows x 5 columns]
# ------------------------------------------------------------

# print(df.groupby('species'))
# <pandas.core.groupby.generic.DataFrameGroupBy object at 0x10523e110>

# ------------------------------------------------------------

# groupby a column and find the mean of same rows' values
# print(df.groupby('species').mean())
#             sepal_length  sepal_width  petal_length  petal_width
# species
# setosa             5.006        3.428         1.462        0.246
# versicolor         5.936        2.770         4.260        1.326
# virginica          6.588        2.974         5.552        2.026
# ------------------------------------------------------------

# print(df.groupby('species').describe())
#            sepal_length                               ... petal_width
#                   count   mean       std  min    25%  ...         min  25%  50%  75%  max
# species                                               ...
# setosa             50.0  5.006  0.352490  4.3  4.800  ...         0.1  0.2  0.2  0.3  0.6
# versicolor         50.0  5.936  0.516171  4.9  5.600  ...         1.0  1.2  1.3  1.5  1.8
# virginica          50.0  6.588  0.635880  4.9  6.225  ...         1.4  1.8  2.0  2.3  2.5
#
# [3 rows x 32 columns]
# ------------------------------------------------------------

# print(df.groupby('species').describe().T)
# species                setosa  versicolor  virginica
# sepal_length count  50.000000   50.000000  50.000000
#              mean    5.006000    5.936000   6.588000
#              std     0.352490    0.516171   0.635880
#              min     4.300000    4.900000   4.900000
#              25%     4.800000    5.600000   6.225000
#              50%     5.000000    5.900000   6.500000
#              75%     5.200000    6.300000   6.900000
#              max     5.800000    7.000000   7.900000
# sepal_width  count  50.000000   50.000000  50.000000
#              mean    3.428000    2.770000   2.974000
#              std     0.379064    0.313798   0.322497
#              min     2.300000    2.000000   2.200000
#              25%     3.200000    2.525000   2.800000
#              50%     3.400000    2.800000   3.000000
#              75%     3.675000    3.000000   3.175000
#              max     4.400000    3.400000   3.800000
# petal_length count  50.000000   50.000000  50.000000
#              mean    1.462000    4.260000   5.552000
#              std     0.173664    0.469911   0.551895
#              min     1.000000    3.000000   4.500000
#              25%     1.400000    4.000000   5.100000
#              50%     1.500000    4.350000   5.550000
#              75%     1.575000    4.600000   5.875000
#              max     1.900000    5.100000   6.900000
# petal_width  count  50.000000   50.000000  50.000000
#              mean    0.246000    1.326000   2.026000
#              std     0.105386    0.197753   0.274650
#              min     0.100000    1.000000   1.400000
#              25%     0.200000    1.200000   1.800000
#              50%     0.200000    1.300000   2.000000
#              75%     0.300000    1.500000   2.300000
#              max     0.600000    1.800000   2.500000

# ------------------------------------------------------------

# print(df.groupby('species')['sepal_length'].sum())
# species
# setosa        250.3
# versicolor    296.8
# virginica     329.4
# Name: sepal_length, dtype: float64
# ------------------------------------------------------------

# making it dataframe
# print(df.groupby('species')[['sepal_length']].sum())
#             sepal_length
# species
# setosa             250.3
# versicolor         296.8
# virginica          329.4
# ------------------------------------------------------------

# The meaning of "keys" is the column .
# You can add multiple columns, but you must use double square brackets
# it gives the result with a feature warning.
# print(df.groupby('species')['sepal_length', 'sepal_width'].sum())
#             sepal_length  sepal_width
# species
# setosa             250.3        171.4
# versicolor         296.8        138.5
# virginica          329.4        148.7
# FutureWarning: Indexing with multiple keys (implicitly converted
# to a tuple of keys) will be deprecated, use a list instead

# print(df.groupby('species')[['sepal_length', 'sepal_width']].sum())
#             sepal_length  sepal_width
# species
# setosa             250.3        171.4
# versicolor         296.8        138.5
# virginica          329.4        148.7
# ------------------------------------------------------------

data = {'Company':['GOOG', 'GOOG', 'MSFT', 'MSFT', 'GOOG', 'MSFT', 'GOOG', 'MSFT'],
        'Department':['HR', 'IT', 'IT', 'HR', 'HR', 'IT', 'IT', 'HR'],
        'Person':['Sam', 'Charlie', 'Amy', 'Vanessa', 'Carl', 'Sarah', 'Tom', 'Terry'],
        'Age':[30, 28, 35, 40, 42, 25, 32, 48],
        'Sales':[200, 120, 340, 124, 243, 350, 180, 220]}
df1 = pd.DataFrame(data)
print(df1)
#   Company Department   Person  Age  Sales
# 0    GOOG         HR      Sam   30    200
# 1    GOOG         IT  Charlie   28    120
# 2    MSFT         IT      Amy   35    340
# 3    MSFT         HR  Vanessa   40    124
# 4    GOOG         HR     Carl   42    243
# 5    MSFT         IT    Sarah   25    350
# 6    GOOG         IT      Tom   32    180
# 7    MSFT         HR    Terry   48    220
# ------------------------------------------------------------

# print(df1.groupby('Company').mean())
#           Age   Sales
# Company
# GOOG     33.0  185.75
# MSFT     37.0  258.50
# ------------------------------------------------------------

# print(df1.groupby('Company')['Sales'].mean())
# Company
# GOOG    185.75
# MSFT    258.50
# Name: Sales, dtype: float64

# lets make it df :
# print(df1.groupby('Company')[['Sales']].mean())
#           Sales
# Company
# GOOG     185.75
# MSFT     258.50
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
# ------------------------------------------------------------