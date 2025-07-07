# 🧠 Customer Support Ticket Analysis & Satisfaction Prediction

This repository contains a comprehensive **Data Science project** developed for internship purposes. The goal is to **analyze customer support ticket data** and build insights & predictive models related to **customer satisfaction** using machine learning and exploratory analysis.

---

## 📁 Folder Structure

Each folder focuses on a specific area of analysis:

| Folder                         | Description |
|-------------------------------|-------------|
| `age_group_analysis/`         | Analyze support tickets across age brackets. |
| `channel_review/`             | Ticket channel performance and customer preference. |
| `customer_segmentation/`      | KMeans-based segmentation using customer attributes. |
| `gender_analysis/`            | Satisfaction and product preference by gender. |
| `model_customer_satisfaction/`| Machine Learning model to predict satisfaction scores. |
| `priority_resolution_analysis/`| Resolution time and priority-based analysis. |
| `product_analysis/`           | Top purchased products, product-wise satisfaction. |
| `ticket_trend_analysis/`      | Temporal and topical analysis of ticket trends. |

---

## 🧹 Data Cleaning

Raw dataset: `customer_support_tickets.csv`  
Cleaned dataset: `data.csv`

See [`data_clean.md`](./data_clean.md) and [`data_cleaning.py`](./data_cleaning.py) for full steps. Only complete rows (where `Resolution`, `First Response`, and `Time to Resolution` were available) are retained in `data.csv` for analysis and modeling.

---

## 💡 Objective

### 🎯 Main Goal:
Predict **Customer Satisfaction** and extract actionable insights using a variety of **EDA + ML** techniques.

### 🔍 Sub Goals:
- Understand user behavior across gender and age groups.
- Identify high-performing support channels.
- Determine the most problematic product categories.
- Predict satisfaction using support features via ML models.

---

## 📦 Dataset Description

| Feature | Description |
|---------|-------------|
| `Ticket ID` | Unique ID for each support ticket. |
| `Customer Name`, `Email`, `Age`, `Gender` | Demographics. |
| `Product Purchased` | Product bought by the customer. |
| `Ticket Type`, `Subject`, `Description` | Issue details. |
| `Ticket Status`, `Priority`, `Channel` | Support metadata. |
| `First Response Time`, `Time to Resolution` | Response metrics. |
| `Customer Satisfaction Rating` | Target variable (1–5). |

---

## 📊 Tools & Libraries

- `pandas`, `numpy` for data processing
- `matplotlib`, `seaborn` for visualization
- `sklearn` for modeling and ML
- `KMeans`, `RandomForestClassifier`, `LabelEncoder`, `StandardScaler`

---

## 🧠 Model Approach

Located in: [`model_customer_satisfaction/`](./model_customer_satisfaction/)

1. Preprocessing (drop NA, encode, scale)
2. Train/Test split
3. Random Forest Model training
4. Evaluation via Accuracy, Confusion Matrix
5. Feature Importance Visualization

---

## 🛠️ Next Steps

- Add dashboards/visuals (if time permits)
- Optionally export results as images/interactive plots
- Consider adding Flask/Streamlit interface

---

## 📬 Contact

For queries, suggestions, or feedback:
[@bhuvanesh-m-dev](https://github.com/bhuvanesh-m-dev)

---

> 🚀 Project status: **Actively in progress**
