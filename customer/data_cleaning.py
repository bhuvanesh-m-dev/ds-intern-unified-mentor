import pandas as pd
import numpy as np

data = pd.read_csv("/content/sample_data/customer_support_tickets.csv")

print("Available columns in the dataset:")
print(data.columns.tolist())

columns_to_check = ['Resolution', 'First Response', 'Time to Response']
existing_columns = [col for col in columns_to_check if col in data.columns]

if len(existing_columns) < len(columns_to_check):
    missing_cols = set(columns_to_check) - set(existing_columns)
    print(f"\nWarning: The following columns were not found and will be skipped: {missing_cols}")

if not existing_columns:
    raise ValueError("None of the specified columns exist in the dataset")

data[existing_columns] = data[existing_columns].replace(['', ' ', None, 'Not Given'], np.nan)

data_cleaned = data.dropna(subset=existing_columns)

null_counts = data_cleaned.isnull().sum()
print("\nNull value counts after cleaning:")
print(null_counts)

duplicate_count = data_cleaned.duplicated().sum()
print(f"\nNumber of duplicates: {duplicate_count}")

data_cleaned.to_csv("data.csv", index=False)

print("\nData cleaning complete. Cleaned data saved to 'data.csv'")
