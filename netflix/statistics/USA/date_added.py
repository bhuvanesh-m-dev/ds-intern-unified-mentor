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
