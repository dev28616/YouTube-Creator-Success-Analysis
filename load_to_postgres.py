import pandas as pd
from sqlalchemy import create_engine
import re

def clean_data(df):
    """Performs initial data cleaning on the DataFrame."""
    # Convert 'published_at' to datetime objects
    df['published_at'] = pd.to_datetime(df['published_at'])

    # Ensure numeric columns are the correct type, filling NaNs with 0
    numeric_cols = ['view_count', 'like_count', 'comment_count']
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

    # Clean the 'tags' column: fill missing values with empty string
    df['tags'] = df['tags'].fillna('')

    # Clean text fields to remove potential problematic characters for SQL
    text_cols = ['title', 'description', 'tags']
    for col in text_cols:
        # Removes null characters which can cause copy errors in Postgres
        df[col] = df[col].str.replace('\x00', '', regex=False)

    print("Data cleaning complete.")
    return df

if __name__ == '__main__':
    # --- Database Connection Details ---
    # Replace with your PostgreSQL credentials
    db_user = 'postgres'
    db_password = '722161' 
    db_host = 'localhost'
    db_port = '5432'
    db_name = 'youtube_project'
    
    # The name of the table we will create in the database
    table_name = 'videos'

    # Create the database connection engine
    # The connection string format is: 'postgresql://user:password@host:port/dbname'
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')

    try:
        # Load the raw data from the CSV file
        df = pd.read_csv('youtube_finance_videos_raw.csv')
        print(f"Loaded {len(df)} rows from CSV.")

        # Clean the data
        cleaned_df = clean_data(df)

        # Load the cleaned DataFrame into the PostgreSQL table
        print(f"Loading data into '{table_name}' table...")
        # 'if_exists='replace'' will drop the table if it already exists and create a new one.
        # This is useful for re-running the script.
        cleaned_df.to_sql(table_name, engine, if_exists='replace', index=False)

        print("Successfully loaded data into PostgreSQL.")

    except FileNotFoundError:
        print("Error: 'youtube_finance_videos_raw.csv' not found. Make sure it's in the same directory.")
    except Exception as e:
        print(f"An error occurred: {e}")
