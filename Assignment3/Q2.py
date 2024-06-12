import numpy as np
from numpy import random

arr_1 = np.array([1, 2, 3, 4])
arr_2 = np.array([2, 4, 6, 8])
print(np.add(arr_1, arr_2))
print(np.subtract(arr_1, arr_2))
print(np.multiply(arr_1, arr_2))
print(np.divide(arr_1, arr_2))

# A
arr_3 = random.randint(0, 100, size = (3, 4))
print(arr_3)

# B
print(np.exp(arr_1), "\n", np.log(arr_1))

# C
arr_4 = np.array([1.2, 2.5, 5.6, 3.4, 7.8])
print(np.ceil(arr_4), "\n", np.floor(arr_4))