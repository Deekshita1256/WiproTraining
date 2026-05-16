import matplotlib.pyplot as plt
import seaborn as sns

# Load the built-in dataset
tips = sns.load_dataset('tips')

# 1. Histogram with KDE line
# Note: displot returns a FacetGrid, color maps to plot elements
sns.displot(data=tips, x="total_bill", kde=True, color="darkblue")
plt.title("Total Bill Distribution")
plt.show()

# 2. JointPlot with a regression line
sns.jointplot(data=tips, x="total_bill", y="tip", kind="reg", color="purple")
plt.show()

# 3. BoxPlot by day and smoker status
plt.figure(figsize=(8, 5))
sns.boxplot(data=tips, x="day", y="total_bill", hue="smoker", palette="Set2")
plt.title("Total Bill by Day and Smoker Status")
plt.show()
