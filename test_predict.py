import pickle
import numpy as np

# Load model
model = pickle.load(open("model/best_model.pkl", "rb"))
features_list = pickle.load(open("model/features.pkl", "rb"))

# Sample manual test input (must match order of features_list)
sample_input = {
    'team': 5,
    'targeted_productivity': 0.8,
    'smv': 26,
    'wip': 1000,
    'over_time': 1200,
    'incentive': 300,
    'idle_time': 20,
    'idle_men': 5,
    'no_of_style_change': 2,
    'no_of_workers': 60,
    'quarter_Q2': 1,
    'department_sewing': 1
}

# Fill missing features with 0
final_input = [sample_input.get(col, 0) for col in features_list]

# Predict
final_input = np.array(final_input).reshape(1, -1)
pred = model.predict(final_input)
print("Prediction:", round(pred[0], 2))
