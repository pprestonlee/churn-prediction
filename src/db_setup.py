# db_setup.py
import sqlite3
from pathlib import Path

def create_database():
    try:
        # Create a new SQLite database (or connect to an existing one)
        conn = sqlite3.connect('../data/churn.db')
        print("Database created successfully!")
        conn.close()
        return conn
    except sqlite3.Error as e:
        print(f"Error creating database: {e}")
        raise
            

def create_tables():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('../data/churn.db')
        cursor = conn.cursor()

        # Read SQL script from file - /sql
        sql_path = Path('../sql/create_tables.sql')
        with open(sql_path, 'r') as f:
            sql_script = f.read()

        # Execute SQL script to create tables
        cursor.executescript(sql_script)
        conn.commit()
        print("Tables created successfully!")
        conn.close()
        return conn
    except sqlite3.Error as e:
        print(f"Error creating tables: {e}")
        raise

create_database()
create_tables()