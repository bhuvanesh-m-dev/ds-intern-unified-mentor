import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print('''Disclaimer: The Netflix dataset includes Thunderbolt (1947), a documentary film originally released in 1947, predating Netflix's founding in 1997. This film was added to Netflix’s catalog at a later date as part of their curated content, which may include classic or historical titles. The "release date" in the dataset reflects the original theatrical release, not the date it was adopted by Netflix for streaming.''')

data = pd.read_csv("/home/bhuvanesh-m-ubuntu/Desktop/Netflix/files/cleaned_netflix.csv")

# Filter for South Korea only
data_korea = data[data['country'].str.contains('South Korea', na=False)]

print('Graph for total number of Movies released per year in Netflix OTT (South Korea only)')

filtered_df = data_korea[(data_korea['release_year'] >= 1900) & (data_korea['release_year'] <= 2025)]

# Movies per year
movies_per_year = filtered_df[filtered_df['type'] == 'Movie'].groupby('release_year').size().reset_index(name='total_movies')
movies_per_year = movies_per_year.sort_values('release_year')

plt.figure(figsize=(14, 7))
plt.plot(movies_per_year['release_year'], movies_per_year['total_movies'], marker='o', linestyle='-', color='r', label='Movies')

plt.xlabel('Release Year', fontsize=14)
plt.ylabel('Total Movies Released', fontsize=14)
plt.title('Total Number of Movies Released per Year in South Korea (1900–2025)', fontsize=16, fontweight='bold')
plt.legend(fontsize=12)

plt.xticks(ticks=range(int(movies_per_year['release_year'].min()), int(movies_per_year['release_year'].max())+1, 2), rotation=45, ha='right')

plt.tight_layout()

# Save the generated graph 
ans = input("Do you want to save the generated graph?{y/n} :").lower()
if ans in ('y','yes'):
    plt.savefig("img/movies_per_year/South_Korea/South_Korea.png", dpi=300)
    print('''Visit img folder to view the saved graph''')
else:
    print('''Generated graph will not save!''')
