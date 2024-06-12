import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder as le

data = pd.read_csv('clean_data2.csv')

print(data.info())

Y = data.iloc[: ,0]
# print(Y)
X = data.iloc[: ,1:]
# print(X)

train_X, test_X, train_Y, test_Y = train_test_split(X, Y, test_size=0.3)
print(test_X.shape)
print(train_X.shape)
print(test_Y.shape)
print(train_Y.shape)