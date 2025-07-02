import matplotlib.pyplot as plt
import numpy as np

data = [12, 7, 3, 15, 8, 10, 18, 6, 9, 14, 11, 13, 5, 17, 16]


minimum = np.min(data)
q1 = np.percentile(data, 25)
median = np.median(data)
q3 = np.percentile(data, 75)
maximum = np.max(data)
iqr = q3 - q1

plt.figure(figsize=(8, 6))
box = plt.boxplot(data, vert=True, patch_artist=True, widths=0.5, boxprops=dict(facecolor='lightblue'))

plt.title("Boxplot with Statistical Annotations")
plt.ylabel("Values")
plt.xlabel("Data = [12, 7, 3, 15, 8, 10, 18, 6, 9, 14, 11, 13, 5, 17, 16]")
plt.grid(True, axis='y')


x_annot_left = 1.15
x_annot_right = 1.35

plt.text(x_annot_left, minimum, f"Min: {minimum}", va='center', color='blue')
plt.text(x_annot_right, q1, f"Q1: {q1}", va='center', color='green')
plt.text(x_annot_right, median, f"Median: {median}", va='center', color='red')
plt.text(x_annot_right, q3, f"Q3: {q3}", va='center', color='green')
plt.text(x_annot_left, maximum, f"Max: {maximum}", va='center', color='blue')
plt.text(x_annot_right, median + 2, f"IQR: {iqr}", va='center', color='purple')  

plt.tight_layout()
plt.show()
