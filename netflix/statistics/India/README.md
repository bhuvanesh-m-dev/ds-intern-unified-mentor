# 📈 Netflix India Statistics: `date_added` vs `release_year`

This project presents **statistical analysis** on two key date fields in the Netflix dataset for **India**:

* **Date Added** to the Netflix platform
* **Release Year** of the content

It includes **mean**, **median**, and **mode** values, along with **distribution visualizations** specific to Indian content.

---

## 🇮🇳 India

### 📅 Date Added Distribution

![Date Added - India](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/statistics/India/date_added_india.png)

### 🎬 Release Year Distribution

![Release Year - India](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/statistics/India/release_year.png)

---

## 🐍 Python Script: `date_added` (India)

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv("netflix/files/cleaned_netflix.csv")
data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')
data = data.dropna(subset=['date_added'])

# Filter for India only
data_india = data[data['country'].str.contains("India", na=False)]
data_india['year_added'] = data_india['date_added'].dt.year

date_stats = {
    'Mean': data_india['year_added'].mean(),
    'Median': data_india['year_added'].median(),
    'Mode': data_india['year_added'].mode()[0] if not data_india['year_added'].mode().empty else None
}

print(date_stats)

plt.figure(figsize=(10, 6))
sns.histplot(data_india['year_added'], bins=20, color='skyblue')
plt.title('India: Distribution of Content Added to Netflix by Year')
plt.xlabel('Year Added')
plt.ylabel('Count')
plt.tight_layout()

ans = input("Do you want to save the generated graph?{y/n}: ").lower()
if ans in ('y', 'yes'):
    plt.savefig("img/statistics/India/date_added_india.png", dpi=300)
    print("Visit img folder to view the saved graph")
else:
    print("Generated graph will not save!")

plt.show()
```

---

## 🐍 Python Script: `release_year` (India)

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv("netflix/files/cleaned_netflix.csv")
data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')
data = data.dropna(subset=['date_added'])

# Filter for India only
data_india = data[data['country'].str.contains("India", na=False)]
data_india['year_added'] = data_india['date_added'].dt.year

year_stats = {
    'Mean': data_india['release_year'].mean(),
    'Median': data_india['release_year'].median(),
    'Mode': data_india['release_year'].mode()[0] if not data_india['release_year'].mode().empty else None
}

print(year_stats)

plt.figure(figsize=(10, 6))
sns.histplot(data_india['release_year'], bins=20, color='skyblue')
plt.title('India: Distribution of Content Released on Netflix by Year')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.tight_layout()

ans = input("Do you want to save the generated graph?{y/n}: ").lower()
if ans in ('y', 'yes'):
    plt.savefig("img/statistics/India/release_year.png", dpi=300)
    print("Visit img folder to view the saved graph")
else:
    print("Generated graph will not save!")

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

