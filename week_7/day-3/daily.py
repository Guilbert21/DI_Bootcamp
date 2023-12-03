# import seaborn as sns
# import numpy as np
# from sklearn.datasets import load_boston
# import pandas as pd

# boston=load_boston()
# boston_df=pd.DataFrame(boston.data,columns=boston.feature_names)
# boston_df['Price']=boston.target

# continuous_features = ['CRIM', 'ZN', 'INDUS', 'NOX', 'RM', 'AGE', 'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT', 'Price']

# for feature in continuous_features:
#     sns.boxplot(x=feature, data=boston_df)

# for feature in continuous_features:
#     q1 = np.percentile(boston_df[feature], 25)
#     q3 = np.percentile(boston_df[feature], 75)
#     iqr = q3 - q1
#     lower_bound = q1 - 1.5 * iqr
#     upper_bound = q3 + 1.5 * iqr
#     num_outliers = len(boston_df[(boston_df[feature] < lower_bound) | (boston_df[feature] > upper_bound)])
#     print(f"{feature}: {num_outliers}")


from sklearn.datasets import load_boston
import pandas as pd
boston=load_boston()
boston_df=pd.DataFrame(boston.data,columns=boston.feature_names)
boston_df['Price']=boston.target

import seaborn as sns
sns.boxplot(data=boston_df)

# or each continuous feature, calculate how many outliers there are using the 1.5 * IQR rule.
# (NumPy has a function to calculate Q1 and Q3.) Did it looks similar to the boxplot?
import numpy as np
q1=np.quantile(boston_df['Price'],0.25)
q3=np.quantile(boston_df['Price'],0.75)
iqr=q3-q1
outliers=boston_df[(boston_df['Price']<(q1-1.5*iqr)) | (boston_df['Price']>(q3+1.5*iqr))]
print(len(outliers))

# How would you deal with the outliers in each of these cases?
# Path: week_7/day-4/example.py
# Drop the outliers
boston_df.drop(outliers.index,inplace=True)
