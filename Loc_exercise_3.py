import pandas as pd
import numpy as np

# data = pd.DataFrame({
#     'age' :     [ 10, 22, 13, 21, 12, 11, 17],
#     'section' : [ 'A', 'B', 'C', 'D', 'E', 'F', 'G'],
#     'country' : [ 'USA', 'GBR', 'TUR', 'NLD', 'BEL', 'DEU', 'FRA'],
#     'gender' :  [ 'M', 'F', 'F', 'M', 'M', 'M', 'F'],
#     'favourite_color' : [ 'red', 'blue', 'yellow', 'pink', 'black', 'green', 'red']
# })
# data.set_index('section', inplace=True)
# print(data)
#          age country gender favourite_color
# section
# A         10     USA      M             red
# B         22     GBR      F            blue
# C         13     TUR      F          yellow
# D         21     NLD      M            pink
# E         12     BEL      M           black
# F         11     DEU      M           green
# G         17     FRA      F             red

#####################################
# How to select the rows where ages are greater than 15 as below?
# print(data[data["age"] > 15])
#          age country gender favourite_color
# section
# B         22     GBR      F            blue
# D         21     NLD      M            pink
# G         17     FRA      F             red

#####################################
# How to select the country column where ages are greater than 15 as below?
# print(data[data["age"] > 15 ]["country"]) # series
# section
# B    GBR
# D    NLD
# G    FRA
# Name: country, dtype: object

# print(data[data["age"] > 15 ][["country"]]) # dataframe
#         country
# section
# B           GBR
# D           NLD
# G           FRA

#####################################
# How to select the rows where the favourite_colurs are red and the
# ages are greater than 15 as below?
# print(data[(data["favourite_color"] == "red") & (data["age"] > 15)] )
#          age country gender favourite_color
# section
# G         17     FRA      F             red

#####################################
# How many rows do you get if you return the following code?
# data[(data['age']>20) | (data['favourite_color'] == 'red')]
# print(data[(data['age']>20) | (data['favourite_color'] == 'red')])
#          age country gender favourite_color
# section
# A         10     USA      M             red
# B         22     GBR      F            blue
# D         21     NLD      M            pink
# G         17     FRA      F             red

#####################################
outside = ['A1','A1','A1','A2','A2','A2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)
np.random.seed(101)
data = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['X','Y'])
print(data)

# The Multi-Indexed DataFrame data is given above. How to get the following output?
# 1    0.605965
# 2    0.740122
# 3   -0.589001

# print(data.loc["A2","Y"])
# 1    0.605965
# 2    0.740122
# 3   -0.589001
# Name: Y, dtype: float64

# print(data.loc[["A2","Y"]])
# KeyError: "['Y'] not in index"

# print(data.loc[["A2"],"Y"])
# A2  1    0.605965
#     2    0.740122
#     3   -0.589001
# Name: Y, dtype: float64

# print(data.loc["A2",["Y"]]) # dataframe
#           Y
# 1  0.605965
# 2  0.740122
# 3 -0.589001

# print(data["A2"]["Y"])
# KeyError: 'A2'

# print(data["Y"]["A2"])
# 1    0.605965
# 2    0.740122
# 3   -0.589001
# Name: Y, dtype: float64

# data.loc['A1','X'] and data['X']['A1'] both outputs the same result.
#####################################
# The Multi-Indexed DataFrame data is given above. How to get the following output?
# 0.605965
# print(data.loc["A2"].loc[1,"Y"])
# 0.6059653494949336

# selecting only A2 row:
# print(data.loc["A2"])
#           X         Y
# 1 -0.848077  0.605965
# 2 -2.018168  0.740122
# 3  0.528813 -0.589001
#####################################
