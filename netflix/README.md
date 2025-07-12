# 📊 Netflix Data Analysis – Unified Mentor Internship

This repository contains part of the **Data Science Internship Project** at **Unified Mentor**, where I analyze Netflix OTT content data using Python libraries such as Pandas, NumPy, and Matplotlib.

---

## 📂 Files Included

| File Name             | Purpose                                                          |
| --------------------- | ---------------------------------------------------------------- |
| `netflix.csv`         | Raw dataset containing Netflix content details                   |
| `data_cleaning.py`    | Cleans the dataset by handling missing and inconsistent values   |
| `movies_per_year.py`  | Analyzes and visualizes number of movies released per year       |
| `series_per_year.py`  | Analyzes and visualizes number of series released per year       |
| `merged_graph.py`     | Displays both movies and series release trends on a single graph |
| `cleaned_netflix.csv` | Output file after cleaning, created by `data_cleaning.py`        |

---

## 🧼 Step 1: Data Cleaning

The original `netflix.csv` contains some columns like `director`, `cast`, etc., where values are marked as **"Not Given"**. These should be treated as missing data (NaN in Python).

Run the following script to clean the data:

```bash
python data_cleaning.py
```

🔹 This will create a new file called `cleaned_netflix.csv`.

---

## 📊 Step 2: Data Analysis and Graphs

Use the cleaned dataset for further analysis. The following scripts generate visual insights:

### 2️⃣ `movies_per_year.py`

Generates a **line graph** showing the **number of movies released each year**.

Run:

```bash
python movies_per_year.py
```

### 3️⃣ `series_per_year.py`

Generates a **line graph** showing the **number of TV shows released each year**.

Run:

```bash
python series_per_year.py
```

### 4️⃣ `merged_graph.py`

Combines both movie and series release trends on a **single line graph** for comparison.

Run:

```bash
python merged_graph.py
```

📝 **Note**: These graphs are line plots, not bar charts. Each graph represents trends over time using data points connected with lines.

💾 **Tip**: You can save the generated graphs to your local storage for future reference and documentation.

> 📌 Note: These scripts use `cleaned_netflix.csv` as input and rely on `pandas`, `numpy`, and `matplotlib`.

---

## 🛠 Requirements

Install the required Python libraries using:

```bash
pip install pandas numpy matplotlib
```

---

## 📌 Project Context

This mini-project is part of the **Data Science Internship** under **Unified Mentor**, focused on working with real-world datasets and applying Python-based data cleaning and visualization techniques.

---

## 🙋‍♂️ BHUVANESH M 
🌐 [bhuvaneshm.in](https://bhuvaneshm.in)  
🔗 [linkedin.com/in/bhuvaneshm-developer](https://www.linkedin.com/in/bhuvaneshm-developer)  
✍️ [dev.to/bhuvaneshm\_dev](https://dev.to/bhuvaneshm_dev)  
📊 [kaggle.com/bhuvaneshm06](https://www.kaggle.com/bhuvaneshm06)  

---
