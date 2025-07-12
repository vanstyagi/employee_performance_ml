import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pickle

# Load and preprocess again for safety
file_path = os.path.join("dataset", "garments_worker_productivity.csv")
data = pd.read_csv(file_path)
data['wip'] = data['wip'].fillna(data['wip'].median())
data.drop('date', axis=1, inplace=True)
data = pd.get_dummies(data, columns=['quarter', 'department', 'day'], drop_first=True)

X = data.drop('actual_productivity', axis=1)
y = data['actual_productivity']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 1️⃣ Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
lr_r2 = r2_score(y_test, lr_pred)
print("Linear Regression R² Score:", lr_r2)

# 2️⃣ Random Forest
rf = RandomForestRegressor()
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
rf_r2 = r2_score(y_test, rf_pred)
print("Random Forest R² Score:", rf_r2)

# 3️⃣ XGBoost
xgb = XGBRegressor()
xgb.fit(X_train, y_train)
xgb_pred = xgb.predict(X_test)
xgb_r2 = r2_score(y_test, xgb_pred)
print("XGBoost R² Score:", xgb_r2)

# 4️⃣ Save the best model
best_model = max([(lr_r2, lr), (rf_r2, rf), (xgb_r2, xgb)], key=lambda x: x[0])[1]

with open("model/best_model.pkl", "wb") as f:
    pickle.dump(best_model, f)

print("Best model saved to model/best_model.pkl")
with open("model/features.pkl", "wb") as f:
    pickle.dump(X_train.columns.tolist(), f)