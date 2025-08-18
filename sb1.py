import matplotlib.pyplot as plt
import seaborn as sns # seaborn is advance then matplotlib
var = [1,2,3,4,5,6,7,8]
var1 = [8,7,6,5,4,3,2,1]

# creating plot using matplotlib
plt.plot(var ,var1)
plt.show()

# creating plot using seaborn
sns.lineplot(x=var , y=var1)
plt.show()

# using pandas
import pandas as pd
var = [1,2,3,4,5,6,7,8]
var1 = [8,7,6,5,4,3,2,1]
df = pd.DataFrame({
    "var" : var,
    "var1": var1
})
print(df)
sns.lineplot(x='var',y='var1',data=df)
plt.show()