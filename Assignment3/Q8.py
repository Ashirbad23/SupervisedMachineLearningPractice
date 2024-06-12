import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ComputerSales.csv')
plt.scatter(df['Sale Price'], df['Profit'])
plt.show()