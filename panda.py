import pandas as pd
studentData = {"Name": ["A", "B", "C"],
               "Age": [20, 23, 24],
               "City": ["Bhubaneswar", "India", "America"]}
data = pd.DataFrame(studentData)
print(data)
