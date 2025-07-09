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
import matplotlib.pyplot as plt

df = pd.read_csv("netflix/files/cleaned_netflix.csv")

# Filter valid years
df = df[(df['release_year'] >= 1900) & (df['release_year'] <= 2025)]

# Group by type and year
grouped = df.groupby(['release_year', 'type']).size().unstack().fillna(0)
grouped['Total'] = grouped.sum(axis=1)

plt.figure(figsize=(14, 7))
plt.plot(grouped.index, grouped['Total'], marker='o', linestyle='-', color='black', label='Total Content')
plt.plot(grouped.index, grouped['Movie'], linestyle='--', color='red', label='Movies')
plt.plot(grouped.index, grouped['TV Show'], linestyle='--', color='blue', label='TV Shows')

plt.title('Netflix Total Content Released Per Year (1900–2025)', fontsize=16, fontweight='bold')
plt.xlabel('Release Year', fontsize=14)
plt.ylabel('Total Titles Released', fontsize=14)
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

ans = input("Do you want to save the generated graph? (y/n): ").lower()
if ans in ('y', 'yes'):
    plt.savefig("img/mergered_graph/merged_graph.png", dpi=300)
    print("Graph saved successfully.")
else:
    print("Graph was not saved.")

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

