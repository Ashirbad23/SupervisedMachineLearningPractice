import numpy as np
from numpy import linalg as LA


arr_1 = np.array([[1, 2], [3, 4]])
arr_2 = np.array([[2, 4], [6, 9]])

arr_1 = np.matrix(arr_1)
arr_2 = np.matrix(arr_2)

# (A)
mat_mul = np.dot(arr_1, arr_2)
print(mat_mul)

# (B)
eigen_value1, eigen_vector1 = LA.eig(arr_1)
eigen_value2, eigen_vector2 = LA.eig(arr_2)
print(eigen_value1, "\n", eigen_value2)
print("\n",eigen_vector1,"\n",eigen_vector2)

# (C)
determinant1, determinant2 = LA.det(arr_1), LA.det(arr_2)
print(determinant1, "\n", determinant2)

# (D)
inv1, inv2 = LA.inv(arr_1), LA.inv(arr_2)
print(inv1, "\n", inv2)