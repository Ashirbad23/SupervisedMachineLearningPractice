import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('ComputerSales.csv')
print(df.shape)
print(df.isna().sum())
print(df.info())
print(df.describe())

def xylabel(x, y='Frequency'):
    plt.xlabel(x)
    plt.ylabel(y)

plt.subplot(2, 3, 1)
plt.hist(df['Sale ID'], edgecolor='black')
xylabel('Sale ID')

plt.subplot(2, 3, 2)
plt.hist(df['Age'], edgecolor='black')
xylabel('Age')

plt.subplot(2, 3, 3)
plt.hist(df['Sale Price'], edgecolor='black')
xylabel('Sale Price')

plt.subplot(2, 3, 4)
plt.hist(df['Profit'], edgecolor='black')
xylabel('Profit')

plt.subplot(2, 3, 5)
plt.hist(df['Year'])
xylabel('Year')

plt.tight_layout()
plt.show()