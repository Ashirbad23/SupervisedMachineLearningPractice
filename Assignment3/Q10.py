import pandas as pd
from sklearn.preprocessing import LabelEncoder as le

df = pd.read_csv("https://raw.githubusercontent.com/gauraviiita/Supervised_ML/main/Datasets/Chapter_2/Housing.csv")
print(df.head())

print(df.info())

for x in df:
    if(df[x].dtype==object):
        df[x]=le().fit_transform(df[x])

print(df.info())

df.to_csv("clean_data2.csv")