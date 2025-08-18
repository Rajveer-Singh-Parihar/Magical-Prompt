import matplotlib.pyplot as plt
import numpy as np
data = [7, 8, 5, 6, 9, 12, 15, 10]
plt.boxplot(data, vert=True, patch_artist=True)
plt.title('Box Plot Example')
plt.show()

# ex
test = np.random.normal(200,50,400)
plt.boxplot(test)
plt.show()