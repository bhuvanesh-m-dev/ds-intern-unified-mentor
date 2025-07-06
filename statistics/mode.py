import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Wine Quality Dataset.csv")
mode_val = df['total sulfur dioxide'].mode()[0]

print("Mode of Total Sulfur Dioxide:", mode_val)

plt.bar(['Mode'], [mode_val], color='purple')
plt.title("Mode of Total Sulfur Dioxide")
plt.ylabel("Value")
plt.show()
