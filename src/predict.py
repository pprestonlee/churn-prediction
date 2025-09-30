from data_prep import engineer_features
import pandas as pd
import joblib
import os

def load_artifacts(pipeline_path="../models/lr_pipeline.pkl"):
    if not os.path.exists(pipeline_path):
        raise FileNotFoundError("Pipeline file not found. Run train_model.py first.")
    
    pipeline = joblib.load(pipeline_path)
    return pipeline

def predict(data, pipeline):
    data = engineer_features(data)

    preprocessor = pipeline.named_steps['preprocessor']
    data = preprocessor.transform(data)

    model = pipeline.named_steps['model']

    predictions = model.predict(data)
    probabilities = model.predict_proba(data)[:, 1]
    return predictions, probabilities

def main():
    example_data = pd.DataFrame([
        {
            "gender": "Male",
            "under_30": "No",
            "senior_citizen": "No",
            "married": "Yes",
            "dependents": "No",
            "referred_friend": "Yes",
            "phone_service": "Yes",
            "multiple_lines": "No",
            "internet_service": "Yes",
            "online_security": "No",
            "online_backup": "No",
            "device_protection": "No",
            "premium_tech_support": "No",
            "streaming_tv": "Yes",
            "streaming_movies": "Yes",
            "streaming_music": "Yes",
            "unlimited_data": "Yes",
            "paperless_billing": "Yes",
            "offer": "Offer A",
            "internet_type": "Fiber Optic",
            "contract": "Month-to-Month",
            "payment_method": "Credit Card",
            "age": 35,
            "num_dependents": 0,
            "num_referrals": 2,
            "tenure_months": 12,
            "avg_monthly_long_distance_charge": 15.0,
            "avg_monthly_gb_download": 25.0,
            "monthly_charge": 70.35
        }
    ])

    # Load artifacts
    pipeline = load_artifacts()

    # Predict
    predictions, probabilities = predict(example_data, pipeline)

    print("Predictions (0=no churn, 1=churn):", predictions)
    print("Churn probabilities:", probabilities)

if __name__ == "__main__":
    main()
