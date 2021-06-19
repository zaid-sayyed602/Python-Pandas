import pandas as pd
import numpy as np
print("\n\nQuestion 1: From given data set print first and last five rows:")
df=pd.read_csv("Automobile.csv")
print(df.head(5))
print(df.tail(5))

print("Question 2: Find the most expensive car company name")
print(df[["company","price"]][df["price"]==df['price'].max()])

print(" Question 3: Print All Toyota Cars details")
company=df.groupby("company")
print(company.get_group("toyota"))

print("Question 4: Count total cars per company")
company=df.groupby("company")
a=company.count()
print(a['index'])
#---METHOD WITHOUT USING GROUPBY----
##print(df.set_index(["company","index"]).count(level="company")
#---DIRECT METHOD TO COUNT SAME VALUES----
##print(df["company"].value_counts())

print("Question 5: Find each company’s Highest price car")
company=df.groupby("company")
a=company["price"].agg(np.max)
print(a)

print("Question 6: Find the average mileage of each car making company")
company=df.groupby("company")
a=company["average-mileage"].agg(np.mean)
print(a)

print("Question 7: Sort all cars by Price in descending order column and display first five rows")
b=df.sort_values(by="price",ascending=False,na_position="last")
print(b.head(5))

print("Question 8: Concatenate two data frames using the following conditions")
d1={"company":["ford","mercedes","bmw","audi"],"price":[23845,171995,135925,71400]}
d2={"company":["toyota","honda","nissan","mitsubishi"],"price":[29995,23600,61500,58900]}
df1=pd.DataFrame(d1)
df2=pd.DataFrame(d2)
df3=pd.concat([df1,df2],keys=["Germany","Japan"])
print(df3)

print("Question 9: Merge two data frames using the following condition")
d1={"company":["toyota","honda","bmw","audi"],"price":[23845,17995,135925,71400]}
d2={"company":["toyota","honda","bmw","audi"],"horsepower":[141,80,182,160]}
df1=pd.DataFrame(d1)
df2=pd.DataFrame(d2)
df3=pd.merge(df1,df2,on="company")
print(df3)
