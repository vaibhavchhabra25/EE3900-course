import matplotlib.pyplot as plt
import numpy as np

n = np.linspace(0,20,100,endpoint=True)

x_n = np.e**(1j*2*np.pi*n/5)

plt.plot(n,x_n)
plt.grid()
plt.xlabel("$n$")
plt.ylabel("$x[n]$")

plt.show()
