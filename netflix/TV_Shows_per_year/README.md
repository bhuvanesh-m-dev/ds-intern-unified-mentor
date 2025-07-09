# 📺 Netflix TV Shows Per Year

This project analyzes the **yearly trend of TV show releases** on the Netflix platform across different regions—**Worldwide, India, South Korea, and the USA**. It visualizes how the number of TV series has evolved year by year, helping to identify growth patterns in regional content offerings.

---

## 🌍 Global Trend

![TV Shows Worldwide](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/TV_Shows_per_year/series_per_year.png)

This graph illustrates the total number of TV shows released globally on Netflix, categorized by year.

---

## 🇮🇳 India

![TV Shows in India](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/TV_Shows_per_year/India/India.png)

This graph highlights the rise of Indian series on Netflix, year by year.

---

## 🇰🇷 South Korea

![TV Shows in South Korea](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/TV_Shows_per_year/South_Korea/South_Korea.png)

Korean dramas and series have seen significant growth. This plot shows how their presence on Netflix has evolved.

---

## 🇺🇸 USA

![TV Shows in USA](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/TV_Shows_per_year/USA/USA.png)

A consistent contributor to Netflix’s TV content, this graph shows annual U.S. series releases.

---

## 🐍 Python Script (Overview)

The data is grouped by country and release year, then plotted using `matplotlib`. Example snippet:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv('netflix_titles.csv')

# Filter TV Shows
tv_shows = df[df['type'] == 'TV Show']

# Convert 'date_added' to datetime
tv_shows['date_added'] = pd.to_datetime(tv_shows['date_added'])
tv_shows['year_added'] = tv_shows['date_added'].dt.year

# Group by year and country
country = 'India'  # Change to USA, South Korea, etc.
tv_shows_country = tv_shows[tv_shows['country'].str.contains(country, na=False)]
counts = tv_shows_country['year_added'].value_counts().sort_index()

# Plot
plt.figure(figsize=(10, 6))
plt.plot(counts.index, counts.values, marker='o')
plt.title(f'TV Shows Released Per Year in {country}')
plt.xlabel('Year')
plt.ylabel('Number of TV Shows')
plt.grid(True)
plt.tight_layout()
plt.savefig(f'netflix/img/TV_Shows_per_year/{country}/{country}.png')
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
