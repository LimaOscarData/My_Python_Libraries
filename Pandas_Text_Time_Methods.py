import re

import numpy as np
import pandas as pd
import seaborn as sns

df = pd.read_excel('/Users/oscar/Desktop/My_Python_Libraries/text_exercise.XLSX')
# print(df)
#       id          staff department                 job       salary age
# 0  M0001       Tom BLUE         HR             manager   "$150,000"  52
# 1  M0002     JOHN BLACK         IT             manager   "$180,000"  48
# 2  E0001  Micheal Brown         IT      data scientist   "$150,000"  35
# 3  E0002   jason walker         HR           recruiter  130000dolar  38
# 4  E0003     Alex Green         IT   backend developer   "$110,000"   -
# 5  E0004    OSCAR SMİTH         IT  frontend developer   "$120,000"  32
# 6  E0005    Adrian STAR         IT      data scientist   "$135,000"  40
# 7  E0006   Albert simon         IT      data scientist  125000dolar  35

# print(df.info())
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 8 entries, 0 to 7
# Data columns (total 6 columns):
#  #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
#  0   id          8 non-null      object
#  1   staff       8 non-null      object
#  2   department  8 non-null      object
#  3   job         8 non-null      object
#  4   salary      8 non-null      object
#  5   age         8 non-null      object
# dtypes: object(6)
# memory usage: 512.0+ bytes
# None

#------------------------------------------------------------------------------------------------
# some explanations :
# lower() => Converts a string into lower case
# upper() => Converts a string into upper case
# capitalize() => Converts the first character to upper case
# title() => Converts the first character of each word to upper case
# swapcase() => Swaps the case lower/upper

# this is python built-in lower:
# print('steve'.lower())
# steve

# this is for series in pandas :
# print(df['staff'].str.lower())
# 0         tom blue
# 1       john black
# 2    micheal brown
# 3     jason walker
# 4       alex green
# 5     oscar smi̇th
# 6      adrian star
# 7     albert simon
# Name: staff, dtype: object

# also you can use it for srt.upper(), str.title(), str.capitalize(), str.swapcase().

#------------------------------------------------------------------------------------------------
# isalpha() => Returns True if all characters in the string are in the alphabet
# isnumeric() => Returns True if all characters in the string are numeric
# isalnum() => Returns True if all characters in the string are alphanumeric
# endswith() => Returns true if the string ends with the specified value
# startswith() => Returns true if the string starts with the specified value
# contains() => Returns a Boolean value True for each element if the substring contains in the element, else False.

# print(df)
#       id          staff department                 job       salary age
# 0  M0001       Tom BLUE         HR             manager   "$150,000"  52
# 1  M0002     JOHN BLACK         IT             manager   "$180,000"  48
# 2  E0001  Micheal Brown         IT      data scientist   "$150,000"  35
# 3  E0002   jason walker         HR           recruiter  130000dolar  38
# 4  E0003     Alex Green         IT   backend developer   "$110,000"   -
# 5  E0004    OSCAR SMİTH         IT  frontend developer   "$120,000"  32
# 6  E0005    Adrian STAR         IT      data scientist   "$135,000"  40
# 7  E0006   Albert simon         IT      data scientist  125000dolar  35

# print(df['job'].str.isalpha())
# 0     True
# 1     True
# 2    False
# 3     True
# 4    False
# 5    False
# 6    False
# 7    False
# Name: job, dtype: bool

# print(df['age'].str.isnumeric())
# 0      NaN
# 1      NaN
# 2      NaN
# 3      NaN
# 4    False
# 5      NaN
# 6      NaN
# 7      NaN
# Name: age, dtype: object
#
# it returns them as NaN but we need them as boolean.

# If the types are object we can't check them by using str.isnumeric() attribute :
# lets convert them to str initially .
# astype let us to convert an item to related type, in below example to str .
# print(df['age'].astype(str).str.isnumeric())
# 0     True
# 1     True
# 2     True
# 3     True
# 4    False
# 5     True
# 6     True
# 7     True
# Name: age, dtype: bool

# print(df['job'])
# 0               manager
# 1               manager
# 2        data scientist
# 3             recruiter
# 4     backend developer
# 5    frontend developer
# 6        data scientist
# 7        data scientist
# Name: job, dtype: object

# print(df['job'].str.startswith('data'))
# 0    False
# 1    False
# 2     True
# 3    False
# 4    False
# 5    False
# 6     True
# 7     True
# Name: job, dtype: bool

# Also you can use it with str.endswith("per"), str.contains("data"),


# print(df['salary'])
# 0     "$150,000"
# 1     "$180,000"
# 2     "$150,000"
# 3    130000dolar
# 4     "$110,000"
# 5     "$120,000"
# 6     "$135,000"
# 7    125000dolar
# Name: salary, dtype: object

# print(df['salary'].str.isalnum())
# 0    False
# 1    False
# 2    False
# 3     True
# 4    False
# 5    False
# 6    False
# 7     True
# Name: salary, dtype: bool

# if there is a any punctuation or sign inside the series, result will be deceptive.
# first of all we need to clean them .

# With using regex :
# It shows the results which contains a character a to z .
# print(df['salary'].str.contains(r'[a-z]'))
# 0    False
# 1    False
# 2    False
# 3     True
# 4    False
# 5    False
# 6    False
# 7     True
# Name: salary, dtype: bool

#------------------------------------------------------------------------------------------------
# We can use these string methods which returning boolean expression for creating condition and so selecting relative rows
# it returns the all rows which contains the 'data' inside the job's column :
# print(df[ df['job'].str.contains('data') ])
#       id          staff department             job       salary age
# 2  E0001  Micheal Brown         IT  data scientist   "$150,000"  35
# 6  E0005    Adrian STAR         IT  data scientist   "$135,000"  40
# 7  E0006   Albert simon         IT  data scientist  125000dolar  35


# let's change the value of another column's related rows which contains the True value :
df.loc[df['job'].str.contains('data'), 'department' ] = 'DS'
# print(df['department'])
# 0    HR
# 1    IT
# 2    DS
# 3    HR
# 4    IT
# 5    IT
# 6    DS
# 7    DS
# Name: department, dtype: object

# print(df.loc[])
















