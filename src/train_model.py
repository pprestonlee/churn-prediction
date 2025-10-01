import os
import joblib
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
try:
    from xgboost import XGBClassifier
    xgb_available = True
except ImportError:
    xgb_available = False

from data_prep import load_data, clean_data, engineer_features, build_preprocessor

def train_evaluate_model(
    model_type="logistic",  # "logistic", "random_forest", "xgboost"
    data_path="../data/raw/churn_v1.csv",
    model_path="../models/churn_pipeline.pkl",
    test_size=0.2,
    random_state=42
):
    # Load and prepare data
    df = load_data(data_path)
    df = clean_data(df)
    df = engineer_features(df)

    X = df.drop(columns=["churn_value"])
    y = df["churn_value"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    # Preprocessing pipeline
    preprocessor = build_preprocessor()

    # Select model
    if model_type == "logistic":
        model = LogisticRegression(max_iter=1000)
    elif model_type == "random_forest":
        model = RandomForestClassifier(
            random_state=random_state,
            class_weight="balanced"
        )
    elif model_type == "xgboost" and xgb_available:
        model = XGBClassifier(
            scale_pos_weight=(y == 0).sum() / (y == 1).sum(),
            eval_metric="logloss",
            random_state=random_state
        )
    else:
        raise ValueError(f"Unsupported model_type: {model_type}")

    # Full pipeline
    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", model)
    ])

    # Train
    pipeline.fit(X_train, y_train)

    # Predict
    y_pred = pipeline.predict(X_test)

    # Metrics
    print(f"=== {model_type} evaluation metrics ===")
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Precision:", precision_score(y_test, y_pred))
    print("Recall:", recall_score(y_test, y_pred))
    print("F1 Score:", f1_score(y_test, y_pred))
    print("\nClassification Report:\n", classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

    # Save pipeline (preprocessing + model)
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(pipeline, model_path)
    print(f"\nPipeline saved to {model_path}")

    return pipeline

if __name__ == "__main__":
    pipeline = train_evaluate_model(model_type="random_forest")