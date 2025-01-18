import pandas as pd

dict1={
    "Name": ["Arman","Ashish","Arpit","Shiv","Amar",],
    "EID": [112,113,114,115,116],
    "Salary": [35000,45000,11100,23490,50500],
    "City": ["Lucknow","Kanpur","Sultanpur","Pratagrah","Bhopal"]
    }
df=pd.DataFrame(dict1)
print(df)
print("------------------------------")
print(df.head())
print("------------------------------")
print(df.head(2))
print("------------------------------")
df.to_csv('Mydataframe.csv')
print("------------------------------")
print(pd.read_csv('Mydataframe.csv'))
print("------------------------------")
print(df.tail())
print("------------------------------")
print(df.tail(2))
print("------------------------------")
print(df.info())
print("------------------------------")
print(df.describe())
print("------------------------------")
#sort salary column ascending and descending
print("Before")
print(df)
print("After-ascending")
print(df.sort_values(by="Salary"))
print("After-descending")
print(df.sort_values(by="Salary",ascending=False))
print("------------------------------")

#location of data using LOC function
print(df)
print("-----")
print(df.loc[2])
print("-----")
print(df.loc[0:2])
print("------------------------------")
