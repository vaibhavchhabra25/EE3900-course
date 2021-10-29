import numpy as np

import matplotlib.pyplot as plt

t = [-5,0,5] 
u_t = [0,0, 1]

plt.step(t, u_t)
plt.title('Unit step input')
plt.xlabel('$t$')
plt.ylabel('$r(t)$')
plt.show()

import matplotlib.pyplot as plt

t = np.linspace(0,5,100)
plt.plot(t, 1-np.e**(-2*t))
plt.title('Unit-step response')
plt.xlabel('$t$')
plt.ylabel('$c(t)=1-e^{-2t}$')
plt.show()

import matplotlib.pyplot as plt

s = np.linspace(-2,5,100)
plt.plot(s, 2/(2+s))
plt.title('Transfer function')
plt.xlabel('$s$')
plt.ylabel('$T(s)=\dfrac{\mathcal{L}\{c(t)\}(s)}{\mathcal{L}\{r(t)\}(s)}$')
plt.show()
