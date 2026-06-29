import pandas as pd

#csv file reading 

df=pd.read_csv("color_notepad.csv",index_col="HEX")
print(df.to_string())
 
 
#json file reading 


df1=pd.read_json("colors.json")
print(df1.to_string())

#selection by columns


##print(df["Name"].to_string())
##print(df[["Name","HEX"]].to_string())




##SELECTION BY ROWS 
print(df.loc["#FFFFFF"].to_string())
print(df.loc[["#FFFFFF","#000000"]].to_string())
print(df.loc[["#FFFFFF","#000000"],["Name","RGB"]].to_string())
