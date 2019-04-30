# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv("wmap_n.csv")
data.head()

weights = data.pivot_table("w","y", "x" )

plt.title("Weights map")
sns.heatmap(weights, annot=True, fmt=".0f", linewidths=0.5, linecolor="Gray")
plt.show()
