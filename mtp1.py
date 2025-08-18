import matplotlib.pyplot as plt
# LINEAR - PLOT GRAPH
x = [1,2,3,4]
y = [5,6,7,8]
plt.title("Linear Graph")
plt.plot(x,y)
plt.show()

# changing color
x = [1,2,3,4]
y = [5,6,7,8]
c = 'r' #red color - we can give green ,pink ,red ,purple color also
plt.plot(x,y,c)
plt.show()

# creating random lines
x=[5,3,8,7,6]
y=[10,5,8,4,2]
plt.plot(x,y)
plt.show()

# CREATING MARKER
x=[5,3,8,7,6]
y=[10,5,8,4,2]
plt.plot(x,y,marker ='.')
plt.show()

# CREATING DIFFERENT GRAPH FOR X AND Y
x=[5,3,8,7,6]
y=[10,5,8,4,2]
plt.plot(x,y)
plt.plot(y,marker = '>')
plt.plot(x,marker = '.')
plt.show()