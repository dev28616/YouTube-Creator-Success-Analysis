# YouTube Success Analysis & Creator Playbook

An end-to-end data science project that reverse-engineers the drivers of YouTube success for Indian finance creators. This project transforms raw data into a predictive engine and culminates in an interactive strategy playbook designed to empower creators with actionable, data-driven insights.

---

## 🎯 Business Problem & Solution

### Problem
The YouTube creator space is saturated. New and existing creators in the high-value **finance niche** struggle to identify a content strategy that reliably drives growth. They often rely on intuition rather than data, leading to inconsistent results.

### Solution
We built a **predictive model** to quantify the impact of various content attributes on viewership and distilled the findings into a **user-friendly interactive infographic**. Now, creators can make data-backed decisions easily.

---

## 🚀 Live Infographic & Final Report

👉 View the live interactive infographic here:  
[https://youtube-analyze.netlify.app/](https://youtube-analyze.netlify.app/)

---

## 📊 Key Insights & Recommendations

- ✅ **Optimize for Engagement, Not Just Clicks**  
  Engagement rate is the strongest predictor of video success. Prioritize content that sparks conversation and community interaction.

- ✅ **Publish on Wednesday or Saturday**  
  Publishing on these days boosts views by ~15% on average due to peak audience availability.

---

## 🛠️ Technical Architecture

- **Data Collection**  
  Python script using YouTube Data API v3 to collect 1,000+ videos from 20 top finance channels.

- **Data Storage & Engineering**  
  PostgreSQL stores the dataset. SQL & Python clean and create 8 predictive features (e.g., `engagement_rate`, `title_contains_money_keyword`).

- **Predictive Modeling**  
  RandomForest Regressor built in Scikit-learn predicts view counts and reveals feature importance.

- **Data Visualization & Reporting**  
  Responsive SPA built with HTML5, Tailwind CSS, and Chart.js.

---

## 💡 Future Enhancements

- ☁️ Cloud Migration to GCP (BigQuery + Vertex AI)
- ✨ Advanced Feature Engineering (NLP on comments, Computer Vision on thumbnails)
- 📊 Real-time Creator Dashboard (Input channel ID → Personalized Report)

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repo:
```bash
git clone https://github.com/dev28616/YouTube-Success-Analysis.git
cd YouTube-Success-Analysis
