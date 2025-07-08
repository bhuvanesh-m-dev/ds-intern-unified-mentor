import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import os


file_path = 'customer/data.csv'
data = pd.read_csv(file_path)

ratings_counts = data['Customer Satisfaction Rating'].value_counts().sort_index()


plt.figure(figsize=(8, 6))
plt.bar(ratings_counts.index, ratings_counts.values, color='steelblue')

plt.xlabel('Satisfaction Rating')
plt.ylabel('Number of Customers')
plt.title('Distribution of Customer Satisfaction Ratings')

plt.xticks(ratings_counts.index)
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=5, integer=True))
plt.ylim(bottom=0) 

plt.tight_layout()
# Ask user if they want to save the figure
ans = input("Do you want to save the generated graph? (y/n): ").lower()
if ans in ('y', 'yes'):
    save_path = 'img/model_customer_satisfaction.png'
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    print(f"Graph saved to {save_path}")
    print('''Visit the 'img' folder to view the saved graph.''')
else:
    print('''Generated graph will not be saved!''')
plt.show()
