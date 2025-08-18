# Bar plot in seaborn library
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
df1 =sns.load_dataset("penguins")
#print(df1)
sns.barplot(x=df1.island,y=df1.bill_length_mm)
plt.show()

# secound way tocreate a graph
sns.barplot(x="island",y="bill_length_mm",data=df1,hue="sex")
plt.show()

# ORDER PARAMETER
order1 = ["Dream","Torgersen","Biscoe"]
sns.barplot(x="island",y="bill_length_mm",data=df1,hue="sex",order=order1)
plt.show()

#hue order
order1 = ["Dream","Torgersen","Biscoe"]
sns.barplot(x="island",y="bill_length_mm",data=df1,hue="sex",order=order1,hue_order=['Female','Male'])
plt.show()

# HISTOGRAM IN SEABORN LIBRARY
sns.displot(df1["flipper_length_mm"],bins=[170,180,190,200,210,220,230,240],color='hot pink') # bins are used for peoper sequencing
plt.show()

# kernal density
sns.displot(df1["flipper_length_mm"],kde= False)
plt.show()