# To Read First five lines from a file
import pandas as pd
df = pd.read_csv(r"C:\Users\rajve\Downloads\customers-100.csv")
print(df) #- print whole data
print(df.head()) # read first five data 
print(df.head(10)) # want to see first 10 data
print(df.tail()) # to see last five data
print(df.tail(20))# tosee last 20 data
print(df.dtypes) # To check the data which type
print(df.describe()) #for statics and computing - numerical data
print(df.dtypes== 'object') # describing the data which is object
print(df[df.dtypes[df.dtypes=='int 32'].index]) # we can check integer and floating point number as well
print(df[['Customer Id','Email','Phone 2','Website']]) # data according we want we get
print(df.columns) # to check all columns in data sets
print(df[['Email']]) # to show all email column
print(df[['Email']][3:16]) # show email 3 to 15 beacuse runs n-1
print(df[['Email']][3:16:2]) # runs with step of 2(jump) - 3,5,7,9,11,13,15
print(df[['Email','Website']][4:17]) # slicing 4 to 16 (n-1 so give 17)
print(df[['Email','Website']][4:17:3]) # jump of 3
df['new_col']=0 # creating new column whose value is zero - we can assign any type of value
print(df)
df.insert(loc= 3 , column='food',value=0) # creating column where want to create
print(df)
df.insert(loc= 2 , column='Equipments',value="oxygen cylinder") # creating column where want to create
print(df)