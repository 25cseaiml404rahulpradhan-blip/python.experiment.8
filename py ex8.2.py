import numpy as np

arr_int = np.array([1, 2, 3, 4], dtype=np.int32)
arr_float = np.array([1.5, 2.5, 3.5], dtype=np.float64)
arr_bool = np.array([1, 0, 1], dtype=np.bool_)
arr_str = np.array(["apple", "banana"], dtype=np.str_)

print("Data Types:")
print("Integer array type:", arr_int.dtype)
print("Float array type:", arr_float.dtype)
print("Boolean array type:", arr_bool.dtype)
print("String array type:", arr_str.dtype)

arr_converted = arr_int.astype(np.float32)
print("Converted type:", arr_converted.dtype)

matrix = np.array([[1, 2, 3], [4, 5, 6]])

print("\nStructural Properties:")
print("Data type (dtype):", matrix.dtype)
print("Dimensions (ndim):", matrix.ndim)
print("Shape (shape):", matrix.shape)
print("Total elements (size):", matrix.size)
print("Element size in bytes (itemsize):", matrix.itemsize)
print("Total size in bytes (nbytes):", matrix.nbytes)
