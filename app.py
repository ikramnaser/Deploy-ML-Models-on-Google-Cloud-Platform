import os
import joblib
import pandas as pd
from flask import Flask, request, jsonify
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

# Load the trained pipeline
pipeline_filename = os.path.join('trained_model', 'heartattack_prediction_pipeline.pkl')
try:
    pipeline = joblib.load(pipeline_filename)
except Exception as e:
    print(f"Error loading pipeline file: {e}")
    raise SystemExit(1)

@app.route('/predict', methods=['POST'])
def predict():
    """
    Predict heart disease probability for new data
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          id: PredictInput
          properties:
            age:
              type: number
              description: Age of the person
            sex:
              type: string
              description: Gender (Male, Female)
            cp:
              type: number
              description: Chest pain type (0-3)
            trtbps:
              type: number
              description: Resting blood pressure (in mm Hg)
            chol:
              type: number
              description: Serum cholesterol in mg/dl
            fbs:
              type: number
              description: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
            restecg:
              type: number
              description: Resting electrocardiographic results (0-2)
            thalachh:
              type: number
              description: Maximum heart rate achieved
            exng:
              type: number
              description: Exercise induced angina (1 = yes, 0 = no)
            oldpeak:
              type: number
              description: ST depression induced by exercise relative to rest
            slp:
              type: number
              description: Slope of the peak exercise ST segment (0-2)
            caa:
              type: number
              description: Number of major vessels (0-4) colored by fluoroscopy
            thall:
              type: number
              description: Thalassemia (0-3)
    responses:
      200:
        description: Successfully predicted heart disease probability
        schema:
          id: PredictOutput
          properties:
            prediction:
              type: string
              description: Predicted heart disease status (No-Heart-Disease, Heart-Disease)
    """
    data = request.get_json()

    if not data:
        return jsonify({"error": "No input data provided"}), 400

    try:
        # Convert data to a DataFrame
        new_data = pd.DataFrame(data, index=[0])

        # Make predictions using the pipeline
        prediction = pipeline.predict(new_data)

        pred_mapping = {
            0: 'No-Heart-Disease',
            1: 'Heart-Disease'
        }

        predicted_class = pred_mapping[prediction[0]]

        return jsonify({"prediction": predicted_class})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
