'''Data Set name – titanic.csv
1. many missing data points we have display the count for each column.
2. Fill “NaN" with "0".
3. Fill missing value of Name column with “Unknown”
4. Fill missing value of Age column with average of Age column
5. Fill missing value of Cabin column with “NA”
6. Replace Survived columns value 0 to “alive” and 1 to “dead”'''

import pandas as pd

print("\n\nQUESTION NO 1")
df=pd.read_csv("titanic.csv")
print(df.isna().sum())

'''print("\n\nQUESTION NO 2")
df["Name"]=df["Name"].fillna("Unknow")
print("Successfully filled name colomun with unknow")
print(df.loc[1::,["Name"]])'''

'''print("\n\nQUESTION NO 3")
df=df.fillna(0)
print("Successfully filled with zero ")
print(df)
'''
'''print("\n\nQUESTION NO 4")
avg=df["Age"].mean()
df["Age"]=df["Age"].fillna(avg)
print(avg)
print(df.Age)'''

print("\n\nQUESTION NO 5")
df["Cabin"]=df["Cabin"].fillna("NA")
print(df.Cabin)

print("\n\nQUESTION NO 6")
df["Survived"]=df["Survived"].replace({0:"DEAD",1:"ALIVE"})
print(df.Survived.head(10))
