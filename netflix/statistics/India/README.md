# 📈 Netflix India Statistics: `date_added` vs `release_year`

This project presents **statistical analysis** on two key date fields in the Netflix dataset for **India**:

* **Date Added** to the Netflix platform
* **Release Year** of the content

It includes **distribution visualizations** specific to Indian content.

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

data_india = data[data['country'].str.contains('India', na=False)]

data_india['date_added'] = pd.to_datetime(data_india['date_added'], errors='coerce')
data_india = data_india.dropna(subset=['date_added'])

data_india['year_added'] = data_india['date_added'].dt.year
data_india['month_added'] = data_india['date_added'].dt.month
data_india['day_added'] = data_india['date_added'].dt.day

mean_year = data_india['year_added'].mean()
median_year = data_india['year_added'].median()
mode_year = data_india['year_added'].mode()[0] if not data_india['year_added'].mode().empty else None

print(f"Mean year (India): {mean_year}")
print(f"Median year (India): {median_year}")
print(f"Mode year (India): {mode_year}")

plt.figure(figsize=(10,6))
sns.histplot(data_india['year_added'], bins=10, kde=False, color='blue')
plt.title('Distribution of Content Added to Netflix by Year (India)')
plt.xlabel('Year Added')
plt.ylabel('Count')
plt.tight_layout()
# Save the generated graph 
ans = input("Do you want to save the generated graph?{y/n} :").lower()
if ans in ('y','yes'):
    import os
    os.makedirs("img/statistics", exist_ok=True)
    plt.savefig("img/statistics/India/date_added_india.png", dpi=300)
    print('''Visit img folder to view the saved graph''')
else:
    print('''Generated graph will not save!''')
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

data_usa = data[data['country'].str.contains('United States', na=False)]

data_usa['date_added'] = pd.to_datetime(data_usa['date_added'], errors='coerce')
data_usa = data_usa.dropna(subset=['date_added'])

data_usa['year_added'] = data_usa['date_added'].dt.year
data_usa['month_added'] = data_usa['date_added'].dt.month
data_usa['day_added'] = data_usa['date_added'].dt.day

mean_year = data_usa['release_year'].mean()
median_year = data_usa['release_year'].median()
mode_year = data_usa['release_year'].mode()[0] if not data_usa['release_year'].mode().empty else None

print(f"Mean release year (USA): {mean_year}")
print(f"Median release year (USA): {median_year}")
print(f"Mode release year (USA): {mode_year}")

plt.figure(figsize=(20,12))
sns.histplot(data_usa['release_year'], bins=20, kde=False, color='skyblue')
plt.title('Distribution of Content Released on Netflix by Year (USA)')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.tight_layout()

plt.xticks(
    ticks=range(int(data_usa['release_year'].min()), int(data_usa['release_year'].max()) + 1, 1),
    rotation=45,
    ha='right'
)


# Save the generated graph 
ans = input("Do you want to save the generated graph?{y/n} :").lower()
if ans in ('y','yes'):
    plt.savefig("img/statistics/USA/release_year.png", dpi=300)
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

