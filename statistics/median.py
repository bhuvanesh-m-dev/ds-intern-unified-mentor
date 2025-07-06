import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Wine Quality Dataset.csv")
median_val = df['total sulfur dioxide'].median()

print("Median of Total Sulfur Dioxide:", median_val)

plt.bar(['Median'], [median_val], color='green')
plt.title("Median of Total Sulfur Dioxide")
plt.ylabel("Value")
plt.show()
