YouTube Success Analysis & Creator Playbook

<div align="center">

</div>

An end-to-end data science project that reverse-engineers the drivers of YouTube success for Indian finance creators. This project transforms raw data into a predictive engine and culminates in an interactive strategy playbook designed to empower creators with actionable, data-driven insights.

🎯 The Business Problem & The Solution
Problem: The YouTube creator space is saturated. New and existing creators in the high-value finance niche struggle to identify a content strategy that reliably drives growth. They often rely on intuition rather than data, leading to inconsistent results.

Solution: This project addresses the ambiguity by building a predictive model that quantifies the impact of various content attributes on viewership. The model's findings are distilled into a user-friendly interactive infographic, transforming complex data science into a simple, actionable checklist for any creator.

🚀 Live Infographic & Final Report
The key findings and strategic recommendations are presented in a live, single-page web application.

View the Live YouTube Creator Success Infographic at https://youtube-analyze.netlify.app/

📊 Key Insights & Recommendations
The analysis produced a clear, data-backed strategy for content creators. The model, with an R-squared of 0.72, identified audience engagement as the primary lever for growth.

1. Recommendation: Optimize for Engagement, Not Just Clicks
   The model shows that engagement_rate is the most critical factor in predicting a video's success. Creators should prioritize content that sparks conversation and community interaction.

2. Recommendation: Publish on Wednesday or Saturday to Boost Views by ~15%
   There is a clear, measurable advantage to publishing on specific days. On average, videos published mid-week and on the weekend align with peak audience availability, providing a significant initial viewership boost.

🛠️ Technical Architecture
Data Collection: A Python script leverages the YouTube Data API v3 to construct a unique dataset of 1,000+ videos from 20 top-tier channels.

Data Storage & Engineering: PostgreSQL serves as the data warehouse. SQL and Python were used to clean, transform, and engineer 8 new predictive features (e.g., engagement_rate, title_contains_money_keyword).

Predictive Modeling: A RandomForest Regressor was trained in Scikit-learn to predict view counts and quantify feature importance.

Data Visualization & Reporting: The final insights are presented in a responsive SPA built with HTML5, Tailwind CSS, and Chart.js.

💡 Scalability & Future Enhancements
This project serves as a robust proof-of-concept. The following steps could scale this solution into a production-level system:

Cloud Migration: Transition the entire pipeline to Google Cloud Platform (GCP). Store data in BigQuery for superior scalability and use Vertex AI for automated model training, evaluation, and deployment.

Advanced Feature Engineering: Incorporate more complex features by performing NLP sentiment analysis on video comments or using computer vision to analyze thumbnail effectiveness.

Real-time Creator Dashboard: Develop a full-stack web application where a creator could input their channel ID and receive a personalized, real-time report and content recommendations based on the model's analysis.

⚙️ Setup and Installation
To run this project locally, follow these steps:

Clone the repository:

git clone [https://github.com/](https://github.com/)dev28616/YouTube-Success-Analysis.git
cd YouTube-Success-Analysis

Set up a Python virtual environment:

python -m venv venv
source venv/bin/activate # On Windows, use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

(Note: You will need to create a requirements.txt file.)

Set up PostgreSQL:

Install and run a local PostgreSQL server.

Create a new database named youtube_project.

Run the Scripts:

Add your YouTube API Key to youtube_data_collector.py.

Add your PostgreSQL password to load_to_postgres.py and analysis_and_modeling.py.

Run the scripts in order:

python youtube_data_collector.py
python load_to_postgres.py
python analysis_and_modeling.py

📂 Project Structure
.
├── 📄 youtube_data_collector.py # Script to fetch data from YouTube API
├── 📄 load_to_postgres.py # Script to clean and load data into PostgreSQL
├── 📄 analysis_and_modeling.py # Script for EDA and building the ML model
├── 📄 index.html # The final interactive infographic/report
├── 🖼️ correlation_heatmap.png # Generated visualization
├── 🖼️ avg_views_by_day.png # Generated visualization
├── 🖼️ feature_importance.png # Generated visualization
└── 📄 README.md # You are here!
