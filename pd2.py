import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\rajve\Downloads\customers-100.csv") # csv file comma separated file - way to store big data sets
a = df['Website'][0:10]
print(a)
l =['Rajveer','a1','Banna','a2','a3','Prabal','A10','a4','a5','a6']
print(pd.Series(list(a),index=l)) # to change the index according to needs

s= pd.Series(np.random.rand(34))
print(s)

# Creating Data Freame
m1 = pd.Series([100,200,300,400,500],index=[1,2,3,4,5])
print(m1)
m2 = pd.Series([600,700,800,900,1000],index=[1,2,3,4,5])
m3 = pd.concat([m1,m2]) # print whole series upto 1000
print(m3)
print(m3[1]) # 100 - 600
print(m1*m2) # we can perform multiplication
print(m1+m2) # return the addition 

# deleting particular column
print(df.drop('Website',axis=1)) # temprorary delete
print(df.drop('Phone 2',axis=1,inplace=True)) # to delete permanently
print(df.drop(3)) # deleting third row temprory
print(df.drop(3,inplace=True)) # to delete permanently

# converting any name column to index
print(df.set_index('Website')) # index ki jagah website name - this change is not permanently
print(df.set_index('Website',inplace=True)) # to delete permanently
print(df.reset_index()) #reset our index

# MAKING DATAFRAME FROM THE DICTIONARY
d = {
    "name":["john","Candy","bob","freshi"],
    "marks":[34,56,75,90],
    "sports":["Cricket","volyball","kabbddi","tenis"]
}
s=pd.DataFrame(d)
print(s)

# To remove the missing value in ROW - NAN
print(df.dropna()) # temprorary delete
print(df.dropna(subset=["Index"])) # to delete particular column - null value
print(df.dropna(inplace=True)) # to delete permanently
print(df.dropna(axis=1,inplace=True)) # to delete against the row

# FILL SOMETHING AT MISSING INDex
print(df.fillna(method="ffill")) # forward fill
print(df.fillna(method="bfill")) # backward fill
print(df.fillna("Rajveer")) # null index value is rajveer