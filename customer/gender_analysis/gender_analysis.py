import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv('customer/data.csv')

min_age = df['Customer Age'].min()
max_age = df['Customer Age'].max()
start_bin = (min_age // 5) * 5
end_bin = ((max_age // 5) + 1) * 5
bins = range(start_bin, end_bin + 5, 5)
labels = [f'{i}-{i+4}' for i in bins[:-1]]
df['Age Group'] = pd.cut(df['Customer Age'], bins=bins, labels=labels, right=False, include_lowest=True)

age_gender_counts = df.groupby(['Age Group', 'Customer Gender']).size().unstack(fill_value=0)

fig, ax = plt.subplots(figsize=(12, 8))

colors = {
    'Male': 'blue',
    'Female': 'pink',
    'Other': 'black'
}

for gender in colors.keys():
    if gender in age_gender_counts.columns:
        ax.plot(age_gender_counts.index, age_gender_counts[gender], marker='o', linestyle='--', color=colors[gender], label=gender, alpha=0.7)

ax.set_xlabel('Age Group', fontsize=14)
ax.set_ylabel('Number of Customers', fontsize=14)
ax.set_title('Customer Gender Distribution by Age Group', fontsize=18)
plt.xticks(rotation=45, ha="right")
plt.grid(True, linestyle='--', alpha=0.6)
ax.legend(title="Gender")
plt.tight_layout()

# Ask user if they want to save the figure
ans = input("Do you want to save the generated graph? (y/n): ").lower()
if ans in ('y', 'yes'):
    save_path = 'img/gender_analysis.png'
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Graph saved to {save_path}")
    print('''Visit the 'img' folder to view the saved graph.''')
else:
    print('''Generated graph will not be saved!''')

plt.show()
