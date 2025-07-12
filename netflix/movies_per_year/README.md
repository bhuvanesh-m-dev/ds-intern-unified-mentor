# 🎬 Netflix Movies Per Year

This project analyzes the **yearly trend of movie releases** on the Netflix platform across different regions—**Worldwide, India, South Korea, and the USA**. It visualizes how the number of movies has evolved year by year, helping to identify growth patterns in regional content offerings.

---

## 🌍 Global Trend

![Movies Worldwide](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/movies_per_year/movies_per_year.png)

This graph illustrates the total number of movies released globally on Netflix, categorized by year.    
[For more details.](https://github.com/bhuvanesh-m-dev/ds-intern-unified-mentor/tree/main/netflix/movies_per_year)

---

## 🇮🇳 India

![Movies in India](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/movies_per_year/India/India.png)

This graph highlights the rise of Indian movies on Netflix, year by year.    
[For more details.](https://github.com/bhuvanesh-m-dev/ds-intern-unified-mentor/tree/main/netflix/movies_per_year/India)

---

## 🇰🇷 South Korea

![Movies in South Korea](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/movies_per_year/South_Korea/South_Korea.png)

Korean cinema has expanded greatly on Netflix. This plot shows how its presence has evolved over time.   
[For more details.](https://github.com/bhuvanesh-m-dev/ds-intern-unified-mentor/tree/main/netflix/movies_per_year/South_Korea)

---

## 🇺🇸 USA

![Movies in USA](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/movies_per_year/USA/USA.png)

A major content provider on Netflix, this graph shows yearly releases of American movies.   
[For more details.](https://github.com/bhuvanesh-m-dev/ds-intern-unified-mentor/tree/main/netflix/movies_per_year/USA)

---

## 🐍 Python Script (World Wide)

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


print('''Disclaimer: The Netflix dataset includes Thunderbolt (1947), a documentary film originally released in 1947, predating Netflix's founding in 1997. This film was added to Netflix’s catalog at a later date as part of their curated content, which may include classic or historical titles. The "release date" in the dataset reflects the original theatrical release, not the date it was adopted by Netflix for streaming.''')



data = pd.read_csv("netflix/files/cleaned_netflix.csv")


print('Graph for total number of Movies released per year in Netflix OTT')

filtered_df = data[(data['release_year'] >= 1900) & (data['release_year'] <= 2025)]

movies_per_year = filtered_df[filtered_df['type'] == 'Movie'].groupby('release_year').size().reset_index(name='total_movies')
movies_per_year = movies_per_year.sort_values('release_year')

plt.figure(figsize=(14, 7))
plt.plot(movies_per_year['release_year'], movies_per_year['total_movies'], marker='o', linestyle='-', color='r', label='Movies')

plt.xlabel('Release Year', fontsize=14)
plt.ylabel('Total Movies Released', fontsize=14)
plt.title('Total Number of Movies Released per Year (1900–2025)', fontsize=16, fontweight='bold')
plt.legend(fontsize=12)


plt.xticks(ticks=range(int(movies_per_year['release_year'].min()), int(movies_per_year['release_year'].max())+1, 2), rotation=45, ha='right')

plt.tight_layout()


# Save the generated graph 
ans=input("Do you want to save the generated graph?{y/n} :").lower()
if ans in ('y','yes'):
    plt.savefig("img/movies_per_year/movies_per_year.png", dpi=300)
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
