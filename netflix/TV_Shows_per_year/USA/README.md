# 📺 Netflix TV Shows in USA (Per Year)

This project analyzes the **yearly trend of TV show releases** on the Netflix platform specifically for the **USA**. It visualizes how the number of American TV series released on Netflix has changed over the years.

---

## 🇺🇸 USA

![TV Shows in USA](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/TV_Shows_per_year/USA/USA.png)

This graph highlights the annual trend of U.S.-produced series released on Netflix.

---

## 🐍 Python Script (Overview)

The data is filtered for U.S. content and grouped by release year, then plotted using `matplotlib`. Example snippet:

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
country = 'United States'
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
plt.savefig(f'netflix/img/TV_Shows_per_year/USA/USA.png')
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

