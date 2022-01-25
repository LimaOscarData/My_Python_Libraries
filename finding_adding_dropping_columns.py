import pandas as pd
import  numpy as np

''' 
people_dict={"first":["Richard", "Robert", "Jason"],
             "last" :["Stone", "Deepdive", "Seaborn"],
             "email": ["richardstone@email.com", "robertdeepdive@email.com",
                        "jasonseaborn@email.com"]}
df=pd.DataFrame(people_dict)
print(df,"\n")
#      first      last                     email
# 0  Richard     Stone    richardstone@email.com
# 1   Robert  Deepdive  robertdeepdive@email.com
# 2    Jason   Seaborn    jasonseaborn@email.com 

# What is the output of the code below?
# df[(df['first']=="Richard") | (df['last'] == 'Deepdive')]
print(df[(df['first']=="Richard") | (df['last'] == 'Deepdive')])
#      first      last                     email
# 0  Richard     Stone    richardstone@email.com
# 1   Robert  Deepdive  robertdeepdive@email.com
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

# Try to find the rows where the value of age is greater than or equal to 21.
print(data[(data["age"] >= 21)])
#    age section   city gender favourite_color
# 1   22       B  Delhi      F            blue
# 3   21       B  Delhi      M            pink

# How to add a new column (column new ) using the first two chars of the column city ?
data["new"] = data["city"].str[:2]
print(data)
#    age section     city gender favourite_color new
# 0   10       A  Gurgaon      M             red  Gu
# 1   22       B    Delhi      F            blue  De
# 2   13       C   Mumbai      F          yellow  Mu
# 3   21       B    Delhi      M            pink  De
# 4   12       B   Mumbai      M           black  Mu
# 5   11       A    Delhi      M           green  De
# 6   17       A   Mumbai      F             red  Mu

# How to set the column section as the index as below?
data.set_index("section", inplace=True)
print(data)
#          age     city gender favourite_color new
# section
# A         10  Gurgaon      M             red  Gu
# B         22    Delhi      F            blue  De
# C         13   Mumbai      F          yellow  Mu
# B         21    Delhi      M            pink  De
# B         12   Mumbai      M           black  Mu
# A         11    Delhi      M           green  De
# A         17   Mumbai      F             red  Mu

# How to remove the column city ?
data.drop(columns="city", inplace=True) # you can use this way or below
# data.drop("city", axis=1, inplace=True)
print(data)
#          age gender favourite_color new
# section                                
# A         10      M             red  Gu
# B         22      F            blue  De
# C         13      F          yellow  Mu
# B         21      M            pink  De
# B         12      M           black  Mu
# A         11      M           green  De
# A         17      F             red  Mu

'''

