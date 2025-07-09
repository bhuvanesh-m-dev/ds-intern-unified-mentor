import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("netflix/files/cleaned_netflix.csv")

data_usa = data[data['country'].str.contains('United States', na=False)]

print('Graph for total number of Movies and TV Shows released per year in Netflix OTT (USA only)')

filtered_df = data_usa[(data_usa['release_year'] >= 1900) & (data_usa['release_year'] <= 2025)]

movies_per_year = filtered_df[filtered_df['type'] == 'Movie'].groupby('release_year').size().reset_index(name='total_movies')
tv_per_year = filtered_df[filtered_df['type'] == 'TV Show'].groupby('release_year').size().reset_index(name='total_tv_shows')

merged = pd.merge(movies_per_year, tv_per_year, on='release_year', how='outer').fillna(0)
merged = merged.sort_values('release_year')

plt.figure(figsize=(14, 7))
plt.plot(merged['release_year'], merged['total_movies'], marker='o', linestyle='-', color='r', label='Movies')
plt.plot(merged['release_year'], merged['total_tv_shows'], marker='x', linestyle='--', color='b', label='TV Shows')

plt.xlabel('Release Year', fontsize=14)
plt.ylabel('Total Released', fontsize=14)
plt.title('Total Number of Movies and TV Shows Released per Year in USA (1900–2025)', fontsize=16, fontweight='bold')
plt.legend(fontsize=12)

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
