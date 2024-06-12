from matplotlib import pyplot as plt
import numpy as np
months = []
for i in range(1, 13):
    months.append(i)

months = np.array(months)
monthly_sales = np.array([50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105])

plt.plot(months, monthly_sales, marker='o')
plt.xlabel("Months-->")
plt.ylabel("Monthly-Sales-->")
plt.title("Line Plot for Monthly-Sales")
plt.grid()
plt.savefig('monthly_Sales_Graph.png')