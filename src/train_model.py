from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from data_prep import load_data, clean_data, engineer_features, preprocess_data
import pandas as pd
import joblib
import os

def train_evaluate_model(data_path="../data/raw/churn_v1.csv",
                        model_path="../models/lr_model.pkl",
                        pipeline_path="../models/preprocessor.pkl"):
    df = load_data(data_path)
    df = clean_data(df)
    df = engineer_features(df)

    X = df.drop(columns=["churn_value"])
    y = df["churn_value"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    preprocessor = preprocess_data(X_train)

    X_train_processed = preprocessor.fit_transform(X_train)
    X_test_processed = preprocessor.transform(X_test)

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train_processed, y_train)

    y_pred = model.predict(X_test_processed)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    os.makedirs(os.path.dirname(pipeline_path), exist_ok=True)

    joblib.dump(model, model_path)
    joblib.dump(preprocessor, pipeline_path)

    print(f"Model saved to {model_path}")
    print(f"Preprocessor saved to {pipeline_path}")

    return model, preprocessor

if __name__ == "__main__":
    train_evaluate_model()