import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
y = [4,2,3,5,1,8]
plt.title("Scatter plot")
plt.xlabel("month")
plt.ylabel("Numbers")
plt.scatter(x,y)
plt.show()

# distinct color
x = [1,2,3,4,5,6]
y = [4,2,3,5,1,8]
plt.title("Scatter plot")
plt.xlabel("month")
plt.ylabel("Numbers")
c =['red','black','hotpink','blue','brown','green']
plt.scatter(x,y,color = c)
plt.show()

# CHANGING THE SIZE
x = [1,2,3,4,5,6]
y = [4,2,3,5,1,8]
plt.title("Scatter plot")
plt.xlabel("month")
plt.ylabel("Numbers")
c =['red','black','hotpink','blue','brown','green']
plt.scatter(x,y,color = c,s=150) # s for the size
plt.show()

# basic example
import matplotlib.pyplot as plt

# Ensure x and y have the same length
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# s also needs to match the length of x and y
sizes = [20, 50, 100, 200, 300]

# Correct scatter plot
plt.scatter(x, y, c='red', s=sizes, alpha=0.5)
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
