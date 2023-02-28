import seaborn as sns
import matplotlib.pyplot as plt

sns.violinplot(x="Pclass", y="Fare", hue="Sex", data=df, split=True, inner="quartile")
plt.title("Fare Distribution by Class and Gender")
plt.show()

sns.swarmplot(x="Pclass", y="Age", hue="Survived", data=df)
plt.title("Age Distribution by Survival and Class")
plt.show()

corr = df.corr()
sns.heatmap(corr, cmap="coolwarm", annot=True)
plt.title("Correlation Matrix")
plt.show()

sns.pairplot(data=df, vars=["Age", "Fare"], hue="Survived")
plt.title("Pair Plot of Age, Fare, and Survival")
plt.show()

