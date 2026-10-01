import numpy as np

arr = np.array([[1, 2, 3], [4, 5, 6]])

print("--- Array Properties ---")
print("Dimensions:", arr.ndim)
print("Shape:", arr.shape)
print("Total size:", arr.size)
print("Data type:", arr.dtype)
print("Item size (bytes):", arr.itemsize)
print("Total bytes:", arr.nbytes)

print("\n--- Statistical & Mathematical Functions ---")
print("Sum of all elements:", np.sum(arr))
print("Column-wise sum:", np.sum(arr, axis=0))
print("Row-wise sum:", np.sum(arr, axis=1))
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print("Maximum value:", np.max(arr))
print("Minimum value:", np.min(arr))
print("Index of max value:", np.argmax(arr))

print("\n--- Structural Transformation Functions ---")
reshaped = arr.reshape(3, 2)
print("Reshaped array (3x2):\n", reshaped)

flattened = arr.flatten()
print("Flattened array:", flattened)

transposed = arr.T
print("Transposed array:\n", transposed)
