import numpy as np


A = np.array([[1,1,1],[1,2,2],[1,2,3]])
print(A)
print(A.ravel())
print(A.flatten())

invA = np.linalg.inv(A)
print(invA)
B = np.array([1,1,1])
print(B.shape)
X = invA @ B
print(X)

