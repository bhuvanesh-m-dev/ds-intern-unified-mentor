import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("/home/bhuvanesh-m-ubuntu/Desktop/Netflix/files/cleaned_netflix.csv")

# Graph for total number of TV Shows (series) released per year
print('Graph for total number of TV Shows (series) released per year in Netflix OTT')
# Filter for years between 1900 and 2025
filtered_df = data[(data['release_year'] >= 1900) & (data['release_year'] <= 2025)]

# TV Shows per year
tv_per_year = filtered_df[filtered_df['type'] == 'TV Show'].groupby('release_year').size().reset_index(name='total_tv_shows')
tv_per_year = tv_per_year.sort_values('release_year')

plt.figure(figsize=(14, 7))
plt.plot(tv_per_year['release_year'], tv_per_year['total_tv_shows'], marker='x', linestyle='--', color='b', label='TV Shows')

plt.xlabel('Release Year', fontsize=14)
plt.ylabel('Total TV Shows Released', fontsize=14)
plt.title('Total Number of TV Shows Released per Year (1900–2025)', fontsize=16, fontweight='bold')
plt.legend(fontsize=12)

# Adjust x-axis ticks: every 2 years
plt.xticks(ticks=range(int(tv_per_year['release_year'].min()), int(tv_per_year['release_year'].max())+1, 2), rotation=45, ha='right')

plt.tight_layout()



# Save the generated graph 
ans=input("Do you want to save the generated graph?{y/n} :").lower()
if ans in ('y','yes'):
    plt.savefig("img/TV_Shows_per_year/series_per_year.png", dpi=300)
    print('''Visit img folder to view the saved graph''')
else:
    print('''Generated graph will not save!''')

plt.show()
