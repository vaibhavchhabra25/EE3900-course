import numpy as np
import math
from matplotlib import pyplot as plt

x = np.linspace(-6,6,100)

def y(x,a):
    return (x**2-12*a-4)/4*a

plt.grid()
plt.title('Parabolas for different values of $a$')
plt.xlabel('x')
plt.ylabel('y')

plt.plot(x,y(x,-1/3),'b',label='$a=-1/3$')
plt.plot(x,y(x,1),'r',label='$a=1$')
plt.plot(x,y(x,1/3),'g',label='$a=1/3$')

plt.legend()
