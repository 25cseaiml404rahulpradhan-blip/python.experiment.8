import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60]])

print("--- Statistical Operations ---")
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))
print("Variance:", np.var(arr))
print("Row-wise mean:", np.mean(arr, axis=1))
print("Column-wise max:", np.max(arr, axis=0))

print("\n--- Broadcasting ---")
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10
print("Broadcasting Scalar (Addition):\n", arr_2d + scalar)

row_vector = np.array([10, 20, 30])
print("\nBroadcasting Row Vector:\n", arr_2d + row_vector)

col_vector = np.array([[10], [20]])
print("\nBroadcasting Column Vector:\n", arr_2d + col_vector)
