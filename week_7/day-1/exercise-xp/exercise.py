import numpy as np
import pandas as pd

# EX-1
# def create_array(start, length, stop):
#     return np.linspace(start, stop, length)

# my_array = create_array(6, 100, 6 + 4 * 99)
# EX-2
# a = np.array([1,2,3,np.nan,5,6,7,np.nan])
# print(a)

# a = a[np.logical_not(np.isnan(a))]
# print(a)

# EX-3
# arr_1 = np.random.randint(1,100, size = (5,6))
# print(arr_1)
# print("Maximum value is: ",arr_1.max())

# EX-4
series = pd.Series(np.take(list('abcdefghijklmnop'), np.random.randint(16, size=500)))
# df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')
print(series)
