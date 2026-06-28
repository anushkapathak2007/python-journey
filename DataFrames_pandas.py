import pandas as pd 
data={"Name":["Spongebob","Patrick","Squidward","Mr.Krabs"],"Age":[20,21,22,23]}
df=pd.DataFrame(data,index=["employee1","employee2","employee3","employee4"])
print(df)
print(df.loc["employee1"])
print(df.iloc[0])