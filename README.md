# Heart Attack Prediction API - GCP Deployed Machine Learning Service

This project was developed during a hackathon focused on **deploying Machine Learning models at scale** using modern cloud and MLOps tools.

It is a full pipeline from model training to deployment, offering an **API that predicts the likelihood of heart disease** based on patient data. The model is trained locally using scikit-learn and deployed on **Google Cloud Platform (GCP)** with a **Flask API** interface and **Swagger documentation** for easy access and testing.

---

## Tools & Technologies Used

| Category        | Tools                                                       |
|----------------|-------------------------------------------------------------|
| **Languages**   | Python                                                      |
| **ML Frameworks** | scikit-learn, pandas, numpy                             |
| **MLOps**       | joblib (model persistence), Flask, Flasgger                |
| **Cloud**       | Google Cloud Platform (App Engine / Compute Engine)        |
| **Other Skills**| API design, Data Preprocessing, Model Evaluation, Swagger UI |

---

## What the Model Does

This Decision Tree Classifier predicts whether a patient is likely to suffer from heart disease based on clinical parameters such as:

- Age, Sex
- Chest pain type (`cp`)
- Resting blood pressure (`trtbps`)
- Cholesterol level (`chol`)
- Fasting blood sugar, ECG results, Exercise-induced angina
- Maximum heart rate, ST depression, number of major vessels, thalassemia

---

## Project Workflow

### 🔹 1. Data Preprocessing & Training (`train_pipeline.py`)
- Reads and cleans the dataset.
- Splits data into train/test sets.
- Applies preprocessing:
  - Missing value imputation
  - Encoding categorical variables
- Trains a `DecisionTreeClassifier`
- Evaluates accuracy
- Saves model pipeline using `joblib`.

### 🔹 2. API Development (`app.py`)
- Uses **Flask** to create REST endpoints:
  - `GET /` → Health check
  - `POST /predict` → Accepts JSON with patient data and returns prediction
- Swagger documentation is automatically generated with **Flasgger**.
- Loads the saved pipeline and performs inference in real time.

### 🔹 3. Cloud Deployment
- The API is containerized and deployed on **Google Cloud Platform**, enabling scalable and public access to the ML model.

---

## Skills

- **End-to-End ML Project Ownership**: From raw CSV to a production-ready API.
- **MLOps Foundations**: Model serialization, pipeline creation, and clean separation of training/inference code.
- **Cloud Deployment**: Successfully deployed a Python-based ML microservice to GCP.
- **Clean API Design & Documentation**: Used Flasgger to auto-generate Swagger docs for non-technical stakeholders.
- **Robust Error Handling**: Gracefully manages model load failures and invalid input.

---
