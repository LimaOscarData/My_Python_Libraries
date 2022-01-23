import pandas as pd
import numpy as np

data = [1, 3, 5, 7, 9, 18]
# dataframe
print("dataframe\n", pd.DataFrame(data = data),"\n")
# series
print("series\n", pd.Series(data = data),"\n")
#  changing column name
print("changing column name\n",pd.DataFrame(data = data, columns=["col_1"]),"\n")
### Creating a DataFrame using a NumPy Arrays ###
m = np.arange(1,24,2).reshape(3,4)
print("m :\n", m ,"\n")
df=pd.DataFrame(data=m, columns=['var1','var2','var3','var4'])
print("dataframe of m:\n",df,"\n")
print("head of df m :\n", df.head(),"\n")
print("head with value 1 :\n", df.head(1),"\n")
print("tail of m:\n", df.tail(),"\n")
print("tail of m with value 1:\n", df.tail(1),"\n")
print("sample of m with value 2 :\n",df.sample(2) ,"\n")
print("df's column :\n",df.columns , "\n")
print("for each loop of the sum of columns :")
for i in df.columns:
    print("total of column 1:\n", df[i].sum(), "\n")
df.columns = ["new1", "new2", "new3", "new4"]
print("after assigning new values to the column names :\n", df, "\n")
df.index = ["a", "b", "c"]
print("after change the index of df :\n", df, "\n")
print("another way to change of column name :\n", df.rename(columns={"new1": "a", "new2":"b"}) , "\n")
print("Another way of changing index label :\n", df.rename(index = {"a":1, "b":2}) ,"\n")
print("shape of df :\n", df.shape , "\n")
print("finding the column length from shape :\n" , df.shape[1], "\n")
print("dataframe ndim :\n", df.ndim, "\n")
print("size of data frame :\n", df.size, "\n")
print("length of df :\n", len(df) , "\n")
print("values of df :\n", df.values,"\n")
print("type of df :\n" , type(df), "\n")
print("type of df.values :\n", type(df.values), "\n")
### Creating a DataFrame using a dict ###
s1 = np.random.randint(2,10, size = 4)
s2 = np.random.randint(3,10, size = 4)
s3 = np.random.randint(4,15, size = 4)
print("s1, s2 and s3 arrays are :", s1, s2, s3, "\n", sep="\n")
print("Type of s1 : \n", type(s1), "\n")
my_dict = {"var1":s1, "var2":s2, "var3":s3}
print("my_dict is :\n", my_dict, "\n")
df1 = pd.DataFrame(my_dict)
print("df1 is :\n", df1, "\n")
print("df1 index is : \n", df1.index, "\n")
print("list comprehensions [i for i in df1.index]:\n", [i for i in df1.index], "\n")
print("'var2' in df1 :\n","var2" in df1)
### Now, let's examine again the idexing, selection and slicing methods
# and several attributes using a different DataFrame : ###
from numpy.random import randn
print("rand(5,4) result :\n", randn(5,4), "\n")
print("split example 'A B C D E'.split() :\n", 'A B C D E'.split(),"\n")
np.random.seed(101)
df3 = pd.DataFrame(randn(5,4), index = 'A B C D E'.split(), columns = 'W X Y Z'.split())
print(" df3 is :\n", df3, "\n")
# Selection and Indexing
print("df3['W'] :\n", df3["W"], "\n")
print("type of df3 :\n", type(df3["W"]), "\n")
print("df3[['W']] :\n", df3[["W"]], "\n")
print("type of df3[['W']] :\n", type(df3[["W"]]), "\n")
print("df3[['W', 'Z']] is df:\n", df3[["W", "Z"]], "\n")
print("df3['A':'C'] is a df :\n", df3["A":"C"], "\n")
print("type of df3['A':'C'] :\n", type(df3['A':'C']),"\n")
print("df3['A':'C']['W'] :\n", df3["A":"C"]["W"], "\n")
a= df3["A": "C"][["W", "Y"]]
print("a is (df3['A': 'C'][['W', 'Y']]) :\n", a, "\n")
# Creating a new column :
print("df3 is :\n", df3, "\n")
df3["new"] = df3["X"] * df3["Y"]
print("df3['new'] = df3['X'] * df3['Y'] :\n", df3, "\n")
df3["new2"] = [1,2,3,4,5]
print("df3['new2'] = [1,2,3,4,5] :\n",df3,"\n")
df3 = df3[["new", "new2", "W", "X", "Y", "Z"]]
print("df3 = df3[['new', 'new2', 'W', 'X', 'Y', 'Z']] :\n",df3, "\n")
### Removing Columns & Rows ###
# Removing Columns
print(""" there are two ways to drop columns
first :df3.drop(columns=["new","new2"])
second :df3.drop("new", axis=1)\n""" )
df3.drop("new2", axis=1)
print("df3.drop('new2', axis=1) (without inplace):\n", df3.drop("new2", axis=1), "\n")
df3.drop(["new","new2"], axis=1)
print('df3.drop(["new","new2"], axis=1) is :\n', df3.drop(["new","new2"], axis=1), "\n")
print("after all drop commands df3 didn't change df3 (without inplace):\n",df3, "\n")
df3.drop(columns=["new","new2"])
print('df3.drop(columns=["new","new2"]) command :\n' , df3.drop(columns=["new","new2"]), "\n")
print('after we drop "new","new2" without inplace:\n', df3, "\n")
df3.drop("new", axis=1)
print('After w drop "new" with axis=1, df3.drop("new", axis=1)\n', df3.drop("new", axis=1), "\n")
df3.drop(["new","new2"], axis=1, inplace=True)
print('after we drop "new","new2" with inplace command df3.drop(["new","new2"], axis=1, inplace=True):\n', df3, "\n")
# Removing rows
print("""there are two ways to do delete rows
first one is df4.drop(index="a")
second one is df4.drop('a', axis=0)
""")
m = np.random.randint(1,40, size=(8,4))
df4 = pd.DataFrame(m, columns = ["var1","var2","var3",'var4'])
df4.index='a b c d e f g h'.split()
print('df4 is :\n', df4, "\n")
df4.drop('a', axis=0)
print(" after we drop line 0 with , df4.drop('a', axis=0)\n", df4.drop('a', axis=0), "\n")
df4.drop(index='a')
print('after we drop index a df4.drop(index="a") :\n', df4.drop(index='a'), "\n")
df4.drop(index=['a'])
print('after we drop index a df4.drop(index=["a"]) :\n', df4.drop(index=['a']), "\n")
### Selecting Rows ###
m = np.random.randint(1,40, size=(8,4))
df5 = pd.DataFrame(m, columns = ["var1","var2","var3",'var4'])
print("df5 :\n", df5,"\n")
print("df5.loc[4] is:\n", df5.loc[4], "\n")
print('type of df5.loc[4]', type(df5.loc[4]), "\n")
print("df5.loc[[4]]: \n", df5.loc[[4]], "\n")
print('type of df5.loc[[4]] is df:\n', type(df5.loc[[4]]), "\n")
print("df5.loc[2:5] is : \n", df5.loc[2:5], "\n")
print("type of df5.loc[2:5] is :\n", type(df5.loc[2:5]), "\n")
print("df5.iloc[2:5] is :\n", df5.iloc[2:5], "\n")
print("type of df5.iloc[2:5] :\n", type(df5.iloc[2:5]), "\n")
df5.index='a b c d e f g h'.split()
print("we assign new label to index :\n", df5, '\n')
print("df5.iloc[1:4] is :\n", df5.iloc[1:4], "\n")
print("type of df5.iloc[1:4] :\n", type(df5.iloc[1:4]), "\n")
print('df5.loc["a":"d"] is :\n', df5.loc["a":"d"], '\n')
print('type of df5.loc["a":"d"] is :\n', type(df5.loc["a":"d"]), "\n")
print('df5.iloc[3,1] is :\n', df5.iloc[3,1], '\n')
print('df5.loc["d","var2"] is :\n', df5.loc["d","var2"], "\n")
print('df5.loc["d":"g","var3"] is :\n', df5.loc["d":"g","var3"], "\n")
print('type of df5.loc["d":"g","var3"] is :\n', type(df5.loc["d":"g","var3"]), "\n")
print('df5.loc["d":"g"]["var3"] is :\n', df5.loc["d":"g"]["var3"], "\n")
print('type of df5.loc["d":"g"]["var3"] is :\n', type(df5.loc["d":"g"]["var3"]), "\n")
print('df5.loc["d":"g"][["var3"]] is :\n', df5.loc["d":"g"][["var3"]], "\n")
print('type of df5.loc["d":"g"][["var3"]] is :\n', type(df5.loc["d":"g"][["var3"]]), "\n")
print('df5.loc["d":"g",["var3"]] is :\n', df5.loc["d":"g",["var3"]], "\n")
print('type of df5.loc["d":"g",["var3"]] is :\n', type(df5.loc["d":"g",["var3"]]), "\n")
print('df5.iloc[2:5,2] is :\n',df5.iloc[2:5,2], "\n")
print('type of df5.iloc[2:5,2] is :\n', type(df5.iloc[2:5,2]), "\n")
print('df5.iloc[2:5][["var2"]] is :\n', df5.iloc[2:5][["var2"]],"\n")
print('type of df5.iloc[2:5][["var2"]] is :\n', type(df5.iloc[2:5][["var2"]]), "\n")
print('df3 is :\n', df3, "\n" )
print('df3.loc["C"] is :\n', df3.loc["C"], "\n")
print('df3.iloc[2] is :\n', df3.iloc[2], "\n")
print('df3.loc[["C"]] is df :\n', df3.loc[["C"]], "\n")
print('df3.iloc[[2]] is :\n', df3.iloc[[2]], "\n")
### Selecting subset of rows and columns ###
print('df3.loc["C","Z"] is :\n',df3.loc["C","Z"], "\n")
print('type of df3.loc["C","Z"]\n', type(df3.loc["C","Z"]), "\n")
print('df3.loc[["C"],["Z"]] is :\n', df3.loc[["C"],["Z"]], "\n")
print('type of df3.loc[["C"],["Z"]] is:\n', type(df3.loc[["C"],["Z"]]), "\n")
print('df3.loc[["A", "C"], ["X","Z"]] is :\n', df3.loc[["A", "C"], ["X","Z"]], "\n")
print('type of df3.loc[["A", "C"], ["X","Z"]] is :\n',type(df3.loc[["A", "C"], ["X","Z"]]),"\n")
print('df3.iloc[[0,2],[0,3]] is :\n',df3.iloc[[0,2],[0,3]], "\n")
print('type of df3.iloc[[0,2],[0,3]] is :',type(df3.iloc[[0,2],[0,3]]),"\n")
### Conditional Selection ###
print('df3[df3 > 2] is :\n', df3[df3 > 2], "\n")
print('df3[df3["Z"]>0.5] is :\n', df3[df3["Z"]>0.5], "\n")
print('df3[df3["Z"]>0.5][["X"]] is :\n', df3[df3["Z"]>0.5][["X"]], "\n")
### For two conditions you can use | → or, & → and with parenthesis: ###
print("df3[(df3['W']>0) & (df3['Y']<1)] is :\n", df3[(df3['W']>0) & (df3['Y']<1)] , "\n")
print("df3[(df3['W']>0) & (df3['Y']<1)] == 0 is :\n", df3[(df3['W']>0) & (df3['Y']<1)] == 0, "\n")
### Conditional selection using .loc[] and .iloc[] ###
print('df3.loc[(df3.X > 0), ["X", "Y"]] is :\n', df3.loc[(df3.X > 0), ["X", "Y"]], "\n")
print("df3.loc[((df3.W>1) | (df3.Y<1)), ['Y','Z']] is :\n", df3.loc[((df3.W>1) | (df3.Y<1)), ['Y','Z']], "\n")
df3.reset_index()
print('df3.reset_index() is :\n',df3.reset_index(), "\n")
df3.reset_index(drop=True)
print("df3.reset_index(drop=True) is :\n", df3, "\n")
print('df3.set_index("Z") is :\n', df3.set_index("Z"), "\n")
df3.reset_index(drop=True, inplace=True)
print('df3.reset_index(drop=True, inplace=True) is :\n', df3,"\n")









