import  pandas as pd
import numpy as np

data = pd.DataFrame([('bird', 389.0 ),
                     ('bird', 40.0 ),
                     ('bird', 405.0 ),
                     ('mammal', 80.2 ),
                     ('mammal', 12.0 ),
                     ('mammal', 58 )
                     ],
                     index=['falcon', 'parrot', 'eagle', 'lion', 'monkey', 'leopard'],
                    columns=('class', 'speed')
                    )
print(data)
# 	        class	speed
# falcon	bird	389.0
# parrot	bird	40.0
# eagle	    bird	405.0
# lion	    mammal	80.2
# monkey	mammal	12.0
# leopard	mammal	58.0


########################################################
# How to calculate the avg speed of birds and mammals using  groupby method?
# You should get the following table.
# it shows all the columns of data dataframe which is numeric.
#
# print(data.groupby('class').mean() )
#              speed
# class
# bird    278.000000
# mammal   50.066667


########################################################
# How to calculate the max speed of birds and mammals using  groupby method?
# You should get the following table.
#
# print(data.groupby("class")['speed'].max())

# class
# bird      405.0
# mammal     80.2
# Name: speed, dtype: float64


########################################################
# Example of using multiple agg.functions in list:
#
# print(data.groupby('class')['speed'].agg(['mean', 'median' , 'min', 'max']))
#               mean  median   min    max
# class
# bird    278.000000   389.0  40.0  405.0
# mammal   50.066667    58.0  12.0   80.2


# Let's use double brackets for speed column.
# You can see the speed column name at the top:
#
# print(data.groupby('class')[['speed']].agg(['mean', 'median' , 'min', 'max']))
#              speed
#               mean median   min    max
# class
# bird    278.000000  389.0  40.0  405.0
# mammal   50.066667   58.0  12.0   80.2


# if you are using agg. function(mean, median, sum) inside the quotation mark you
# don't need to use it with a module name(np=numpy, pd=pandas).
#
# print(data.groupby('class').agg({'speed':['mean','median',np.mean, np.median]}))
#              speed
#               mean median        mean median
# class
# bird    278.000000  389.0  278.000000  389.0
# mammal   50.066667   58.0   50.066667   58.0


# if you use 'speed' with one square bracket [] you take error.
# print(data.groupby('class')['speed'].agg({'speed':['mean','median',np.mean, np.median]}))
# pandas.core.base.SpecificationError: nested renamer is not supported


# if you want to use 'speed' column with agg dictionary function,
# you must use it with double square brackets. [[]].
# print(data.groupby('class')[['speed']].agg({'speed':['mean','median',np.mean, np.median]}))
#              speed
#               mean median        mean median
# class
# bird    278.000000  389.0  278.000000  389.0
# mammal   50.066667   58.0   50.066667   58.0
########################################################