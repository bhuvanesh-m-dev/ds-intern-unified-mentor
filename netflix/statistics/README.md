# 📈 Netflix Global Statistics: `date_added` vs `release_year`

This project presents **statistical analysis** on two key date fields in the Netflix dataset:

* **Date Added** to the Netflix platform
* **Release Year** of the content

It includes **distribution visualizations** for global data and country-specific subsets—India, South Korea, and the USA.

---

## 🌍 Global Statistics

### 📅 Date Added Distribution

![Date Added - Global](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/statistics/date_added.png)

### 🎬 Release Year Distribution

![Release Year - Global](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/statistics/release_year.png)   
[For more details.](https://github.com/bhuvanesh-m-dev/ds-intern-unified-mentor/tree/main/netflix/statistics)

---

## 🇮🇳 India

### 📅 Date Added Distribution

![Date Added - India](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/statistics/India/date_added_india.png)

### 🎬 Release Year Distribution

![Release Year - India](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/statistics/India/release_year.png)      
[For more details.](https://github.com/bhuvanesh-m-dev/ds-intern-unified-mentor/tree/main/netflix/statistics/India)

---

## 🇰🇷 South Korea

### 📅 Date Added Distribution

![Date Added - South Korea](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/statistics/South_Korea/date_added_south_korea.png)

### 🎬 Release Year Distribution

![Release Year - South Korea](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/statistics/South_Korea/release_year.png)   
[For more details.](https://github.com/bhuvanesh-m-dev/ds-intern-unified-mentor/tree/main/netflix/statistics/South_Korea)

---

## 🇺🇸 USA

### 📅 Date Added Distribution

![Date Added - USA](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/statistics/USA/date_added_usa.png)

### 🎬 Release Year Distribution

![Release Year - USA](https://raw.githubusercontent.com/bhuvanesh-m-dev/ds-intern-unified-mentor/refs/heads/main/netflix/img/statistics/USA/release_year.png)    
[For more details.](https://github.com/bhuvanesh-m-dev/ds-intern-unified-mentor/tree/main/netflix/statistics/USA)

---

## 🐍 Python Script: `date_added`

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv("netflix/files/cleaned_netflix.csv")


data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')
data = data.dropna(subset=['date_added'])

data['year_added'] = data['date_added'].dt.year
data['month_added'] = data['date_added'].dt.month
data['day_added'] = data['date_added'].dt.day

mean_year = data['year_added'].mean()
median_year = data['year_added'].median()
mode_year = data['year_added'].mode()[0] if not data['year_added'].mode().empty else None

print(f"Mean year: {mean_year}")
print(f"Median year: {median_year}")
print(f"Mode year: {mode_year}")

plt.figure(figsize=(10,6))
sns.histplot(data['year_added'], bins=20, kde=False, color='skyblue')
plt.title('Distribution of Content Added to Netflix by Year')
plt.xlabel('Year Added')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("year_added_distribution.png", dpi=300)
# Save the generated graph 
ans=input("Do you want to save the generated graph?{y/n} :").lower()
if ans in ('y','yes'):
    plt.savefig("img/statistics/date_added.png", dpi=300)
    print('''Visit img folder to view the saved graph''')
else:
    print('''Generated graph will not save!''')
plt.show()
```

---

## 🐍 Python Script: `release_year`

```python
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv("netflix/files/cleaned_netflix.csv")

data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')
data = data.dropna(subset=['date_added'])

data['year_added'] = data['date_added'].dt.year
data['month_added'] = data['date_added'].dt.month
data['day_added'] = data['date_added'].dt.day

mean_year = data['release_year'].mean()
median_year = data['release_year'].median()
mode_year = data['release_year'].mode()[0] if not data['release_year'].mode().empty else None

print(f"Mean release year: {mean_year}")
print(f"Median release year: {median_year}")
print(f"Mode release year: {mode_year}")

plt.figure(figsize=(10,6))
sns.histplot(data['release_year'], bins=20, kde=False, color='skyblue')
plt.title('Distribution of Content Released on Netflix by Year')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("release_year_distribution.png", dpi=300)

# Save the generated graph 
ans = input("Do you want to save the generated graph?{y/n} :").lower()
if ans in ('y','yes'):
    plt.savefig("img/statistics/release_year.png", dpi=300)
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

