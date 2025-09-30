from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
import joblib, os, pandas as pd

from data_prep import load_data, clean_data, engineer_features, build_preprocessor

def train_evaluate_model(
                        data_path="../data/raw/churn_v1.csv",
                        model_path="../models/lr_pipeline.pkl"
                        ):
    df = load_data(data_path)
    df = clean_data(df)
    df = engineer_features(df)

    X = df.drop(columns=["churn_value"])
    y = df["churn_value"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1, stratify=y
    )

    preprocessor = build_preprocessor()
    pipeline = Pipeline([
        ("preprocessor", preprocessor),
        ("model", LogisticRegression(max_iter=1000))
    ])

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(pipeline, model_path)
    print(f"Pipeline (preprocessing + model) saved to {model_path}")

    return pipeline

if __name__ == "__main__":
    train_evaluate_model()
