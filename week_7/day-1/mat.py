import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [2, 20, 35, 6]
plt.plot(x, y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('first graph')
plt.show()

# data = pd.read_csv("https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv")

# plt.plot(data.id, data["sepal_length"], "r--") 
# plt.show()