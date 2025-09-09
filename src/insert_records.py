import sqlite3
import pandas as pd

def insert_records():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('../data/churn.db')
        cursor = conn.cursor()

        # Insert raw demographics.csv records
        demographics = pd.read_csv('../data/raw/telco/demographics.csv')
        for row in demographics.itertuples(index=False):
            cursor.execute("""
                        INSERT INTO demographics (customer_id, count, gender, age, under_30, senior_citizen, married, dependents, num_dependents)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, row)
            
        location = pd.read_csv('../data/raw/telco/location.csv')
        for row in location.itertuples(index=False):
            cursor.execute("""
                        INSERT INTO location (location_id, customer_id, count, country, state, city, zip_code, lat_long, latitude, longitude)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, row)

        # Insert raw population.csv records
        population = pd.read_csv('../data/raw/telco/population.csv')
        for row in population.itertuples(index=False):
            cursor.execute("""
                        INSERT INTO population (population_id, zip_code, pop)
                        VALUES (?, ?, ?)
                        """, row)
            
        services = pd.read_csv('../data/raw/telco/services.csv')
        for row in services.itertuples(index=False):
            cursor.execute("""
                        INSERT INTO services (
                            'service_id',
                            'customer_id',
                            'count',
                            'quarter',
                            'referred_friend',
                            'num_referrals',
                            'tenure_months',
                            'offer',
                            'phone_service',
                            'avg_monthly_long_distance_charge',
                            'multiple_lines',
                            'internet_service',
                            'internet_type',
                            'avg_monthly_gb_download',
                            'online_security',
                            'online_backup',
                            'device_protection',
                            'premium_tech_support',
                            'streaming_tv',
                            'streaming_movies',
                            'streaming_music',
                            'unlimited_data',
                            'contract',
                            'paperless_billing',
                            'payment_method',
                            'monthly_charge',
                            'total_charges',
                            'total_refunds',
                            'total_extra_data_charges',
                            'total_long_distance_charges',
                            'total_revenue'
                        )
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, row)
            
        status = pd.read_csv('../data/raw/telco/status.csv')
        for row in status.itertuples(index=False):
            cursor.execute("""
                        INSERT INTO status (
                           status_id, 
                           customer_id, 
                           count, 
                           quarter, 
                           satisfaction_score,
                           customer_status,
                           churn_label,
                           churn_value,
                           churn_score,
                           cltv,
                           churn_category,
                           churn_reason)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                        """, row)
        conn.commit()
        print("Records inserted successfully!")
        conn.close()
        # Insert sample records into demographics table
    except sqlite3.Error as e:
        print(f"Error inserting records: {e}")
        raise

insert_records()