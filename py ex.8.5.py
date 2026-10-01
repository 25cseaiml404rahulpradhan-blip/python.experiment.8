import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([[10, 20], [30, 40]])

print("--- 1. Saving & Loading Text Files (.txt) ---")
np.savetxt("single_array.txt", arr1)
loaded_txt = np.loadtxt("single_array.txt")
print("Loaded from Text:", loaded_txt)

print("\n--- 2. Saving & Loading Single Binary File (.npy) ---")
np.save("single_array.npy", arr1)
loaded_npy = np.load("single_array.npy")
print("Loaded from NPY:", loaded_npy)

print("\n--- 3. Saving & Loading Multiple Arrays (.npz) ---")
np.savez("multiple_arrays.npz", first=arr1, second=arr2)
loaded_npz = np.load("multiple_arrays.npz")
print("Keys available in NPZ:", list(loaded_npz.keys()))
print("Loaded First Array:\n", loaded_npz["first"])
print("Loaded Second Array:\n", loaded_npz["second"])

print("\n--- 4. Saving & Loading Compressed Multiple Arrays (.npz) ---")
np.savez_compressed("compressed_arrays.npz", first=arr1, second=arr2)
loaded_compressed = np.load("compressed_arrays.npz")
print("Loaded Compressed First Array:", loaded_compressed["first"])
