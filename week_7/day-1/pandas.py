import pandas as pd
import numpy as np

df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv')

print(df.groupby("species").apply(np.mean))