import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Wine Quality Dataset.csv")
mean_val = df['total sulfur dioxide'].mean()

print("Mean of Total Sulfur Dioxide:", mean_val)

plt.bar(['Mean'], [mean_val], color='orange')
plt.title("Mean of Total Sulfur Dioxide")
plt.ylabel("Value")
plt.show()
