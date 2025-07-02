

import matplotlib.pyplot as plt

plt.figure(figsize=(8, 6))

import matplotlib.patches as patches
ax = plt.gca()
box_rect = patches.Rectangle((2, 1.85), 4, 0.3, linewidth=1.5, edgecolor='blue', facecolor='lightblue', label='IQR (Q1 to Q3)')
ax.add_patch(box_rect)
plt.vlines(4, 1.7, 2.3, color='red', linewidth=2, label='Median (50th %)')
plt.hlines(2, 1, 2, color='blue', linewidth=2)
plt.hlines(2, 6, 7, color='blue', linewidth=2)
plt.vlines(1, 1.85, 2.15, color='blue', linewidth=2)
plt.vlines(7, 1.85, 2.15, color='blue', linewidth=2)

plt.text(1, 2.25, 'Min\n(0th %)', ha='center', color='blue')
plt.text(2, 2.35, 'Q1\n(25th %)', ha='center', color='green')
plt.text(4, 2.4, 'Median\n(50th %)', ha='center', color='red')
plt.text(6, 2.35, 'Q3\n(75th %)', ha='center', color='green')
plt.text(7, 2.25, 'Max\n(100th %)', ha='center', color='blue')
plt.text(4, 1.6, 'IQR = Q3 - Q1', ha='center', color='purple')

plt.ylim(1.5, 2.6)
plt.xlim(0, 8)
plt.axis('off')
plt.title('Boxplot Structure: IQR, Quartiles, Min, Max, Median')
plt.tight_layout()
plt.savefig("iqr/iqr.png", dpi=300)
print("Saved schematic boxplot as iqr.png in the current directory.")
