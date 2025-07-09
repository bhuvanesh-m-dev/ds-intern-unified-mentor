import pandas as pd 
df = pd.read_csv('data.csv') 
ages = df['Customer Age'] 
mean_age = ages.mean() 
median_age = ages.median() 
mode_age = ages.mode()[0] 
print(f"Mean Customer Age: {mean_age:.2f}") 
print(f"Median Customer Age: {median_age:.2f}") 
print(f"Mode Customer Age: {mode_age:.2f}")
