import pandas as pd
#---QUESTION NO 1---
df=pd.read_csv("Teams.csv")
first_point=df.iloc[:1,:]
print(first_point)

#---QUESTION NO 2---
print("FIRST ROW OF THE DATA\n")
print(df.iloc[0])

#---QUESTION NO 3---
print("FIRST 10 VALUES FROM THE DATA")
print(df.loc[:10,["Year"]])

#---QUESTION NO 4---
sample_records=df.iloc[[1,2,3,5,8],:]
print(sample_records)

#---QUESTION NO 5---
print(df.loc[[0,5,10],["Rank","Points","Team"]])

#---QUESTION NO 6---
a=df.tail().loc[::,["Team","Rank"]]
print(a)

#---QUSTION NO 7---
print(df.iloc[::2])

#---QUSTION NO 8---
print(df.iloc[1::2])
