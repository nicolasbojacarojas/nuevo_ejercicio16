import numpy as np
import matplotlib.pyplot as plt
a = np.loadtxt("album.txt")
x = a[:,1]
y = a[:,0]
plt.plot(x,y)
plt.savefig("album")
