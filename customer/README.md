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

## 📬 Contact

For contributions, questions or feedback:  
📧 [bhuvanesh-m-dev](https://github.com/bhuvanesh-m-dev)

---

## 🙋‍♂️ BHUVANESH M 

🌐 [bhuvaneshm.in](https://bhuvaneshm.in)   
🔗 [linkedin.com/in/bhuvaneshm-developer](https://www.linkedin.com/in/bhuvaneshm-developer)   
✍️ [dev.to/bhuvaneshm\_dev](https://dev.to/bhuvaneshm_dev)   
📊 [kaggle.com/bhuvaneshm06](https://www.kaggle.com/bhuvaneshm06)    

<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="Header Banner">
</p> 
 <h3 align="center">
    🌌 You are my &nbsp;
    <a href="https://github.com/bhuvanesh-m-dev">
    <img src="https://count.getloli.com/@bhuvanesh-m-dev?name=bhuvanesh-m-dev&theme=ai-1&padding=13&offset=0&align=top&scale=1&pixelated=1&darkmode=auto" alt="bhuvanesh-m-dev" />
    </a>
    &nbsp; visitor. Welcome to my orbit.
</h3>
<p align="center">
  <img src="https://user-images.githubusercontent.com/73097560/115834477-dbab4500-a447-11eb-908a-139a6edaec5c.gif" width="100%" alt="Header Banner">
</p>
