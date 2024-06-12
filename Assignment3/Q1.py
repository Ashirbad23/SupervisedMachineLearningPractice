import pandas as pd
dataSet = pd.read_csv('data.csv', index_col=False)
print(dataSet.shape)
print(dataSet.head())
print(dataSet.info())

print(dataSet.isna().sum())

# Fill the missing value with Mean value
mean_value = dataSet["Calories"].mean()
print(mean_value)
dataSet['Calories'] = dataSet['Calories'].fillna(mean_value)
print(dataSet.isna().sum())

# Removing the row of missing value
dataSet.dropna(inplace=True)
print(dataSet.isna().sum())

# Change to date format
dataSet['Date'] = pd.to_datetime(dataSet['Date'], format="mixed")
print(dataSet)

#replace the wrong values
for x in dataSet.index:
    if((dataSet.loc[x, "Duration"] > 60)):
        dataSet.loc[x, "Duration"] = 60

print(dataSet)

#Replace duplicates
print(dataSet.duplicated().sum())
dataSet.drop_duplicates(inplace=True)
print(dataSet.duplicated().sum())

print(dataSet.iloc[5:15, :])
dataSet.to_csv('clean_data.csv', index=False)