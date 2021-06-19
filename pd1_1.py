import pandas as pd
#--dictionary in series
a=pd.Series({"a":1,"b":2,"c":3,"d":4})
#---tuple in series
a=pd.Series((1,2,3,4))
#---list in series
a=pd.Series([1,2,3,4])
#--index parameter in series
a=pd.Series([1,2,3],index=(10,20,30))
print(a)
#---index parameter for constant value
a=pd.Series(2,index=(10,20,30))
print(a)
