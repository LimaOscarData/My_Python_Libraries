import pandas as pd
import numpy as np

data = pd.DataFrame({
    'age' :     [ 10, 22, 13, 21, 12, 11, 17],
    'section' : [ 'A', 'B', 'C', 'B', 'B', 'A', 'A'],
    'city' :    [ 'Gurgaon', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai', 'Delhi', 'Mumbai'],
    'gender' :  [ 'M', 'F', 'F', 'M', 'M', 'M', 'F'],
    'favourite_color' : [ 'red', 'blue', 'yellow', 'pink', 'black', 'green', 'red']
})
# print(data)
#    age section     city gender favourite_color
# 0   10       A  Gurgaon      M             red
# 1   22       B    Delhi      F            blue
# 2   13       C   Mumbai      F          yellow
# 3   21       B    Delhi      M            pink
# 4   12       B   Mumbai      M           black
# 5   11       A    Delhi      M           green
# 6   17       A   Mumbai      F             red

###########################
# How to select the column city ?
# print(data["city"])
# 0    Gurgaon
# 1      Delhi
# 2     Mumbai
# 3      Delhi
# 4     Mumbai
# 5      Delhi
# 6     Mumbai
# Name: city, dtype: object

###########################
# How can you remove the row 6  permanently?
# data.drop(index=6, inplace=True)
# data.drop(6, axis=0, inplace=True)
# print(data)
#    age section     city gender favourite_color
# 0   10       A  Gurgaon      M             red
# 1   22       B    Delhi      F            blue
# 2   13       C   Mumbai      F          yellow
# 3   21       B    Delhi      M            pink
# 4   12       B   Mumbai      M           black
# 5   11       A    Delhi      M           green

###########################
# change the index's names
data.index = "A B C D E F G".split(" ")
# print(data)
#    age section     city gender favourite_color
# A   10       A  Gurgaon      M             red
# B   22       B    Delhi      F            blue
# C   13       C   Mumbai      F          yellow
# D   21       B    Delhi      M            pink
# E   12       B   Mumbai      M           black
# F   11       A    Delhi      M           green
# G   17       A   Mumbai      F             red

###########################
# How to select the row B with iloc method as below?

# print(data.iloc[1])
# age                   22
# section                B
# city               Delhi
# gender                 F
# favourite_color     blue
# Name: B, dtype: object

###########################
# How to select the rows D and E together with columns city
# and gender with loc method as below?
# 	city	gender
# section
# D	Delhi	M
# E	Mumbai	M

# print(data.loc[["D","E"],["city", "gender"]])
# print(data.loc["D":"E","city": "gender"])
# print(data.loc["D":"E",["city", "gender"]])
# print(data.loc["D":"E",["city", "gender"]])
# print(data.loc[["D","E"],"city": "gender"])
#      city gender
# D   Delhi      M
# E  Mumbai      M

###########################
# How to select the rows D and E together with
# columns city and gender with iloc method as below?
# 	city	gender
# section
# D	Delhi	M
# E	Mumbai	M

# there are two options. first one is using []
# other one is using without [].
# if you are using [] you must use comma , .
# if you dont use the [] you must use colon : .
# main logic is you can use double comma , , , , .
# print(data.iloc[[3,4], [1,2]])
#   section    city
# D       B   Delhi
# E       B  Mumbai

# print(data.iloc[3:5, 1:3]) #if use [] use colon :, increase index 1
#   section    city
# D       B   Delhi
# E       B  Mumbai

# print(data.iloc[3:5, [1,2]]) #if use [] use colon :, increase index 1
#   section    city
# D       B   Delhi
# E       B  Mumbai

# print(data.iloc[[3,5], 1:3]) #if use [] use colon :, increase index 1
#   section   city
# D       B  Delhi
# F       A  Delhi

###########################
# How to select the rows D and E together with columns city and gender
# with iloc method as below?
# 	city	gender
# section
# D	Delhi	M
# E	Mumbai	M

# print(data.iloc[[3,4], [2,3]])
#      city gender
# D   Delhi      M
# E  Mumbai      M

# print(data.iloc[3:5, 2:4])
#      city gender
# D   Delhi      M
# E  Mumbai      M

# print(data.iloc[[3,4], 2:4])
#      city gender
# D   Delhi      M
# E  Mumbai      M

# print(data.iloc[3:5, [2,3]])
#      city gender
# D   Delhi      M
# E  Mumbai      M