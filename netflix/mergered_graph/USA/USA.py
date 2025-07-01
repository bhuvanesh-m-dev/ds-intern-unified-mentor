import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("/home/bhuvanesh-m-ubuntu/Desktop/Netflix/files/cleaned_netflix.csv")

# Filter for USA only
data_usa = data[data['country'].str.contains('United States', na=False)]

# Merge both Movies and TV Shows per year in a single graph for USA
print('Graph for total number of Movies and TV Shows released per year in Netflix OTT (USA only)')
# Filter for years between 1900 and 2025
filtered_df = data_usa[(data_usa['release_year'] >= 1900) & (data_usa['release_year'] <= 2025)]

# Movies per year
movies_per_year = filtered_df[filtered_df['type'] == 'Movie'].groupby('release_year').size().reset_index(name='total_movies')
# TV Shows per year
tv_per_year = filtered_df[filtered_df['type'] == 'TV Show'].groupby('release_year').size().reset_index(name='total_tv_shows')

# Merge on release_year to align both
merged = pd.merge(movies_per_year, tv_per_year, on='release_year', how='outer').fillna(0)
merged = merged.sort_values('release_year')

plt.figure(figsize=(14, 7))
plt.plot(merged['release_year'], merged['total_movies'], marker='o', linestyle='-', color='r', label='Movies')
plt.plot(merged['release_year'], merged['total_tv_shows'], marker='x', linestyle='--', color='b', label='TV Shows')

plt.xlabel('Release Year', fontsize=14)
plt.ylabel('Total Released', fontsize=14)
plt.title('Total Number of Movies and TV Shows Released per Year in USA (1900–2025)', fontsize=16, fontweight='bold')
plt.legend(fontsize=12)

# Adjust x-axis ticks: every 2 years
plt.xticks(ticks=range(int(merged['release_year'].min()), int(merged['release_year'].max())+1, 2), rotation=45, ha='right')

plt.tight_layout()

# Save the generated graph 
ans = input("Do you want to save the generated graph?{y/n} :").lower()
if ans in ('y','yes'):
    plt.savefig("img/mergered_graph/USA/USA.png", dpi=300)
    print('''Visit img folder to view the saved graph''')
else:
    print('''Generated graph will not save!''')

plt.show()
