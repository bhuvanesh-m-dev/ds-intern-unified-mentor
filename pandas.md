
# Pandas Python Library Guide

## Introduction

Pandas is a powerful and easy-to-use open-source data analysis and data manipulation library for Python. It provides flexible data structures like Series and DataFrame, making it simple to work with structured data.

## Getting Started

Install pandas using pip:

```bash
pip install pandas
```

Import pandas in your Python script:

```python
import pandas as pd
```

## Pandas Series

A Series is a one-dimensional labeled array capable of holding any data type.

**Example:**

```python
import pandas as pd
data = [10, 20, 30, 40]
series = pd.Series(data)
print(series)
```

## Pandas DataFrame

A DataFrame is a two-dimensional, size-mutable, and heterogeneous tabular data structure with labeled axes (rows and columns).

**Example:**

```python
import pandas as pd
data = {'Name': ['Alice', 'Bob'], 'Age': [25, 30]}
df = pd.DataFrame(data)
print(df)
```

## Read CSV

Read data from a CSV file into a DataFrame.

```python
df = pd.read_csv('data.csv')
```

## Read JSON

Read data from a JSON file into a DataFrame.

```python
df = pd.read_json('data.json')
```

## Analyze Data

Get a quick overview of your data:

```python
print(df.head())      # First 5 rows
print(df.info())      # Info about DataFrame
print(df.describe())  # Statistical summary
```

## Clean Data

### Clean Empty Cells

Remove rows with empty cells:

```python
df = df.dropna()
```

Fill empty cells with a value:

```python
df = df.fillna(0)
```

### Replace Data

Replace values in a column:

```python
df['column'] = df['column'].replace('old', 'new')
```

### Remove Duplicates

Remove duplicate rows:

```python
df = df.drop_duplicates()
```

---

For more, visit the [official documentation](https://pandas.pydata.org/).
