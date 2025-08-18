import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y1 = [1, 2, 3, 4, 5]
y2 = [2, 3, 4, 5, 6]
y3 = [3, 4, 5, 6, 7]
plt.stackplot(x, y1, y2, y3, labels=['A', 'B', 'C'], colors=['skyblue', 'lightgreen', 'pink'])
plt.legend()
plt.title('Stacked Area Plot Example')
plt.show()
