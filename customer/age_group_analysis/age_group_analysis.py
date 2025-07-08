import pandas as pd
import matplotlib.pyplot as plt
import os
df = pd.read_csv('customer/data.csv')

bins = range(0, 101, 10)
labels = [f'{i+1}-{i+10}' for i in range(0, 100, 10)]
df['Age Group'] = pd.cut(df['Customer Age'], bins=bins, labels=labels, right=True, include_lowest=True)

age_group_counts = df['Age Group'].value_counts().sort_index()

age_groups = age_group_counts.index.tolist()
counts = age_group_counts.values
percentages = (counts / counts.sum()) * 100
colors = [
    '#FF6F61', '#6B5B95', '#88B04B', '#F7CAC9',
    '#92A8D1', '#955251', '#B565A7', '#009B77',
    '#FFD662', '#034F84', '#F7786B', '#DE7A22'
]

fig, ax = plt.subplots(figsize=(10, 10))
wedges, texts = ax.pie(
    percentages,
    labels=None,
    autopct=None,
    startangle=140,
    colors=colors[:len(age_groups)],
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

plt.title('Customer Age Group Distribution', fontsize=18)
plt.tight_layout()

legend_labels = []
for group, pct in zip(age_groups, percentages):
    legend_labels.append(f"{group}: {pct:.2f}%")

ax.legend(wedges, legend_labels, title="Age Groups", loc="upper right", bbox_to_anchor=(1.3, 1), fontsize=12, title_fontsize=14, frameon=False)

# Ask user if they want to save the figure
ans = input("Do you want to save the generated graph? (y/n): ").lower()
if ans in ('y', 'yes'):
    save_path = 'customer/img/age_group_analysis.png'
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Graph saved to {save_path}")
    print('''Visit the 'img' folder to view the saved graph.''')
else:
    print('''Generated graph will not be saved!''')

plt.show()
