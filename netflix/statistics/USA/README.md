# 📈 Netflix USA Statistics: `date_added` vs `release_year`

This project presents **statistical analysis** on two key date fields in the Netflix dataset for **USA**:

* **Date Added** to the Netflix platform
* **Release Year** of the content

It includes **distribution visualizations** specific to U.S. content.

---

## 🇺🇸 USA

### 📅 Date Added Distribution

![Date Added - USA](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/statistics/USA/date_added_usa.png)

### 🎬 Release Year Distribution

![Release Year - USA](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/statistics/USA/release_year.png)

---

## 🐍 Python Script: `date_added` (USA)

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

mean_year = data_usa['year_added'].mean()
median_year = data_usa['year_added'].median()
mode_year = data_usa['year_added'].mode()[0] if not data_usa['year_added'].mode().empty else None

print(f"Mean year (USA): {mean_year}")
print(f"Median year (USA): {median_year}")
print(f"Mode year (USA): {mode_year}")

plt.figure(figsize=(10,6))
sns.histplot(data_usa['year_added'], bins=20, kde=False, color='skyblue')
plt.title('Distribution of Content Added to Netflix by Year (USA)')
plt.xlabel('Year Added')
plt.ylabel('Count')
plt.tight_layout()
# Save the generated graph 
ans = input("Do you want to save the generated graph?{y/n} :").lower()
if ans in ('y','yes'):
    import os
    os.makedirs("img/statistics/USA", exist_ok=True)
    plt.savefig("img/statistics/USA/date_added_usa.png", dpi=300)
    print('''Visit img folder to view the saved graph''')
else:
    print('''Generated graph will not save!''')
plt.show()
```

---

## 🐍 Python Script: `release_year` (USA)

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

