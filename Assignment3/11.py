import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the dataset (you can replace this with your actual dataset)
url = "https://raw.githubusercontent.com/selva86/datasets/master/mtcars.csv"
df = pd.read_csv(url)

# Exclude non-numeric columns (e.g., 'model', 'cars', 'carname')
numeric_df = df.drop(columns=['cars', 'carname'])

# Calculate the correlation matrix
corr_matrix = numeric_df.corr()

# Plot the heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix Heatmap")
plt.show()
