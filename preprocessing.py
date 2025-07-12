import pandas as pd
import os
from sklearn.model_selection import train_test_split

# Load data
file_path = os.path.join("dataset", "garments_worker_productivity.csv")
data = pd.read_csv(file_path)

# 1️⃣ Handle null values
# Filling nulls in 'wip' with median (safe choice)
data['wip'] = data['wip'].fillna(data['wip'].median())

# 2️⃣ Drop 'date' column (not useful for modeling)
data.drop('date', axis=1, inplace=True)

# 3️⃣ Encode categorical columns using one-hot
data = pd.get_dummies(data, columns=['quarter', 'department', 'day'], drop_first=True)

# 4️⃣ Split features and target
X = data.drop('actual_productivity', axis=1)
y = data['actual_productivity']

# 5️⃣ Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("Preprocessing complete.")
print("Train shape:", X_train.shape)
print("Test shape:", X_test.shape)
