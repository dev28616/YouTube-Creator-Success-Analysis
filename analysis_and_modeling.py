import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
import numpy as np

def fetch_data_from_db(db_user, db_password, db_host, db_port, db_name, table_name):
    """Connects to the PostgreSQL database and fetches the data into a DataFrame."""
    print("Connecting to database...")
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    query = f"SELECT * FROM {table_name};"
    df = pd.read_sql(query, engine)
    print("Successfully fetched data from PostgreSQL.")
    return df

def perform_eda(df):
    """Performs Exploratory Data Analysis and generates key visualizations."""
    print("\n--- Starting Exploratory Data Analysis (EDA) ---")

    # 1. Correlation Heatmap
    # We select only numeric columns for the correlation matrix.
    numeric_cols = df.select_dtypes(include=np.number).columns
    plt.figure(figsize=(12, 8))
    sns.heatmap(df[numeric_cols].corr(), annot=True, cmap='viridis', fmt='.2f')
    plt.title('Correlation Heatmap of Numeric Features')
    plt.savefig('correlation_heatmap.png')
    plt.show()
    print("Saved correlation_heatmap.png")
    
    # 2. Average Views by Day of the Week
    # Order the days of the week correctly
    day_order = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    plt.figure(figsize=(10, 6))
    sns.barplot(x='day_of_week', y='view_count', data=df, order=day_order, palette='plasma')
    plt.title('Average Views by Day of Week Published')
    plt.ylabel('Average View Count')
    plt.xlabel('Day of the Week')
    plt.savefig('avg_views_by_day.png')
    plt.show()
    print("Saved avg_views_by_day.png")

    # 3. Scatter plot of Title Length vs. Views
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='title_length', y='view_count', data=df, alpha=0.5)
    # Use a log scale for y-axis to better visualize relationship with wide-ranging view counts
    plt.yscale('log')
    plt.title('Title Length vs. View Count (Log Scale)')
    plt.ylabel('View Count (Log Scale)')
    plt.xlabel('Title Length (Characters)')
    plt.savefig('title_length_vs_views.png')
    plt.show()
    print("Saved title_length_vs_views.png")


def build_predictive_model(df):
    """Builds a RandomForest model to predict view_count and identifies key features."""
    print("\n--- Building Predictive Model ---")

    # 1. Feature Selection
    # Select the features (X) and the target variable (y)
    features = [
        'title_length', 'description_length', 'tags_count',
        'days_since_published', 'engagement_rate',
        'title_contains_question', 'title_contains_money_keyword'
    ]
    target = 'view_count'

    X = df[features]
    y = df[target]

    # 2. Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(f"Data split into {len(X_train)} training samples and {len(X_test)} testing samples.")

    # 3. Model Training
    # We use RandomForest because it's powerful and gives feature importances.
    model = RandomForestRegressor(n_estimators=100, random_state=42, n_jobs=-1)
    print("Training RandomForest Regressor...")
    model.fit(X_train, y_train)
    print("Model training complete.")

    # 4. Model Evaluation
    y_pred = model.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"\nModel Performance:")
    print(f"Mean Absolute Error (MAE): {mae:,.0f}")
    print(f"R-squared (R2 Score): {r2:.2f}")

    # 5. Feature Importance
    importances = pd.DataFrame({
        'feature': features,
        'importance': model.feature_importances_
    }).sort_values('importance', ascending=False)
    
    print("\n--- Key Drivers of Video Success ---")
    print(importances)

    # Visualize Feature Importances
    plt.figure(figsize=(10, 6))
    sns.barplot(x='importance', y='feature', data=importances, palette='rocket')
    plt.title('Feature Importance for Predicting YouTube Views')
    plt.xlabel('Importance Score')
    plt.ylabel('Feature')
    plt.tight_layout()
    plt.savefig('feature_importance.png')
    plt.show()
    print("Saved feature_importance.png")


if __name__ == '__main__':
    # --- Database Connection Details ---
    # Replace with your PostgreSQL credentials
    db_user = 'postgres'
    db_password = '722161' 
    db_host = 'localhost'
    db_port = '5432'
    db_name = 'youtube_project'
    table_name = 'videos'
    
    # Step 1: Fetch the data
    try:
        df_videos = fetch_data_from_db(db_user, db_password, db_host, db_port, db_name, table_name)
        
        # Step 2: Perform EDA
        perform_eda(df_videos)

        # Step 3: Build the predictive model
        build_predictive_model(df_videos)

    except Exception as e:
        print(f"An error occurred during the process: {e}")
