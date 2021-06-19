import pandas as pd
d1={"id":[1,2,3,4,5],"name":["zaid","tanishq","sohan","hemant","mubeen"]}
d2={"id":[1,2,3,4,5],"marks":[80,24,23,34,30]}
df1=pd.DataFrame(d1)
df2=pd.DataFrame(d2)
df3=pd.merge(df1,df2,on="id")
df3.to_csv("merge.csv",index=False)
print(df3[(df3.name=="zaid") | (df3.id==1)])
