import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
df = pd.read_csv(r"C:\Users\rajve\Downloads\people-100.csv")
sns.lineplot(x = 'First Name',y='Job Title',data=df,hue="Sex",style= "Sex",markers=["o",">"])
#print(df)
plt.show() # genrates clear best graph then matplotlib


# to see less data set graph
#df1 = sns.load_dataset("penguise").head(20)
df = pd.read_csv(r"C:\Users\rajve\Downloads\people-100.csv").head(20)
sns.lineplot(x = 'First Name',y='Job Title',data=df,hue="Sex",style= "Sex",markers=["o",">"])
plt.grid() # to add more detailing
plt.title("This is a linear graph related shoowing people proficiency")
plt.show()