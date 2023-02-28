import pandas as pd
import seaborn as sns


url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'

titanic_df = pd.read_csv(url)

titanic_df.head()


# summary statistics
print(titanic_df.describe())

# histogram of Age and Fare
sns.histplot(data=titanic_df, x='Age', bins=20, kde=True)
sns.histplot(data=titanic_df, x='Fare', bins=20, kde=True)

# relationship between Age and Survived
sns.boxplot(data=titanic_df, x='Survived', y='Age')

# relationship between Pclass and Fare
sns.boxplot(data=titanic_df, x='Pclass', y='Fare')

# relationship between Sex and Survived
sns.countplot(data=titanic_df, x='Sex', hue='Survived')
