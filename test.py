import numpy as np 

A = np.array([[1,2],[4,2]])
b = np.array([[35],[110]])
A_inverse = np.linalg.inv(A)
x = A_inverse@b
print(x)