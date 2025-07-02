# 📊 Boxplot with IQR – Documentation

## What is IQR?

IQR stands for **Interquartile Range**. It measures the spread of the middle 50% of a dataset and is calculated as:

```text
IQR = Q3 - Q1
```

Where:

* **Q1** is the 25th percentile
* **Q3** is the 75th percentile

IQR gives us a sense of how the values in the middle of a dataset are spread out, excluding extreme values.

---

## Who Introduced IQR?

The concept of **Interquartile Range (IQR)** was introduced by **Sir Francis Galton**, a key figure in the development of statistical science. He contributed significantly to the field of data visualization and summary statistics.

---

## Why Use IQR in Data Science?

* ✅ **Robust against outliers** and extreme values
* ✅ **Commonly used for detecting outliers** (values beyond 1.5×IQR from Q1 or Q3)
* ✅ **Summarizes central data variability**, especially in skewed distributions

IQR is a core component of boxplots, making it easy to interpret the data distribution visually.

---

## Where is IQR Used?

* ⚖️ **Exploratory Data Analysis (EDA)**
* 🔎 **Outlier detection** in machine learning pipelines
* ✅ **Quality control**, **biological research**, **finance**, and **engineering**

Because of its robustness, IQR is ideal for comparing datasets and evaluating the spread without the influence of outliers.

---

## Boxplot with IQR – Code & Visualization

This project (`boxplot_with_iqr.py`) demonstrates how to compute and visualize IQR using Python libraries:

### Dataset:

```python
[12, 7, 3, 15, 8, 10, 18, 6, 9, 14, 11, 13, 5, 17, 16]
```

### Full Source Code with Line-by-Line Explanation

```python
# Importing required libraries
import matplotlib.pyplot as plt  # For plotting the boxplot
import numpy as np  # For numerical operations like mean, percentile, etc.

# Define dataset
data = [12, 7, 3, 15, 8, 10, 18, 6, 9, 14, 11, 13, 5, 17, 16]  # Sample data points

# Compute summary statistics
minimum = np.min(data)           # Smallest value in the dataset
q1 = np.percentile(data, 25)     # First quartile (25th percentile)
median = np.median(data)         # Median (50th percentile)
q3 = np.percentile(data, 75)     # Third quartile (75th percentile)
maximum = np.max(data)           # Largest value in the dataset
iqr = q3 - q1                    # Interquartile range (Q3 - Q1)

# Create a boxplot
plt.figure(figsize=(8, 6))       # Set the size of the plot
box = plt.boxplot(
    data,
    vert=True,                   # Vertical boxplot
    patch_artist=True,           # Fill the box with color
    widths=0.5,                  # Width of the box
    boxprops=dict(facecolor='lightblue')  # Box color fill
)

# Plot titles and labels
plt.title("Boxplot with Statistical Annotations")
plt.ylabel("Values")
plt.xlabel("Data = [12, 7, 3, 15, 8, 10, 18, 6, 9, 14, 11, 13, 5, 17, 16]")
plt.grid(True, axis='y')         # Add horizontal grid lines

# Set X positions for annotation texts
x_annot_left = 1.15
x_annot_right = 1.35

# Annotate statistics on the plot
plt.text(x_annot_left, minimum, f"Min: {minimum}", va='center', color='blue')
plt.text(x_annot_right, q1, f"Q1: {q1}", va='center', color='green')
plt.text(x_annot_right, median, f"Median: {median}", va='center', color='red')
plt.text(x_annot_right, q3, f"Q3: {q3}", va='center', color='green')
plt.text(x_annot_left, maximum, f"Max: {maximum}", va='center', color='blue')
plt.text(x_annot_right, median + 2, f"IQR: {iqr}", va='center', color='purple')  # Display IQR value above median

# Final layout adjustment and show plot
plt.tight_layout()
plt.show()
```

---

## 🔍 Code Breakdown and Algorithm

### Algorithm Steps:

1. **Import Libraries**:

   * `matplotlib.pyplot` for plotting
   * `numpy` for numerical operations

2. **Define the dataset**: A list of 15 integers.

3. **Calculate statistics**:

   * `min()`, `percentile(25)`, `median()`, `percentile(75)`, `max()` and compute `IQR`.

4. **Plot boxplot**:

   * Set figure size
   * Customize box appearance (light blue)

5. **Annotate plot**:

   * Display min, Q1, median, Q3, max, and IQR with `plt.text()`

6. **Show plot** with `plt.show()`

---

## 📈 Output


![boxplot_with_iqr.png](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/boxplot_with_iqr/img/boxplot_with_iqr.png)

This boxplot shows:

* Central tendency (median)
* Spread (IQR)
* Outliers (beyond 1.5×IQR)

---

## 🚀 Run It

```bash
python boxplot_with_iqr.py
```

Use this script to understand IQR-based distribution in your own datasets.
