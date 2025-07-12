from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load trained model
model_path = os.path.join("model", "best_model.pkl")
features_path = os.path.join("model", "features.pkl")

with open(model_path, "rb") as f:
    model = pickle.load(f)

with open(features_path, "rb") as f:
    features_list = pickle.load(f)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        form = request.form
        input_dict = {}

        # Raw inputs from form
        input_dict['team'] = float(form['team'])
        input_dict['targeted_productivity'] = float(form['targeted_productivity'])
        input_dict['smv'] = float(form['smv'])
        input_dict['wip'] = float(form['wip'])
        input_dict['over_time'] = float(form['over_time'])
        input_dict['incentive'] = float(form['incentive'])
        input_dict['idle_time'] = float(form['idle_time'])
        input_dict['idle_men'] = float(form['idle_men'])
        input_dict['no_of_style_change'] = float(form['no_of_style_change'])
        input_dict['no_of_workers'] = float(form['no_of_workers'])

        # One-hot encoded fields
        quarter = 'Q2' if form.get('quarter_Q2') == '1' else 'Q1'
        dept = 'sewing' if form.get('department_sweing') == '1' else 'finishing'

        input_dict['quarter_' + quarter] = 1
        input_dict['department_' + dept] = 1

        # Ensure full 21 feature list
        final_input = [input_dict.get(col, 0) for col in features_list]

        prediction = model.predict([final_input])
        output = round(prediction[0], 2)

        return render_template("index.html", prediction_text=f"Predicted Productivity: {output}")

    except Exception as e:
        return render_template("index.html", prediction_text=f"Error: {e}")

if __name__ == "__main__":
    import webbrowser
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=True)
