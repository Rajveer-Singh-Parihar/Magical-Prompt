import matplotlib.pyplot as plt
x = [10,20,30,40]
y= ["english","hindi","maths","science"]
plt.pie(x,labels= y)
plt.show()

# if we want color according to our need
x = [10,20,30,40]
y= ["english","hindi","maths","science"]
c =['yellow','magenta','brown','aqua']
plt.pie(x,labels= y,colors= c)
plt.legend() # labels
plt.show()