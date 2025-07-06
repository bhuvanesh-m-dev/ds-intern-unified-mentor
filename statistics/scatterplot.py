import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Wine Quality Dataset.csv")

plt.figure(figsize=(8,6))
scatter = plt.scatter(df['fixed acidity'], df['total sulfur dioxide'], c=df['alcohol'], cmap='viridis', alpha=0.7)
plt.colorbar(scatter, label='Alcohol')
plt.xlabel('Fixed Acidity')
plt.ylabel('Total Sulfur Dioxide')
plt.title('Scatter Plot: Fixed Acidity vs Total Sulfur Dioxide (colored by Alcohol)')
plt.grid(True)
plt.show()
