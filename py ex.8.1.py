import numpy as np

# 1. Creating a 1-D ndarray
arr_1d = np.arange(10, 20)  # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print("Original 1-D Array:", arr_1d)

# 1-D Indexing (Positive and Negative)
print("Element at index 2:", arr_1d[2])       # 12
print("Element at last index (-1):", arr_1d[-1]) # 19

# 1-D Slicing [start:stop:step]
print("Slice from index 1 to 5:", arr_1d[1:5])      # [11, 12, 13, 14]
print("Slice with a step of 2:", arr_1d[0:8:2])      # [10, 12, 14, 16]
print("Reversed array:", arr_1d[::-1])              # Reverses the whole array

# 2. Creating a 2-D ndarray (Matrix)
arr_2d = np.array([[1, 2, 3], 
                   [4, 5, 6], 
                   [7, 8, 9]])
print("\nOriginal 2-D Array:\n", arr_2d)

# 2-D Indexing [row, column]
print("Element at row 1, col 2:", arr_2d[1, 2])     # 6 (Row index 1, Column index 2)

# 2-D Row and Column Selection
print("Entire row 0:", arr_2d[0, :])               # [1, 2, 3]
print("Entire column 1:", arr_2d[:, 1])            # [2, 5, 8]

# 2-D Slicing [row_start:row_stop, col_start:col_stop]
sub_matrix = arr_2d[0:2, 1:3]
print("\nSliced Sub-matrix (Rows 0-1, Cols 1-2):\n", sub_matrix)
# Output:
# [[2, 3],
#  [5, 6]]

# 3. Boolean/Conditional Indexing
print("\nElements greater than 5:", arr_1d[arr_1d > 15])  # [16, 17, 18, 19]
