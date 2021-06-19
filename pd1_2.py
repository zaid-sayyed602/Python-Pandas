import pandas as pd

#-----dictionary in dataframe
d={"id":[1,2,3,4,5],"name":["a","b","c","d","e"],"marks":[31,21,35,20,13]}
print(d)
df=pd.DataFrame(d)
print(df)
print(type(df))

#--Empty dataframe
df=pd.DataFrame()
df["id"]=[1,2,3,4]
df["name"]=["a","b","c","d"]
df["marks"]=[10,20,30,40]

#--accessing dataframe
print(df.name)
print(type(df.name))

#--accessing multiple dataframe
print(df[["id","name"]])

#---converting a dataframe to a csv file
df.to_csv("dataframe.csv",index=False)
print("FILE created")

#---converting csv file to a dataframe
df=pd.read_csv("dataframe.csv")
print(df)
