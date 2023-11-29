from nnfs.datasets import spiral_data
import numpy as np
import matplotlib.pyplot as plt
import nnfs

nnfs.init()

X, y = spiral_data(samples=100, classes=3)

print(X[:,0])
plt.scatter(X[:,0], X[:,1], c=y, cmap='brg')
plt.show()