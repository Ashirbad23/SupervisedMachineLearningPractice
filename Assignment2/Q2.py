import pandas as pd
details = pd.read_csv("person_details.csv")
# print(details)
data = {'Name': ["Ashirbad", "Ohm"], 
        'Gender': ["Male", "Male"], 
        'Age': [19, 18], 
        'City': ["Bhubaneswar", "Kotpad"], 
        'Living Expenses': [4000, 5000]}
data1 = pd.DataFrame(data)
np = pd.concat([details, data1], ignore_index = True)
print(np.tail())
# data1.to_csv("person_details.csv", mode='a', index=False, header=False)
np.to_csv("person_details.csv", index=False)