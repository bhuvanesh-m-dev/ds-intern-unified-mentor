import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv("/home/bhuvanesh-m-ubuntu/Desktop/Netflix/files/cleaned_netflix.csv")

# Filter for South Korea only
data_korea = data[data['country'].str.contains('South Korea', na=False)]

data_korea['date_added'] = pd.to_datetime(data_korea['date_added'], errors='coerce')
data_korea = data_korea.dropna(subset=['date_added'])

# Extract year, month, and day
data_korea['year_added'] = data_korea['date_added'].dt.year
data_korea['month_added'] = data_korea['date_added'].dt.month
data_korea['day_added'] = data_korea['date_added'].dt.day

# statistics for year_added
mean_year = data_korea['year_added'].mean()
median_year = data_korea['year_added'].median()
mode_year = data_korea['year_added'].mode()[0] if not data_korea['year_added'].mode().empty else None

print(f"Mean year (South Korea): {mean_year}")
print(f"Median year (South Korea): {median_year}")
print(f"Mode year (South Korea): {mode_year}")

# Visualize the distribution 
plt.figure(figsize=(10,6))
sns.histplot(data_korea['year_added'], bins=15, kde=False, color='skyblue')
plt.title('Distribution of Content Added to Netflix by Year (South Korea)')
plt.xlabel('Year Added')
plt.ylabel('Count')
plt.tight_layout()
# Save the generated graph 
ans = input("Do you want to save the generated graph?{y/n} :").lower()
if ans in ('y','yes'):
    import os
    os.makedirs("img/statistics/South_Korea", exist_ok=True)
    plt.savefig("img/statistics/South_Korea/date_added_south_korea.png", dpi=300)
    print('''Visit img folder to view the saved graph''')
else:
    print('''Generated graph will not save!''')
plt.show()
