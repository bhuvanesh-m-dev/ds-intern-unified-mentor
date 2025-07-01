import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv("/home/bhuvanesh-m-ubuntu/Desktop/Netflix/files/cleaned_netflix.csv")

# Filter for India only
data_india = data[data['country'].str.contains('India', na=False)]

data_india['date_added'] = pd.to_datetime(data_india['date_added'], errors='coerce')
data_india = data_india.dropna(subset=['date_added'])

# Extract year, month, and day
data_india['year_added'] = data_india['date_added'].dt.year
data_india['month_added'] = data_india['date_added'].dt.month
data_india['day_added'] = data_india['date_added'].dt.day

# statistics for year_added
mean_year = data_india['year_added'].mean()
median_year = data_india['year_added'].median()
mode_year = data_india['year_added'].mode()[0] if not data_india['year_added'].mode().empty else None

print(f"Mean year (India): {mean_year}")
print(f"Median year (India): {median_year}")
print(f"Mode year (India): {mode_year}")

# Visualize the distribution 
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
