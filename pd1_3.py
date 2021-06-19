import pandas as pd
#--reading a file 
df=pd.read_csv("Teams.csv")
print(df)

#--print info of the csv file
#print(df.info())

'''--head mehod used to print first 5 rows and we can
give the no of rows we want in the paranthesis'''
#print(df.head())

'''--head mehod used to print last 5 rows and we can
give the no of rows we want in the paranthesis'''
#print(df.tail())

'''--iloc is used to acces row as well as coloumn by
giving row and column index and by using slicing '''
print(df.iloc[[0,2,4],[1]])

'''--loc is used to access row as well as coloumn by
giving rows index and columns name and by using slicing''' 
print(df.loc[[0,2,3],["Rank","Year"]])

