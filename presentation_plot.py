import matplotlib.pyplot as plt
import numpy as np
import math

t = np.linspace(-5, 10,100)

y = (8.00/55.00)*np.cos(2*t) +(107.00/55.00)*np.sin(2*t) + (-8.00/55.00)*np.exp(-3*t/4)

plt.grid()
plt.xlabel('$t$')
plt.ylabel('$y(t)$')
plt.plot(t,y)
plt.show()
