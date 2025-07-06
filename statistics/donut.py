import matplotlib.pyplot as plt

# Mean values
values = [138.36, 6.85, 10.51]
labels = ['Total Sulfur Dioxide', 'Fixed Acidity', 'Alcohol']
colors = ['#ff9999','#66b3ff','#99ff99']

fig, ax = plt.subplots()
wedges, texts = ax.pie(values, labels=labels, colors=colors, startangle=90, wedgeprops=dict(width=0.5))
ax.axis('equal')  
plt.title("Donut Chart - Mean Comparison")
plt.show()
