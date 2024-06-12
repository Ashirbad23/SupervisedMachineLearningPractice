import seaborn as sns
import matplotlib.pyplot as plt

# Sample data
tips = sns.load_dataset("tips")
print(tips)

# Create scatter plot with different markers for each tip amount
sns.lineplot(x="total_bill", y="tip", hue="sex", style="sex",
                data=tips, markers=["o", "s"])  # Set markers for each sex

plt.show()
