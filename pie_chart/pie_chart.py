import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
platform_counts = df['Most_Used_Platform'].value_counts()
apps = platform_counts.index.tolist()
counts = platform_counts.values
percentages = (counts / counts.sum()) * 100
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7', '#009B77']

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    percentages,
    labels=apps,
    autopct=lambda pct: f"{pct:.2f}%",
    startangle=140,
    colors=colors[:len(apps)],
    wedgeprops={'edgecolor': 'white', 'linewidth': 2},
    textprops={'fontsize': 14, 'color': 'black'}
)

plt.title('Social Media App Usage (%)', fontsize=18, fontweight='bold')
plt.tight_layout()
plt.show()
