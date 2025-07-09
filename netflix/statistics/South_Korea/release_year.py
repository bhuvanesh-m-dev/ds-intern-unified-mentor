import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv("netflix/files/cleaned_netflix.csv")

data_korea = data[data['country'].str.contains('South Korea', na=False)]

data_korea['date_added'] = pd.to_datetime(data_korea['date_added'], errors='coerce')
data_korea = data_korea.dropna(subset=['date_added'])

data_korea['year_added'] = data_korea['date_added'].dt.year
data_korea['month_added'] = data_korea['date_added'].dt.month
data_korea['day_added'] = data_korea['date_added'].dt.day

mean_year = data_korea['release_year'].mean()
median_year = data_korea['release_year'].median()
mode_year = data_korea['release_year'].mode()[0] if not data_korea['release_year'].mode().empty else None

print(f"Mean release year (South Korea): {mean_year}")
print(f"Median release year (South Korea): {median_year}")
print(f"Mode release year (South Korea): {mode_year}")

plt.figure(figsize=(10,6))
sns.histplot(data_korea['release_year'], bins=20, kde=False, color='skyblue')
plt.title('Distribution of Content Released on Netflix by Year (South Korea)')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.tight_layout()
plt.xticks(
    ticks=range(int(data_korea['release_year'].min()), int(data_korea['release_year'].max()) + 1, 2),
    rotation=45,
    ha='right'
)

# Save the generated graph 
ans = input("Do you want to save the generated graph?{y/n} :").lower()
if ans in ('y','yes'):
    plt.savefig("img/statistics/South_Korea/release_year.png", dpi=300)
    print('''Visit img folder to view the saved graph''')
else:
    print('''Generated graph will not save!''')
plt.show()
