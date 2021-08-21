import numpy as np

A = numpy.array([4,8,10])
B = numpy.array([6,10,-8])

# For YZ plane
n = numpy.array([1,0,0])
d = 0

# ratio 
k = (d-np.dot(np.transpose(n),A))/(np.dot(np.transpose(n),B)-d)
print('k =',k)

# point of intersection
P = (A+k*B)/(k+1)
print('P =',P)
