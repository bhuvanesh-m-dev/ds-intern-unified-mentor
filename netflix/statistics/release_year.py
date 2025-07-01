import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv("netflix/files/cleaned_netflix.csv")

# Use date_added for extracting year, month, day
data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')
data = data.dropna(subset=['date_added'])

data['year_added'] = data['date_added'].dt.year
data['month_added'] = data['date_added'].dt.month
data['day_added'] = data['date_added'].dt.day

# statistics for release_year (already integer)
mean_year = data['release_year'].mean()
median_year = data['release_year'].median()
mode_year = data['release_year'].mode()[0] if not data['release_year'].mode().empty else None

print(f"Mean release year: {mean_year}")
print(f"Median release year: {median_year}")
print(f"Mode release year: {mode_year}")

# Visualize the distribution of release_year
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
