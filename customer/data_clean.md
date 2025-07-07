# 📊 Data Cleaning Process: `customer_support_tickets.csv`

## 🧹 Overview

The original dataset, `customer_support_tickets.csv`, contains **17 columns** and **8,469 rows**. However, upon inspection, it was found that some key columns had missing data:

- `Resolution`
- `First Response`
- `Time to Resolution`

These fields are crucial for analysis, and missing values in any of them can lead to inaccurate results or incomplete insights.

---

## 🛠️ Cleaning Strategy

To ensure data quality and consistency, the following cleaning steps were performed:

1. **Loaded** the dataset using Python and pandas.
2. **Checked** for missing values in the columns:
   - `Resolution`
   - `First Response`
   - `Time to Resolution`
3. **Dropped rows** where any of these fields were empty.
4. **Saved** the cleaned data to a new CSV file for future analysis.

---

## 🐍 Script Used

The cleaning process was handled using a Python script:

```bash
data_cleaning.py
