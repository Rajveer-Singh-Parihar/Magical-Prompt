import pandas as pd
df = pd.read_csv(r"C:\Users\rajve\Downloads\customers-100.csv") # reading a csv file
print(df.replace(to_replace=1,value=22)) # one will be replce with 22
df.to_csv(r"C:\Users\rajve\Downloads\customers-100.csv",index=False) # writing a csv file
print(df)

# some basic example of cleaning
data = {
    'Name':['Alice','Bob','None'],
    'Age':[23,None,35]
}
df = pd.DataFrame(data)
df_cleaned = df.dropna() # cleaned data
print(df_cleaned) # alice - 23 , None - 35

# REMOVING THE DUPLICATES
datas = {
    'Name':['Alice','Bob','Alice'],
    'Age':[25,30,25]
}
df=pd.DataFrame(datas)
df_unique =df.drop_duplicates()
print(df_unique) # it prints only unique value
print("\n")

# INDEXING AND SELECTING
data = {
    'Name':['Alice','Bob','karan'],
    'Age':[23,30,35]
}
df = pd.DataFrame(data)
print(df.loc[0]) # selecting rows with index zero
print(df[df['Age']>30]) # age is greater than 30

# SORTING DATA
data = {
    'Name':['Alice','Bob','charlie'],
    'Age':[23,49,35]
}
df = pd.DataFrame(data)
df_sorted = df.sort_values(by='Age',ascending=False) # shows which person have high age
print(df_sorted)

# DATA AGROUPING AND AGGREGATING
data = {
    'Name':['Alice','Bob','raj'],
    'Score':[89,90,99]
}
df = pd.DataFrame(data)
grouped= df.groupby('Name').mean() # group all the data and shows the value
print(grouped)

# APPLYING FUNCTIONS
df['Score'] = df['Score'].apply(lambda x:x+5)
print(df) # print all the marks with increment of five

# MERGING AND COMBINING
df1 = pd.DataFrame({
    'Name':['Alice','Bob'],
    'Score':[90,85]
})
df2 = pd.DataFrame({
    'Name':['Charlie','Dave'],
    'Score':[88,92]
})
result = pd.concat([df1,df2])
print(result)

# merging
df1 = pd.DataFrame({
    'ID':[1,2],
    'Name':['Alice','Bob']
})
df2 = pd.DataFrame({
    'ID':[1,2],
    'Score':[90,85]
})
merged = pd.merge(df1,df2,on='ID') # gives id 1 for alice and 2 for bob and assign marks
print(merged)

# Time Series and analysis
df = pd.DataFrame()
df['Date']=pd.to_datetime(['2024-01-01','2024-01-02']) # add date column
print(df)
print(df[df['Date']>'2024-01-01']) # filter by date

# SUMMARY OF STATICS
dat = {'Age':[25,30,35,40]}
df=pd.DataFrame(dat)
print(df.describe())

# correlation
dat = {'A':[25,30,35,40],'B':[0,70,80,90]}
df=pd.DataFrame(dat)
print(df.corr())