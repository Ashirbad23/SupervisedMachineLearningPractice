from scipy.linalg import det, inv
import numpy as np

A = [[3, 2, -1],
    [2, -4, 7],
    [1, 1, 1]]

A = np.matrix(A)

print(det(A))

print(inv(A))