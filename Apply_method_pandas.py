import  pandas as pd
import numpy as np

train= pd.read_csv('http://bit.ly/kaggletrain')
print(train.head())
#  PassengerId  Survived  Pclass  ...     Fare Cabin  Embarked
# 0            1         0       3  ...   7.2500   NaN         S
# 1            2         1       1  ...  71.2833   C85         C
# 2            3         1       3  ...   7.9250   NaN         S
# 3            4         1       1  ...  53.1000  C123         S
# 4            5         0       3  ...   8.0500   NaN         S
# [5 rows x 12 columns]

#################################################################
# MAP METHOD:
# You can add a new column to a dataframe similar with dictionaries with map function.
# dataframe_name[new_name] = dataframe_name[existing_column_name].map({'value_1'=0, 'value_2'=1})
train['Sex_num'] = train['Sex'].map({'female':0, 'male':1})
# print(train.loc[0:4, ['Sex', 'Sex_num']])
#       Sex  Sex_num
# 0    male        1
# 1  female        0
# 2  female        0
# 3  female        0
# 4    male        1

#################################################################
# APPLY METHOD:
# Apply is both for series and dataframe method.
# apply(use function without a parenthesis: len ) a function each element in a series.
train['Name_length'] = train['Name'].apply(len)
# print(train.loc[0:4, ['Name', 'Name_length']])
#
#                                                 Name  Name_length
# 0                            Braund, Mr. Owen Harris           23
# 1  Cumings, Mrs. John Bradley (Florence Briggs Th...           51
# 2                             Heikkinen, Miss. Laina           22
# 3       Futrelle, Mrs. Jacques Heath (Lily May Peel)           44
# 4                           Allen, Mr. William Henry           24

#----------------------------------------------------------

# You can use it with a numpy function
train['Fare_ceil'] = train['Fare'].apply(np.ceil)
# print(train.loc[0:4, ['Fare', 'Fare_ceil']])
#       Fare  Fare_ceil
# 0   7.2500        8.0
# 1  71.2833       72.0
# 2   7.9250        8.0
# 3  53.1000       54.0
# 4   8.0500        9.0

#----------------------------------------------------------

def get_element(my_list, position):
    return my_list[position]

# you can't use the function's double brackets inside the apply method .
# So you can add after comma , (position) . Not inside the function.
# print(train['Name'].str.split(",").apply(get_element, position=0).head())
# 0       Braund
# 1      Cumings
# 2    Heikkinen
# 3     Futrelle
# 4        Allen
# Name: Name, dtype: object

#----------------------------------------------------------

# Also you can use lambda function like this :
# print(train['Name'].str.split(",").apply(lambda x: x[0]).head() )
# 0       Braund
# 1      Cumings
# 2    Heikkinen
# 3     Futrelle
# 4        Allen
# Name: Name, dtype: object

#################################################################

# Let's try dataframe apply method :

drinks = pd.read_csv('http://bit.ly/drinksbycountry')
print(drinks.head())
#        country  beer_servings  ...  total_litres_of_pure_alcohol  continent
# 0  Afghanistan              0  ...                           0.0       Asia
# 1      Albania             89  ...                           4.9     Europe
# 2      Algeria             25  ...                           0.7     Africa
# 3      Andorra            245  ...                          12.4     Europe
# 4       Angola            217  ...                           5.9     Africa
#
# [5 rows x 6 columns]

#----------------------------------------------------------
# Lets get the our dataframe that we need and use the apply method:
# The axis means below is the direction for the function.
# If axis is 0 : to the right wise, 1 is for downstream.
a=drinks.loc[:, 'beer_servings': 'wine_servings'].apply(max, axis=0)
# # print(a)
# [5 rows x 6 columns]
# beer_servings      376
# spirit_servings    438
# wine_servings      370
# dtype: int64

#----------------------------------------------------------

b = drinks.loc[:, 'beer_servings':'wine_servings'].apply(max, axis=1).head()
# print(b)
# 0      0
# 1    132
# 2     25
# 3    312
# 4    217
# dtype: int64

#----------------------------------------------------------

c = drinks.loc[:, 'beer_servings':'wine_servings'].apply(np.argmax, axis=1).head()
print(c)
# 0    0
# 1    1
# 2    0
# 3    2
# 4    0
# dtype: int64

#################################################################

# APPLY MAP :
#  It is a dataframe method
# Apply a function to every element in a dataframe.

drinks.loc[:, 'beer_servings': 'wine_servings'] = \
drinks.loc[:, 'beer_servings': 'wine_servings'].applymap(float)
print(drinks.head())

#        country  beer_servings  ...  total_litres_of_pure_alcohol  continent
# 0  Afghanistan            0.0  ...                           0.0       Asia
# 1      Albania           89.0  ...                           4.9     Europe
# 2      Algeria           25.0  ...                           0.7     Africa
# 3      Andorra          245.0  ...                          12.4     Europe
# 4       Angola          217.0  ...                           5.9     Africa
#
# [5 rows x 6 columns]





