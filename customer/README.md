# 🧠 Customer Support Ticket Analysis & Satisfaction Prediction

This repository contains a comprehensive **Data Science internship project** focused on analyzing customer support ticket data and building predictive models for **customer satisfaction**.

---

## 📁 Folder Structure

| Folder                          | Description                                               |
| ------------------------------- | --------------------------------------------------------- |
| `age_group_analysis/`           | Analyze support tickets across age brackets.              |
| `channel_review/`               | Ticket channel performance and customer preference.       |
| `gender_analysis/`              | Product preference by gender.            |
| `model_customer_satisfaction/`  | Visualizes the distribution of customer satisfaction ratings using a bar chart.    |


---

## 🧹 Data Cleaning

* **Raw Data**: `customer_support_tickets.csv`
* **Cleaned Data**: `data.csv`

Refer to [`data_clean.md`](./data_clean.md) and [`data_cleaning.py`](./data_cleaning.py) for preprocessing details.

> ✔️ Cleaned data retains rows only where `Resolution`, `First Response`, and `Time to Resolution` are all available.

---

## 💡 Objective

### 🔍 Sub-goals:

* Understand trends across age and gender.
* Discover most-used and best-performing support channels.
* Identify pain points in products.


---

## 📦 Dataset Description

| Feature                                     | Description              |
| ------------------------------------------- | ------------------------ |
| `Ticket ID`                                 | Unique ticket identifier |
| `Customer Name`, `Email`, `Age`, `Gender`   | Demographics             |
| `Product Purchased`                         | Item bought              |
| `Ticket Type`, `Subject`, `Description`     | Issue metadata           |
| `Ticket Status`, `Priority`, `Channel`      | Operational data         |
| `First Response Time`, `Time to Resolution` | Response metrics         |
| `Customer Satisfaction Rating`              | Target variable (1–5)    |

---

## 📊 Tools & Libraries Used

* `pandas`, `numpy` — data handling
* `matplotlib`, `seaborn` — visualization

---

## 📈 Exploratory Visualizations

### 🧯 Customer Age Group Distribution

* Pie chart showing percentage breakdown across age brackets.
![Customer Age Group Pie Chart](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/customer/img/age_group_analysis.png)
[For more details.](https://github.com/bhuvanesh-m-dev/ds-intern-unified-mentor/tree/main/customer/age_group_analysis)

---

### 🎟️ Support Ticket Channel Analysis

* Pie chart showing how customers reached support (Email, Chat, etc.).
![Support Ticket Channel Pie Chart](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/customer/img/ticket_channel_analysis.png)
[For more details.](https://github.com/bhuvanesh-m-dev/ds-intern-unified-mentor/tree/main/customer/channel_review)
---

### 🌟 Satisfaction Rating Distribution

* Bar chart showing how many customers rated satisfaction levels from 1 to 5.
![Customer Satisfaction Bar Chart](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/customer/img/model_customer_satisfaction.png)
[For more details.](https://github.com/bhuvanesh-m-dev/ds-intern-unified-mentor/tree/main/customer/model_customer_satisfaction)
---

### 👥 Gender Distribution by Age Group

* Line chart showing how each gender is distributed across age brackets.
![Customer Gender Analysis Line Chart](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/customer/img/gender_analysis.png)
[For more details.](https://github.com/bhuvanesh-m-dev/ds-intern-unified-mentor/tree/main/customer/gender_analysis)
---

### 📌 Planned & Upcoming Visuals

> These will be included soon (or are in progress):

* 📆 **Ticket Trends Over Time** (line plot or heatmap)
* 🛍️ **Top Products and Ratings** (bar chart, grouped analysis)
* 🚦 **Resolution Time vs Priority** (box plot / violin plot)
* 🧹 **Customer Segments Overview** (scatter or cluster map)
* 📈 **Feature Correlation Heatmap**
* ⚙️ **Gender vs Rating** (stacked bar chart)

---

## 🤖 ML Model: Satisfaction Predictor

Located at: `model_customer_satisfaction/`

**Steps:**

1. Clean & preprocess the data
2. Encode categorical features
3. Scale features where necessary
4. Split into train/test
5. Train Random Forest
6. Evaluate model (accuracy, confusion matrix)
7. Plot feature importances

---

## 🛠️ Future Enhancements

* Build Streamlit/Flask dashboard for real-time interaction
* Add automated EDA report (e.g., with `pandas-profiling`)
* Include interactive charts (e.g., via `plotly`)
* Push to Hugging Face or render via Spaces

---

## 📬 Contact

For contributions, questions or feedback:  
📧 [bhuvanesh-m-dev](https://github.com/bhuvanesh-m-dev)

---
