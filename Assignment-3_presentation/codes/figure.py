import numpy as np
import math
from matplotlib import pyplot as plt

def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def circ_gen(C,r):
	len = 100
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + C).T
	return x_circ

# Plotting a random circle for example
C = np.array([4,5])
r = 4
# Taking random x1 and x2 for illustration
x1 = np.array([C[0]+r*np.cos(1),C[1]+r*np.sin(1)])
x2 = np.array([C[0]+r*np.cos(2.5),C[1]+r*np.sin(2.5)])

M = (x1+x2)/2

ss_mat = np.array([[0,1],[-1,0]])

k = M + 0.4*(x2-x1)@ss_mat

x1x2 = line_gen(x1,x2)
Mk = line_gen(M,k)
x_circ = circ_gen(C,r)

plt.grid()
plt.axis('equal')
plt.xlabel('x')
plt.ylabel('y')

# plotting the circle
plt.plot(x_circ[0,:],x_circ[1,:],label='circle')

#plotting the lines
plt.plot(x1x2[0,:],x1x2[1,:],'-',label='Chord')
plt.plot(Mk[0],Mk[1],'g-',label='P.B.')

# plotting the points
plt.plot(C[0],C[1],'go',label='centre C')
plt.text(C[0],C[1]+0.2,'C')
plt.plot(x1[0],x1[1],'bo')
plt.text(x1[0],x1[1]+0.2,'x1')
plt.plot(x2[0],x2[1],'bo')
plt.text(x2[0]-0.4,x2[1]+0.2,'x2')
plt.plot(M[0],M[1],'bo')
plt.text(M[0],M[1]+0.2,'M')

plt.legend(loc='upper right')