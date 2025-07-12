import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Load data
file_path = os.path.join("dataset", "garments_worker_productivity.csv")
data = pd.read_csv(file_path)

# Show basic info
print("Shape:", data.shape)
print(data.head())
print(data.info())
print("Null values:\n", data.isnull().sum())

# Correlation heatmap
plt.figure(figsize=(12, 8))
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap='coolwarm', linewidths=0.5)
plt.title("Correlation Matrix")
plt.savefig("visuals/correlation_heatmap.png")  # Save to visuals folder
plt.show()
