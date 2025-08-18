import matplotlib.pyplot as plt
import numpy as np
x = [1,2,3,4]
y = [5,6,7,8]
plt.title("Bar Graph")
plt.bar(x,y)
plt.show()

# changing bar color
x = [1,2,3,4]
y = [5,6,7,8]
c = ['g','r','y','b']
plt.bar(x,y,color = c)
plt.show()

x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])
plt.bar(x,y,color = "hotpink")
plt.show()

# CREATING HORIZONTAL REPRESENTATION OF BAR GRAPH
x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])
plt.barh(x,y) # h is for horizontal representation
plt.show()

# MANAGING BAR GRAPH WIDTH ACCORDING TO NEEDS
x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])
plt.bar(x,y,color = "hotpink",width=0.4)
plt.show()


x = np.array(["A","B","C","D"])
y = np.array([3,8,1,10])
plt.barh(x,y,color = "hotpink",height=0.1)
plt.show()