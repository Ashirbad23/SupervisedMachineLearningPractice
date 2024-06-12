# from hmac import new
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/selva86/datasets/master/mpg_ggplot2.csv")
print(df.info())
print(df.shape)

new_col = df.groupby("class").size()
print(type(new_col))

plt.figure(figsize=(10, 6))
plt.pie(new_col, labels=new_col.index) 
plt.show()