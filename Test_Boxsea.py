import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Sample data
df = pd.DataFrame({
    "Category": ["A", "A", "A", "B", "B", "B"],
    "Values": [10, 15, 12, 30, 35, 32]
})

# Modern theme
sns.set_theme(
    style="whitegrid",
    context="talk"
)

plt.figure(figsize=(10, 6))

# Box plot
ax = sns.boxplot(
    x="Category",
    y="Values",
    data=df,
    palette="viridis",
    width=0.5,
    linewidth=2
)

# Overlay data points
sns.stripplot(
    x="Category",
    y="Values",
    data=df,
    color="black",
    alpha=0.6,
    size=8
)

plt.title(
    "Category Distribution Analysis",
    fontsize=20,
    fontweight="bold",
    pad=20
)

plt.xlabel("Category", fontsize=14)
plt.ylabel("Values", fontsize=14)

# Remove unnecessary borders
sns.despine()

plt.tight_layout()
plt.show()