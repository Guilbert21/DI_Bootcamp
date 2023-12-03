# from sklearn.linear_model import LinearRegression
# import pandas as pd

# # df = pd.read_csv('height_weight.csv')


# # X = df['height']
# # print(X)

# # y = df['weight']
# # print(y)

# # # reshape
# # X = X.values.reshape(-1, 1)
# # y = y.values.reshape(-1, 1)


# # lr = LinearRegression()
# # reg = lr.fit(X, y)
# # reg.coef_, reg.intercept_(array([0.39657753]), 14.341004935139239)


# titanic = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv").dropna()
# y = titanic['Survived']
# X = titanic.drop(['Survived'], axis=1)._get_numeric_data()
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
# clf = LogisticRegression()
# clf.fit(X_train, y_train)



# y_pred = clf.predict(X_test)

