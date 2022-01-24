import pandas as pd
import numpy as np
''' 
people_dict={"first":["Richard", "Robert", "Jason"],
             "last" :["Stone", "Deepdive", "Seaborn"],
             "email": ["richardstone@email.com", "robertdeepdive@email.com",
                        "jasonseaborn@email.com"]}
df=pd.DataFrame(people_dict)
print(df.iloc[[1,2]])
print(type(df.iloc[[1,2]]),"\n")
#     first      last                     email
# 1  Robert  Deepdive  robertdeepdive@email.com
# 2   Jason   Seaborn    jasonseaborn@email.com
# <class 'pandas.core.frame.DataFrame'> 

print(df.iloc[1,2])
print(type(df.iloc[1,2]))
# robertdeepdive@email.com
# <class 'str'>

'''

''' 
outside = ['A1','A1','A1','A2','A2','A2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
# print(hier_index)
# [('A1', 1), ('A1', 2), ('A1', 3), ('A2', 1), ('A2', 2), ('A2', 3)]

hier_index = pd.MultiIndex.from_tuples(hier_index)
# print(hier_index)
# MultiIndex([('A1', 1),
#             ('A1', 2),
#             ('A1', 3),
#             ('A2', 1),
#             ('A2', 2),
#             ('A2', 3)],
#            )

# print(type(hier_index))
# <class 'pandas.core.indexes.multi.MultiIndex'>

np.random.seed(101)
data = pd.DataFrame(np.random.randn(6,2),index=hier_index,columns=['X','Y'])
print(data)
#              X         Y
# A1 1  2.706850  0.628133
#    2  0.907969  0.503826
#    3  0.651118 -0.319318
# A2 1 -0.848077  0.605965
#    2 -2.018168  0.740122
#    3  0.528813 -0.589001

print(data.loc["A1"])
#           X         Y
# 1  2.706850  0.628133
# 2  0.907969  0.503826
# 3  0.651118 -0.319318

print(type(data.loc["A1"]))
# <class 'pandas.core.frame.DataFrame'>
'''

''' 
people_dict={"first":["Richard", "Robert", "Jason"],
             "last" :["Stone", "Deepdive", "Seaborn"],
             "email": ["richardstone@email.com", "robertdeepdive@email.com",
                        "jasonseaborn@email.com"]}
df=pd.DataFrame(people_dict)
print(df)
#      first      last                     email
# 0  Richard     Stone    richardstone@email.com
# 1   Robert  Deepdive  robertdeepdive@email.com
# 2    Jason   Seaborn    jasonseaborn@email.com

print(df["last"])
# 0       Stone
# 1    Deepdive
# 2     Seaborn
# Name: last, dtype: object

print(type(df["last"]))
# <class 'pandas.core.series.Series'>
'''

'''

data = pd.DataFrame({
    'age' :     [ 10, 22, 13, 21, 12, 11, 17],
    'section' : [ 'A', 'B', 'C', 'B', 'B', 'A', 'A'],
    'city' :    [ 'Gurgaon', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai'],
    'gender' :  [ 'M', 'F', 'F', 'M', 'M', 'M', 'F'],
    'favourite_color' : [ 'red', 'blue', 'yellow', 'pink', 'black', 'green', 'red']
})

print(data)
#    age section     city gender favourite_color
# 0   10       A  Gurgaon      M             red
# 1   22       B    Delhi      F            blue
# 2   13       C   Mumbai      F          yellow
# 3   21       B    Delhi      M            pink
# 4   12       B   Mumbai      M           black
# 5   11       A    Delhi      M           green
# 6   17       A   Mumbai      F             red



# print(data["city", "age"])
# KeyError: ('city', 'age')

# print(data[["city", "age"]])
# print(type(data[["city", "age"]]))
# <class 'pandas.core.frame.DataFrame'>
#       city  age
# 0  Gurgaon   10
# 1    Delhi   22
# 2   Mumbai   13
# 3    Delhi   21
# 4   Mumbai   12
# 5    Delhi   11
# 6   Mumbai   17

# print(data[["city" and "age"]])
# print(type(data[["city" and "age"]]))
# <class 'pandas.core.frame.DataFrame'>
#    age
# 0   10
# 1   22
# 2   13
# 3   21
# 4   12
# 5   11
# 6   17

data.index = "A B C D E F G".split(" ")
print(data)
#    age section     city gender favourite_color
# A   10       A  Gurgaon      M             red
# B   22       B    Delhi      F            blue
# C   13       C   Mumbai      F          yellow
# D   21       B    Delhi      M            pink
# E   12       B   Mumbai      M           black
# F   11       A    Delhi      M           green
# G   17       A   Mumbai      F             red

# print(data.loc["B"])
# age                   22
# section                B
# city               Delhi
# gender                 F
# favourite_color     blue
# Name: B, dtype: object

# print(data.loc[["B"]])
#    age section   city gender favourite_color
# B   22       B  Delhi      F            blue

# print(data.iloc[1])
# age                   22
# section                B
# city               Delhi
# gender                 F
# favourite_color     blue
# Name: B, dtype: object

# data.columns = ["column_1", "column_2", "column_3", "column_4", "column_5"]
# print(data)
#    column_1 column_2 column_3 column_4 column_5
# A        10        A  Gurgaon        M      red
# B        22        B    Delhi        F     blue
# C        13        C   Mumbai        F   yellow
# D        21        B    Delhi        M     pink
# E        12        B   Mumbai        M    black
# F        11        A    Delhi        M    green
# G        17        A   Mumbai        F      red

'''