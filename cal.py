import numpy as np
arr1 = np.array([[1, 2, 3], [1, 2, 3]])
arr2 = np.array([[5, 6, 7], [5, 6, 7]])
arr3 = np.concatenate((arr1, arr2))
print(arr3)

arr4 = np.array([1, 2, 3])
arr5 = np.array([5, 6, 7])
arr6 = np.concatenate((arr4, arr5))
print(arr6)