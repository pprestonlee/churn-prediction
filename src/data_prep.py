from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pandas as pd
import joblib
import os

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def engineer_features(df):
    df = df.drop(columns=['customer_id', 'location_id', 'country', 'state', 'city', 'zip_code', 'lat_long', 'latitude', 'longitude',
       'population_id', 'pop', 'service_id', 'status_id', 'customer_status', 'churn_label', 'churn_score', 'cltv', 'churn_category',
       'churn_reason'])
    return df

def preprocess_data(df):
    binary_yn = ['under_30', 'senior_citizen', 'married', 'dependents', 'referred_friend', 'phone_service', 'multiple_lines',
              'internet_service', 'online_security', 'online_backup', 'device_protection', 'premium_tech_support', 'streaming_tv',
              'streaming_movies', 'streaming_music', 'unlimited_data', 'paperless_billing']
    categorical = ['offer', 'internet_type', 'contract', 'payment_method']
    continuous = ['age', 'num_dependents', 'num_referrals', 'tenure_months', 'avg_monthly_long_distance_charge', 'avg_monthly_gb_download', 
                  'monthly_charge', 'total_charges', 'total_refunds', 'total_extra_data_charges', 'total_long_distance_charges', 'total_revenue', 
                  'satisfaction_score']
    
    df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})
    for col in binary_yn:
        df[col] = df[col].map({'Yes': 1, 'No': 0})
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), continuous),
            ('cat', OneHotEncoder(), categorical)
        ], remainder='passthrough'
    )
    return preprocessor

def main(input_file: str, output_file: str, pipeline_file: str):
    df = load_data(input_file)
    df = clean_data(df)
    df = engineer_features(df)
    
    preprocessor = preprocess_data(df)
    
    X = df.drop(columns=['churn_value'])
    y = df['churn_value']
    
    X_processed = preprocessor.fit_transform(X)
    
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    joblib.dump(preprocessor, pipeline_file)
    os.makedirs(os.path.dirname(pipeline_file), exist_ok=True)
    
    pd.DataFrame(X_processed).to_csv(output_file, index=False)
    joblib.dump(preprocessor, pipeline_file)

    print(f"Preprocessed data saved to {output_file}")
    print(f"Preprocessing pipeline saved to {pipeline_file}")

if __name__ == "__main__":
    main(
        input_file="../data/raw/churn_v1.csv",
        output_file="../data/processed/processed_v1.csv",
        pipeline_file="../models/preprocessor.pkl"
    )