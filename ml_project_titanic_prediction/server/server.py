from flask import Flask, request, redirect, url_for, render_template, jsonify
import numpy as np
import util

app = Flask(__name__)


@app.route('/get_columns', methods=['GET'])
def get_columns():
    response = jsonify({
        'columns': util.get_columns()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/predict', methods=['GET', 'POST'])
def predict_titanic_survival():
    pclass = int(request.form['pclass'])
    age = int(request.form['age'])
    sibsp = int(request.form['sibsp'])
    parch = int(request.form['parch'])
    fare = float(request.form['fare'])
    sex = request.form['sex']
    embarked = request.form['embarked']

    # Get the prediction result
    survival_prediction = util.get_prediction(pclass, age, sibsp, parch, fare, sex, embarked)

    # Convert to native Python types if necessary
    if isinstance(survival_prediction, (np.int32, np.int64)):
        survival_prediction = int(survival_prediction)  # Convert NumPy int to Python int
    elif isinstance(survival_prediction, np.float32):
        survival_prediction = float(survival_prediction)  # Convert NumPy float to Python float

    response = jsonify({
        'survival_prediction': survival_prediction
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == "__main__":
    print("Starting python Flask Server For Titanic Survival Prediction")
    util.load_saved_artifacts()
    app.run(debug=True)