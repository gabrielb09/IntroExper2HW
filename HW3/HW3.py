import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab
import math

x = np.linspace(-8, 8, 100)
plt.plot(x,mlab.normpdf(x, 0, 1))
plt.plot(x,mlab.normpdf(x, 0, 2))
plt.plot(x,mlab.normpdf(x, 5, 1))
plt.show()
