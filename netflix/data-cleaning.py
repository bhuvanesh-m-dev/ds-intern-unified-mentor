import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


data_by_csv=pd.read_csv("/home/bhuvanesh-m-ubuntu/Desktop/Netflix/files/netflix.csv")
data_by_csv.head() # default for first 5 rows


data_replaced = data_by_csv.replace([0, 'Not Given'], np.nan) # Replace 0, 'Not Given' with NaN
data_replaced


data_dropped = data_replaced.dropna() # Drop rows with NaN values
data_dropped


data_null=data_dropped.isnull().sum()#count the total number of null values
data_null

data_duplicate=data_dropped.duplicated().sum()#drop any duplicates
data_duplicate

data=data_dropped.copy()#to copy to simple
data

data



data.to_csv("/home/bhuvanesh-m-ubuntu/Desktop/Netflix/files/cleaned_netlix.csv",index=False)
