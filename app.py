from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained KNN model
knn_model = joblib.load('knn_model.pkl')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    # Convert data to a numpy array for prediction
    user_input = np.array([[data['age'], data['blood_pressure'], data['specific_gravity'], data['albumin'],
                            data['sugar'], data['red_blood_cells'], data['pus_cell'], data['pus_cell_clumps'],
                            data['bacteria'], data['blood_glucose_random'], data['blood_urea'], data['serum_creatinine'],
                            data['sodium'], data['potassium'], data['haemoglobin'], data['packed_cell_volume'],
                            data['white_blood_cell_count'], data['red_blood_cell_count'], data['hypertension'],
                            data['diabetes_mellitus'], data['coronary_artery_disease'], data['appetite'],
                            data['peda_edema'], data['aanemia']]])
    # Make the prediction
    prediction = knn_model.predict(user_input)
    if prediction[0] == 0:
        result = 'Kidney Disease Detected'
    else:
        result = 'No Kidney Disease Detected'
    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
