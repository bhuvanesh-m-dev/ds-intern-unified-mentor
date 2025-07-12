# 📊 Netflix Content Trends: Movies + TV Shows (Per Year)

This project visualizes the **combined yearly trend of movies and TV shows** released on Netflix. It analyzes how total content output has grown globally and in specific countries—**India**, **South Korea**, and the **USA**.

---

## 🌍 Global Trend

![Merged Graph - Worldwide](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/mergered_graph/merged_graph.png)

This graph shows the total number of movies and TV shows released globally on Netflix over time.   
[For more details.](https://github.com/bhuvanesh-m-dev/ds-intern-unified-mentor/tree/main/netflix/mergered_graph)

---

## 🇮🇳 India

![Merged Graph - India](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/mergered_graph/India/India.png)

Netflix's Indian content has grown steadily. This chart combines both movie and TV show releases.   
[For more details.](https://github.com/bhuvanesh-m-dev/ds-intern-unified-mentor/tree/main/netflix/mergered_graph/India)

---

## 🇰🇷 South Korea

![Merged Graph - South Korea](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/mergered_graph/South_Korea/South_Korea.png)

Korean entertainment has seen a surge on Netflix. This visual tracks both movies and series released annually.   
[For more details.](https://github.com/bhuvanesh-m-dev/ds-intern-unified-mentor/tree/main/netflix/mergered_graph/South_Korea)

---

## 🇺🇸 USA

![Merged Graph - USA](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/mergered_graph/USA/USA.png)

The U.S. remains a major contributor to Netflix’s content. This plot reflects both TV shows and films over the years.   
[For more details.](https://github.com/bhuvanesh-m-dev/ds-intern-unified-mentor/tree/main/netflix/mergered_graph/USA)

---

## 🐍 Python Script (Global)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data = pd.read_csv("netflix/files/cleaned_netflix.csv")

print('Graph for total number of Movies and TV Shows released per year in Netflix OTT')

filtered_df = data[(data['release_year'] >= 1900) & (data['release_year'] <= 2025)]

movies_per_year = filtered_df[filtered_df['type'] == 'Movie'].groupby('release_year').size().reset_index(name='total_movies')
tv_per_year = filtered_df[filtered_df['type'] == 'TV Show'].groupby('release_year').size().reset_index(name='total_tv_shows')
merged = pd.merge(movies_per_year, tv_per_year, on='release_year', how='outer').fillna(0)
merged = merged.sort_values('release_year')

plt.figure(figsize=(14, 7))
plt.plot(merged['release_year'], merged['total_movies'], marker='o', linestyle='-', color='r', label='Movies')
plt.plot(merged['release_year'], merged['total_tv_shows'], marker='x', linestyle='--', color='b', label='TV Shows')

plt.xlabel('Release Year', fontsize=14)
plt.ylabel('Total Released', fontsize=14)
plt.title('Total Number of Movies and TV Shows Released per Year (1900–2025)', fontsize=16, fontweight='bold')
plt.legend(fontsize=12)

plt.xticks(ticks=range(int(merged['release_year'].min()), int(merged['release_year'].max())+1, 2), rotation=45, ha='right')

plt.tight_layout()


# Save the generated graph 
ans=input("Do you want to save the generated graph?{y/n} :").lower()
if ans in ('y','yes'):
    plt.savefig("img/mergered_graph/merged_graph.png", dpi=300)
    print('''Visit img folder to view the saved graph''')
else:
    print('''Generated graph will not save!''')


plt.show()
```

---

## 🙋‍♂️ BHUVANESH M 

🌐 [bhuvaneshm.in](https://bhuvaneshm.in)   
🔗 [linkedin.com/in/bhuvaneshm-developer](https://www.linkedin.com/in/bhuvaneshm-developer)   
✍️ [dev.to/bhuvaneshm\_dev](https://dev.to/bhuvaneshm_dev)   
📊 [kaggle.com/bhuvaneshm06](https://www.kaggle.com/bhuvaneshm06)   

---

