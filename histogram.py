import matplotlib.pyplot as plt
import numpy as np
import random
x = np.random.randint(10,60,(50))
print(x)

data = [1, 2, 2, 3, 3, 3, 4, 4, 5]
plt.hist(data, bins=5, color='purple', edgecolor='black')
plt.title('Histogram Example')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.show()


# example
import matplotlib.pyplot as plt

# Example dataset
data = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5]

# Normalized histogram
plt.hist(data, bins=3, density=True, color='green', alpha=0.7, edgecolor='black')
plt.title('Normalized Histogram')
plt.xlabel('Value')
plt.ylabel('Density')
plt.legend(["Data"])
plt.show()



# example
import matplotlib.pyplot as plt

# Two datasets
data1 = [1, 2, 2, 3, 3, 3, 4, 4, 4, 5]
data2 = [2, 3, 3, 4, 4, 5, 5, 5, 6, 7]

# Overlaid histograms
plt.hist(data1, bins=5, alpha=0.5, label='Dataset 1', color='blue', edgecolor='black')
plt.hist(data2, bins=5, alpha=0.5, label='Dataset 2', color='orange', edgecolor='black')
plt.title('Overlaid Histograms')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.legend()
plt.show()
