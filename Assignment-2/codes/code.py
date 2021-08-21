import numpy as np

A = np.array([[0,6,7],[-6,0,8],[7,-8,0]])
B = np.array([[0,1,1],[1,0,2],[1,2,0]])
C = np.array([2,-2,3])

print('A =\n',A)
print('B =\n',B)
print('C =\n',C)

AC = A@C
BC = B@C

print('AC =',AC)
print('BC =',BC)

LHS = (A+B)@C
RHS = AC+BC

print('(A+B)C =',LHS)
print('AC+BC =',RHS)

print('Hence, (A+B)C = AC+BC')
