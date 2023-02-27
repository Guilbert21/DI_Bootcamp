import numpy as np

# PART-1
arr_1 = np.random.randint(1,100, size = (5,5))
print(arr_1)

# PART-2
arr_1 = arr_1[2, :]
print(arr_1)

# PART-3
# arr_1 = arr_1[:, 3]
# print(arr_1)

# PART-4

arr_1[4, :] = arr_1[4, :] = 7
print(arr_1)

# PART-5
arr_1[:, 4] = arr_1[:, 0] + arr_1[:, 1]
print(arr_1)