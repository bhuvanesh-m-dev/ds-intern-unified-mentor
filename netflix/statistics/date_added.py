import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv("/home/bhuvanesh-m-ubuntu/Desktop/Netflix/files/cleaned_netflix.csv")


data['date_added'] = pd.to_datetime(data['date_added'], errors='coerce')
data = data.dropna(subset=['date_added'])

# Extract year, month, and day
data['year_added'] = data['date_added'].dt.year
data['month_added'] = data['date_added'].dt.month
data['day_added'] = data['date_added'].dt.day

# statistics for year_added
mean_year = data['year_added'].mean()
median_year = data['year_added'].median()
mode_year = data['year_added'].mode()[0] if not data['year_added'].mode().empty else None

print(f"Mean year: {mean_year}")
print(f"Median year: {median_year}")
print(f"Mode year: {mode_year}")

# Visualize the distribution 
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
