import pandas as pd
details = pd.read_csv("person_details.csv")
# (A)
print(details.iloc[0:3, 0:2],'\n')
# (B)
print(details.loc[(details['Living Expenses']>3500)],'\n')
# (C)
print(details.loc[(details['Gender'] == 'Female') & ((details['City'] == 'New York') | (details['City'] == 'Los Angeles')), ['Name', 'Age']],'\n')
# (D)
print(details.iloc[2:8],'\n')

