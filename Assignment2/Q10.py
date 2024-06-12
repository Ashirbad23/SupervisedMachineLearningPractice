import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

data = {
'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
'Sales_Revenue': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105]
}

df = pd.DataFrame(data)

sb.lineplot(x="Month", y="Sales_Revenue", data=df, marker='*', markers=True, markersize=10)

plt.savefig("Monthly_Revenue_Line_Plot.png")
# plt.show()
