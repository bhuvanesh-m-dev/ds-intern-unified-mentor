import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('data.csv')
platform_counts = df['Most_Used_Platform'].value_counts()
apps = platform_counts.index.tolist()
counts = platform_counts.values
percentages = (counts / counts.sum()) * 100
colors = ['#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9', '#92A8D1', '#955251', '#B565A7', '#009B77']

fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts = ax.pie(
    percentages,
    labels=None,
    autopct=None,
    startangle=140,
    colors=colors[:len(apps)],
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

plt.title('Social Media App Usage (%)', fontsize=18, fontweight='bold')
plt.tight_layout()

# Custom legend labels with app name and percentage
legend_labels = [f"{app}: {pct:.2f}%" for app, pct in zip(apps, percentages)]

# Add legend in the upper right corner with color scale
ax.legend(wedges, legend_labels, title="Apps", loc="upper right", bbox_to_anchor=(1.25, 1), fontsize=12, title_fontsize=14, frameon=False)

plt.show()
