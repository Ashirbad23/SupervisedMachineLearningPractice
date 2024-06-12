import seaborn as sns
import matplotlib.pyplot as plt

iris_data = sns.load_dataset('iris')

sns.pairplot(iris_data)
plt.show()