import pandas as pd
import numpy as np

# Read the CSV file
data = pd.read_csv("customer_support_tickets.csv")

# Print columns to see what's available
print("Available columns in the dataset:")
print(data.columns.tolist())

# Define columns we want to check (only those that exist in the DataFrame)
columns_to_check = ['Resolution', 'First Response', 'Time to Response']
# Filter to only include columns that actually exist
existing_columns = [col for col in columns_to_check if col in data.columns]

if len(existing_columns) < len(columns_to_check):
    missing_cols = set(columns_to_check) - set(existing_columns)
    print(f"\nWarning: The following columns were not found and will be skipped: {missing_cols}")

if not existing_columns:
    raise ValueError("None of the specified columns exist in the dataset")

# Replace empty strings or blanks with NaN in specific columns
data[existing_columns] = data[existing_columns].replace(['', ' ', None, 'Not Given'], np.nan)

# Drop rows where any of the specified columns have NaN values
data_cleaned = data.dropna(subset=existing_columns)

# Check for remaining null values
null_counts = data_cleaned.isnull().sum()
print("\nNull value counts after cleaning:")
print(null_counts)

# Check for duplicates
duplicate_count = data_cleaned.duplicated().sum()
print(f"\nNumber of duplicates: {duplicate_count}")

# Save the cleaned data to a new CSV file
data_cleaned.to_csv("data.csv", index=False)

print("\nData cleaning complete. Cleaned data saved to 'data.csv'")
