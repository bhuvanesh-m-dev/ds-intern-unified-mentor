
# NumPy Python Library Guide

## 1. Introduction

NumPy is a fundamental Python library for numerical computing. It provides support for large, multi-dimensional arrays and matrices, along with a collection of mathematical functions to operate on them efficiently.

## 2. Getting Started

Install NumPy using pip:

```bash
pip install numpy
```

Import NumPy in your Python script:

```python
import numpy as np
```

## 3. Creating Arrays

Create arrays of different types:

```python
array = np.array([1, 2, 3, 4, 5])
zeros = np.zeros(5)
ones = np.ones((2, 3))
range_array = np.arange(0, 10, 2)
print(array)
print(zeros)
print(ones)
print(range_array)
```

## 4. Array Indexing & Slicing

Access elements and slices:

```python
print(array[0])        # First element
print(array[1:4])      # Elements from index 1 to 3
```

## 5. Data Types

Check the data type of an array:

```python
print(array.dtype)
```

## 6. Copy vs View

Understand the difference between copying and viewing arrays:

```python
copy_arr = array.copy()
view_arr = array.view()
copy_arr[0] = 100
view_arr[1] = 200
print(array)      # Original array
print(copy_arr)   # Copy (independent)
print(view_arr)   # View (shares data)
```

## 7. Array Shape & Reshape

Get and change the shape of arrays:

```python
print(array.shape)
reshaped = np.reshape(np.arange(6), (2, 3))
print(reshaped)
```

## 8. Iterating Arrays

Loop through array elements:

```python
for x in array:
    print(x)
```

## 9. Joining & Splitting Arrays

Join and split arrays:

```python
arr1 = np.array([1, 2])
arr2 = np.array([3, 4])
joined = np.concatenate((arr1, arr2))
split_arr = np.array_split(array, 3)
print(joined)
print(split_arr)
```

## 10. Searching & Sorting

Find elements and sort arrays:

```python
search_index = np.where(array == 3)
unsorted = np.array([5, 2, 9, 1])
sorted_arr = np.sort(unsorted)
print(search_index)
print(sorted_arr)
```

## 11. Filtering Arrays

Filter elements based on a condition:

```python
filtered = array[array > 3]
print(filtered)
```

## 12. Aggregate Functions

Find max, min, mean, and standard deviation:

```python
print(np.max(array))
print(np.min(array))
print(np.mean(array))
print(np.std(array))
```

## 13. Element-wise Operations

Apply operations to each element:

```python
squared = array ** 2
print(squared)
```

## 14. Matrix Operations

Work with 2D arrays (matrices):

```python
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
product = np.dot(matrix1, matrix2)
print(product)
```

## 15. Matrix Transpose

Transpose a matrix:

```python
print(matrix1.T)
```

---

For more, visit the [official documentation](https://numpy.org/doc/).
