import pandas as pd
import matplotlib.pyplot as plt

drinks = pd.read_csv('http://bit.ly/drinksbycountry')
print(drinks.head(), "\n"*3) # I used *3 for seperating head of dataset.

#        country  beer_servings  ...  total_litres_of_pure_alcohol  continent
# 0  Afghanistan              0  ...                           0.0       Asia
# 1      Albania             89  ...                           4.9     Europe
# 2      Algeria             25  ...                           0.7     Africa
# 3      Andorra            245  ...                          12.4     Europe
# 4       Angola            217  ...                           5.9     Africa
#
# [5 rows x 6 columns]

###########################################################
#  lets calculate the mean beer service of entire dataset

# print(drinks['beer_servings'].mean())
# or you can do that :
# print(drinks.beer_servings.mean()) but do not use it. because:
# 1 ) With brackets you can select multiple columns (e.g., df[['col1', 'col2']]) or add
# a new column (df['newcol'] = ...), which can't be done with dot access.
# 2 ) accessing a single column with a simple name, but you can do more with the bracket notation.
# 3 ) You can only use df.col if the column name is a valid Python identifier, be careful.

# 106.16062176165804

###########################################################
# lets calculate the mean beer servings only for African countries
# print(drinks[drinks["continent"] == "Africa"]["beer_servings"].mean())
# 61.471698113207545

###########################################################
# lets calculate the mean of beer servings of each continent
# print(drinks.groupby("continent")["beer_servings"].mean())
# continent
# Africa            61.471698
# Asia              37.045455
# Europe           193.777778
# North America    145.434783
# Oceania           89.687500
# South America    175.083333
# Name: beer_servings, dtype: float64

# print(drinks.groupby("continent")[["beer_servings"]].mean()) #or making it dataframe
# continent
# Africa             61.471698
# Asia               37.045455
# Europe            193.777778
# North America     145.434783
# Oceania            89.687500
# South America     175.083333
###########################################################
#  using aggregation function with group by
# print(drinks.groupby('continent')['beer_servings'].min())
# continent
# Africa            0
# Asia              0
# Europe            0
# North America     1
# Oceania           0
# South America    93
# Name: beer_servings, dtype: int64

# we can use multiple agg functions
# print(drinks.groupby('continent')['beer_servings'].agg(['count','sum','max', 'min']))
#                count   sum  max  min
# continent
# Africa            53  3258  376    0
# Asia              44  1630  247    0
# Europe            45  8720  361    0
# North America     23  3345  285    1
# Oceania           16  1435  306    0
# South America     12  2101  333   93

###########################################################
print(drinks.groupby('continent').mean())
#                beer_servings  ...  total_litres_of_pure_alcohol
# continent                     ...
# Africa             61.471698  ...                      3.007547
# Asia               37.045455  ...                      2.170455
# Europe            193.777778  ...                      8.617778
# North America     145.434783  ...                      5.995652
# Oceania            89.687500  ...                      3.381250
# South America     175.083333  ...                      6.308333
#
# [6 rows x 4 columns]

###########################################################
# lets use plots
drinks.groupby('continent').mean().plot(kind= 'bar')
plt.show()
###########################################################









