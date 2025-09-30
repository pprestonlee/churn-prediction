from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def clean_data(df):
    df = df.dropna()
    df = df.drop_duplicates()
    return df

def engineer_features(df):
    drop=['customer_id', 'location_id', 'country', 'state', 'city', 'zip_code', 'lat_long', 'latitude', 'longitude',
       'population_id', 'pop', 'service_id', 'status_id', 'satisfaction_score', 'total_charges', 'total_refunds', 'total_extra_data_charges', 'total_long_distance_charges',
       'total_revenue', 'customer_status', 'churn_label', 'churn_score', 'cltv', 'churn_category', 'churn_reason']
    df = df[[col for col in df.columns if col not in drop]]
    
    binary_yn = ['under_30', 'senior_citizen', 'married', 'dependents', 'referred_friend', 'phone_service', 'multiple_lines',
              'internet_service', 'online_security', 'online_backup', 'device_protection', 'premium_tech_support', 'streaming_tv',
              'streaming_movies', 'streaming_music', 'unlimited_data', 'paperless_billing']
    
    df['gender'] = df['gender'].map({'Male': 1, 'Female': 0})
    for col in binary_yn:
        df[col] = df[col].map({'Yes': 1, 'No': 0})
    return df

def build_preprocessor():
    categorical = ['offer', 'internet_type', 'contract', 'payment_method']
    continuous = ['age', 'num_dependents', 'num_referrals', 'tenure_months', 'avg_monthly_long_distance_charge', 'avg_monthly_gb_download', 
                  'monthly_charge']
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), continuous),
            ('cat', OneHotEncoder(), categorical)
        ], remainder='passthrough'
    )
    return preprocessor
