-- Drop if already existing tables
DROP TABLE IF EXISTS demographics;
DROP TABLE IF EXISTS location;
DROP TABLE IF EXISTS population;
DROP TABLE IF EXISTS services;
DROP TABLE IF EXISTS status;

-- Create demographics table
CREATE TABLE demographics (
    customer_id TEXT PRIMARY KEY,
    gender TEXT,
    age INTEGER,
    under_30 TEXT,
    senior_citizen TEXT,
    married TEXT,
    dependents TEXT,
    num_dependents INTEGER
);

CREATE TABLE location (
    location_id TEXT PRIMARY KEY,
    customer_id TEXT,
    country TEXT,
    state TEXT,
    city TEXT,
    zip_code TEXT,
    latitude REAL,
    longitude REAL,
    FOREIGN KEY (customer_id) REFERENCES demographics(customer_id)
);

CREATE TABLE population (
    population_id INTEGER PRIMARY KEY,
    zip_code TEXT,
    pop INTEGER
);

CREATE TABLE services (
    service_id TEXT PRIMARY KEY,
    customer_id TEXT,
    referred_friend TEXT,
    num_referrals INTEGER,
    tenure_months INTEGER,
    offer TEXT,
    phone_service TEXT,
    avg_monthly_long_distance_charge REAL,
    multiple_lines TEXT,
    internet_service TEXT,
    internet_type TEXT,
    avg_monthly_gb_download REAL,
    online_security TEXT,
    online_backup TEXT,
    device_protection TEXT,
    premium_tech_support TEXT,
    streaming_tv TEXT,
    streaming_movies TEXT,
    streaming_music TEXT,
    unlimited_data TEXT,
    contract TEXT,
    paperless_billing TEXT,
    payment_method TEXT,
    monthly_charge REAL,
    total_charges REAL
    total_refunds REAL,
    total_extra_data_charges REAL,
    total_long_distance_charges REAL,
    total_revenue REAL,
    FOREIGN KEY (customer_id) REFERENCES demographics(customer_id)
);

CREATE TABLE status (
    status_id TEXT PRIMARY KEY,
    customer_id TEXT,
    satisfaction_score INTEGER,
    churned TEXT,
    churn_score INTEGER,
    CLTV INTEGER,
    last_interaction TEXT,
    churn_category TEXT,
    churn_reason TEXT,
    FOREIGN KEY (customer_id) REFERENCES demographics(customer_id)
);

