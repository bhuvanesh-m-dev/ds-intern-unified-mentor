import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
platform_counts = df['Most_Used_Platform'].value_counts()
apps = platform_counts.index.tolist()
counts = platform_counts.values
percentages = (counts / counts.sum()) * 100
colors = [
    '#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9',
    '#92A8D1', '#955251', '#B565A7', '#009B77',
    '#FFD662', '#034F84', '#F7786B', '#DE7A22'
]

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts = ax.pie(
    percentages,
    labels=None,
    autopct=None,
    startangle=140,
    colors=colors[:len(apps)],
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

plt.title('Social Media App Usage', fontsize=18)
plt.tight_layout()

legend_labels = []
for app, pct in zip(apps, percentages):
    legend_labels.append(f"{app}: {pct:.2f}%")

ax.legend(wedges, legend_labels, title="Apps", loc="upper right", bbox_to_anchor=(1.25, 1), fontsize=12, title_fontsize=14, frameon=False)

plt.show()
