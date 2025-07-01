import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv("/home/bhuvanesh-m-ubuntu/Desktop/Netflix/files/cleaned_netflix.csv")

# Filter for USA only
data_usa = data[data['country'].str.contains('United States', na=False)]

# Use date_added for extracting year, month, day
data_usa['date_added'] = pd.to_datetime(data_usa['date_added'], errors='coerce')
data_usa = data_usa.dropna(subset=['date_added'])

data_usa['year_added'] = data_usa['date_added'].dt.year
data_usa['month_added'] = data_usa['date_added'].dt.month
data_usa['day_added'] = data_usa['date_added'].dt.day

# statistics for release_year (already integer)
mean_year = data_usa['release_year'].mean()
median_year = data_usa['release_year'].median()
mode_year = data_usa['release_year'].mode()[0] if not data_usa['release_year'].mode().empty else None

print(f"Mean release year (USA): {mean_year}")
print(f"Median release year (USA): {median_year}")
print(f"Mode release year (USA): {mode_year}")

# Visualize the distribution of release_year
plt.figure(figsize=(20,12))
sns.histplot(data_usa['release_year'], bins=20, kde=False, color='skyblue')
plt.title('Distribution of Content Released on Netflix by Year (USA)')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.tight_layout()

# Set x-axis ticks every 2 years
plt.xticks(
    ticks=range(int(data_usa['release_year'].min()), int(data_usa['release_year'].max()) + 1, 1),
    rotation=45,
    ha='right'
)

plt.savefig("release_year_distribution_usa.png", dpi=300)

# Save the generated graph 
ans = input("Do you want to save the generated graph?{y/n} :").lower()
if ans in ('y','yes'):
    import os
    os.makedirs("img/statistics/USA", exist_ok=True)
    plt.savefig("img/statistics/USA/release_year.png", dpi=300)
    print('''Visit img folder to view the saved graph''')
else:
    print('''Generated graph will not save!''')
plt.show()