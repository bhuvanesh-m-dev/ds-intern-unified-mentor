import numpy as np

# 1. Introduction 
NumPy is a library for numerical operations on arrays and matrices.

# 2. Getting Started 
array = np.array([1, 2, 3, 4, 5])  
print("Array:", array)  

# 3. Creating Arrays 
zeros = np.zeros(5)  
ones = np.ones((2, 3))  
range_array = np.arange(0, 10, 2)  
print("Zeros:", zeros)  
print("Ones:\n", ones)  
print("Range Array:", range_array)  

# 4. Array Indexing 
print("First element:", array[0])  

# --- 5. Array Slicing ---
print("Sliced Array (1 to 3):", array[1:4])  

# 6. Data Types 
print("Data type:", array.dtype)  

# 7. Copy vs View 
copy_arr = array.copy()  
view_arr = array.view()  
copy_arr[0] = 100  
view_arr[1] = 200  
print("Original Array:", array)  
print("Copy Array:", copy_arr)  
print("View Array:", view_arr)  

# 8. Array Shape 
print("Shape:", array.shape)

# 9. Array Reshape 
reshaped = np.reshape(np.arange(6), (2, 3))  
print("Reshaped (2x3):\n", reshaped)

# 10. Array Iterating 
for x in array:
    print("Element:", x)

# 11. Array Join 
arr1 = np.array([1, 2])  
arr2 = np.array([3, 4])  
joined = np.concatenate((arr1, arr2))  
print("Joined Array:", joined)

# 12. Array Split 
split_arr = np.array_split(array, 3)  
print("Split Array:", split_arr)

# 13. Array Search 
search_index = np.where(array == 3)  
print("Index of 3:", search_index)

# 14. Array Sort 
unsorted = np.array([5, 2, 9, 1])  
sorted_arr = np.sort(unsorted)  
print("Sorted Array:", sorted_arr)

# 15. Array Filter
filter_condition = array > 3  
filtered = array[filter_condition]  
print("Filtered (array > 3):", filtered)

# 16. Max, Min, Mean, Std 
print("Max:", np.max(array))  
print("Min:", np.min(array))  
print("Mean:", np.mean(array))  
print("Std Dev:", np.std(array))

# 17. Element-wise Operations
squared = array ** 2  
print("Squared Elements:", squared)

# 18. Matrix Operations
matrix1 = np.array([[1, 2], [3, 4]])  
matrix2 = np.array([[5, 6], [7, 8]])  
product = np.dot(matrix1, matrix2)  
print("Matrix Product:\n", product)

# 19. Matrix Transpose
print("Transpose:\n", matrix1.T)  
