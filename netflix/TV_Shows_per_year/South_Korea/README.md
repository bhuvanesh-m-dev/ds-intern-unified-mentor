# 📺 Netflix TV Shows in South Korea (Per Year)

This project analyzes the **yearly trend of TV show releases** on the Netflix platform specifically for **South Korea**. It visualizes how the number of South Korean TV series released on Netflix has changed over the years.

---

## 🇰🇷 South Korea

![TV Shows in South Korea](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/TV_Shows_per_year/South_Korea/South_Korea.png)

This graph highlights the growth of South Korean series on Netflix, year by year.

---

## 🐍 Python Script (Overview)


```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("netflix/files/cleaned_netflix.csv")

data_korea = data[data['country'].str.contains('South Korea', na=False)]

print('Graph for total number of TV Shows (series) released per year in Netflix OTT (South Korea only)')

filtered_df = data_korea[(data_korea['release_year'] >= 1900) & (data_korea['release_year'] <= 2025)]

tv_per_year = filtered_df[filtered_df['type'] == 'TV Show'].groupby('release_year').size().reset_index(name='total_tv_shows')
tv_per_year = tv_per_year.sort_values('release_year')

plt.figure(figsize=(14, 7))
plt.plot(tv_per_year['release_year'], tv_per_year['total_tv_shows'], marker='x', linestyle='--', color='b', label='TV Shows')

plt.xlabel('Release Year', fontsize=14)
plt.ylabel('Total TV Shows Released', fontsize=14)
plt.title('Total Number of TV Shows Released per Year in South Korea (1900–2025)', fontsize=16, fontweight='bold')
plt.legend(fontsize=12)

plt.xticks(ticks=range(int(tv_per_year['release_year'].min()), int(tv_per_year['release_year'].max())+1, 2), rotation=45, ha='right')

plt.tight_layout()

# Save the generated graph 
ans = input("Do you want to save the generated graph?{y/n} :").lower()
if ans in ('y','yes'):
    plt.savefig("img/TV_Shows_per_year/South_Korea/South_Korea.png", dpi=300)
    print('''Visit img folder to view the saved graph''')
else:
    print('''Generated graph will not save!''')
plt.show()
```

---

## 🙋‍♂️ Author

**Bhuvanesh M**
🌐 [bhuvaneshm.in](https://bhuvaneshm.in)
🔗 [linkedin.com/in/bhuvaneshm-developer](https://www.linkedin.com/in/bhuvaneshm-developer)
✍️ [dev.to/bhuvaneshm\_dev](https://dev.to/bhuvaneshm_dev)
📊 [kaggle.com/bhuvaneshm06](https://www.kaggle.com/bhuvaneshm06)

---

