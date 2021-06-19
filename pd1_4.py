import pandas as pd
df=pd.read_csv("Teams_demo.csv")
print(df)

#---isna methods returns a boolean values of all the tables----
print(df.isna())

#---isna methods returns a boolean values of all the tables and sum method is used for detailed values----
print(df.isna().sum())

#---fillna method is used to fill the missing value---
#---here fillna is used to fill missing value with 0 or 1---
df=df.fillna(0)
print(df.isna().sum())
print(df)

#---here fillna is used to fill missing value with avg of the coloumn---
print(df.isna().sum())
avg=df["Points"].mean()
df["Points"]=df["Points"].fillna(avg)
print("Successfully filled with avg")

print(df)
print(df.isna().sum())

#---here fillna is used as backward fill in the missing place---
df["Rank"]=df["Rank"].fillna(method="bfill")
print(df)

#---here fillna is used as forward fill in the missing place---
df["Year"]=df["Year"].fillna(method="ffill")
print(df)

#----df.replace() is used to replace a value----
df=df.replace({"Devils":"Queens"})
print("success")
print(df)
print(df.isna().sum())


#----df.dropna() is used to drop a row---
df=df.dropna()
print(df)
df.to_csv("kachra.csv",index=False)
print("done!!!!!")
