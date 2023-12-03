# import seaborn as sns
# import matplotlib.pyplot as plt

# sns.violinplot(x="Pclass", y="Fare", hue="Sex", data=df, split=True, inner="quartile")
# plt.title("Fare Distribution by Class and Gender")
# plt.show()

# sns.swarmplot(x="Pclass", y="Age", hue="Survived", data=df)
# plt.title("Age Distribution by Survival and Class")
# plt.show()

# corr = df.corr()
# sns.heatmap(corr, cmap="coolwarm", annot=True)
# plt.title("Correlation Matrix")
# plt.show()

# sns.pairplot(data=df, vars=["Age", "Fare"], hue="Survived")
# plt.title("Pair Plot of Age, Fare, and Survival")
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
df.head()
df.info()

sns.barplot(df['Pclass'])
plt.show()
# mean point plot
sns.catplot(x="Pclass", y="Age", hue="Sex", data=df, kind="point");
plt.show()

# scatter plot
sns.relplot(x="Pclass", y="Age",hue="Sex", style="Survived", data=df);
plt.show()

# Line Plot
sns.relplot(x="Pclass", y="Age", kind="line", data=df);
plt.show()

# Linear Regression Plot
sns.lmplot(x="Pclass", y="Age",data=df);
plt.show()