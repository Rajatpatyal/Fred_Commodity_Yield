import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Generate sample data
np.random.seed(42)

df = pd.DataFrame({
    "Value": np.concatenate([
        np.random.normal(0, 1, 500),
        np.random.normal(2, 1.5, 500)
    ]),
    "Group": ["Group A"] * 500 + ["Group B"] * 500
})

# Modern theme
sns.set_theme(
    style="darkgrid",
    context="talk"
)

plt.figure(figsize=(12, 7))

# Density plot
sns.kdeplot(
    data=df,
    x="Value",
    hue="Group",
    fill=True,
    alpha=0.5,
    linewidth=3,
    common_norm=False
)

plt.title(
    "Distribution Comparison by Group",
    fontsize=20,
    fontweight="bold",
    pad=20
)

plt.xlabel("Value", fontsize=14)
plt.ylabel("Density", fontsize=14)

sns.despine()

plt.tight_layout()
plt.show()