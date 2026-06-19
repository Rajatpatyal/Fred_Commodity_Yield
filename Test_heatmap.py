import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)

returns = pd.DataFrame({
    "Gold": np.random.normal(0, 1, 500),
    "Silver": np.random.normal(0, 1.2, 500),
    "Oil": np.random.normal(0, 1.8, 500),
    "Copper": np.random.normal(0, 1.5, 500),
    "USD": np.random.normal(0, 0.8, 500)
})

corr = returns.corr()

plt.figure(figsize=(12, 8))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    center=0,
    vmin=-1,
    vmax=1,
    square=True,
    linewidths=0.5
)

plt.title(
    "Asset Correlation Dashboard",
    fontsize=22,
    fontweight="bold"
)

plt.tight_layout()
plt.show()