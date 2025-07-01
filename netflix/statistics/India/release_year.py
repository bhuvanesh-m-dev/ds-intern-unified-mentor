import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv("/home/bhuvanesh-m-ubuntu/Desktop/Netflix/files/cleaned_netflix.csv")

# Filter for India only
data_india = data[data['country'].str.contains('India', na=False)]

# Use date_added for extracting year, month, day
data_india['date_added'] = pd.to_datetime(data_india['date_added'], errors='coerce')
data_india = data_india.dropna(subset=['date_added'])

data_india['year_added'] = data_india['date_added'].dt.year
data_india['month_added'] = data_india['date_added'].dt.month
data_india['day_added'] = data_india['date_added'].dt.day

# statistics for release_year (already integer)
mean_year = data_india['release_year'].mean()
median_year = data_india['release_year'].median()
mode_year = data_india['release_year'].mode()[0] if not data_india['release_year'].mode().empty else None

print(f"Mean release year (India): {mean_year}")
print(f"Median release year (India): {median_year}")
print(f"Mode release year (India): {mode_year}")

# Visualize the distribution of release_year
plt.figure(figsize=(10,6))
sns.histplot(data_india['release_year'], bins=20, kde=False, color='skyblue')
plt.title('Distribution of Content Released on Netflix by Year (India)')
plt.xlabel('Release Year')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("release_year_distribution_india.png", dpi=300)

# Save the generated graph 
ans = input("Do you want to save the generated graph?{y/n} :").lower()
if ans in ('y','yes'):
    plt.savefig("img/statistics/India/release_year.png", dpi=300)
    print('''Visit img folder to view the saved graph''')
else:
    print('''Generated graph will not save!''')
plt.show()
