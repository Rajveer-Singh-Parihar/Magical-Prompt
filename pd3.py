import pandas as pd
# creating series
s=pd.Series([1,2,3,4,5,6,7,8])
print(s)
# creating a data frame
var = pd.DataFrame({
    "A":[1,2,3,4],
    "B":[5,6,7,8]
})
print(var)
var["C"]=var["A"]+ var["B"] # we can do - , * ,/
print(var)

# new ex 
var1 = pd.DataFrame({"A":[10,20,30,40],"B":[50,60,70,80]})
var1["python"]=var1["A"] <=20 # value is less than 20
print(var1)

# insert and delete
var2 = pd.DataFrame({
    "A":[1,2,3,4],
    "B":[5,6,7,8]
})
var2.insert(1,"python",var["A"]) # column one become python and data is - 1,2,3,4
print(var2)
var2.insert(1,"Python_2",[12,13,14,15]) # index - column name and data
print(var2)

# Slicing
var2["python_2"] = var["A"][:2] # slice 0 1 
print(var2) # NAN - COMEA and new column create 0,1,nan,nan

# Deleting dataFrame
var3=var.pop("B")
print(var3)
del var["A"] 
print(var)