import numpy as np

harvest_data = np.array([
    [50, 55, 60, 52, 65, 70, 75], 
    [30, 32, 28, 35, 33, 40, 42],  
    [100, 95, 105, 110, 98, 120, 125], 
    [40, 38, 42, 45, 41, 50, 55]  
])

print("--- Part 1: Array Properties and Restructuring ---")
print("Shape:", harvest_data.shape)
print("Number of dimensions:", harvest_data.ndim)
print("Total size:", harvest_data.size)

restructured_data = harvest_data.T
print("\nRestructured Array (Rows=Days, Columns=Crops):\n", restructured_data)

print("\n--- Part 2: Statistical Operations ---")
weekly_yield = np.sum(harvest_data, axis=1)
print("Weekly crop yield (Tomatoes, Carrots, Potatoes, Onions):", weekly_yield)

daily_avg = np.mean(harvest_data, axis=0)
print("Daily average across all crops (Mon to Sun):", daily_avg)

best_day = np.max(harvest_data)
print("Maximum single-crop daily yield:", best_day)

print("\n--- Part 3: Broadcasting ---")
daily_bonus = np.array([0, 0, 0, 0, 5, 10, 15])
harvest_with_bonus = harvest_data + daily_bonus
print("Harvest data after fertilizer bonus:\n", harvest_with_bonus)

shrinkage_factors = np.array([0.85, 0.98, 0.99, 0.97])
final_transported_weight = harvest_with_bonus * shrinkage_factors[:, np.newaxis]
print("\nFinal transported weight after shrinkage:\n", final_transported_weight)

output
--- Part 1: Array Properties and Restructuring ---
Shape: (4, 7)
Number of dimensions: 2
Total size: 28

Restructured Array (Rows=Days, Columns=Crops):
 [[ 50  30 100  40]
 [ 55  32  95  38]
 [ 60  28 105  42]
 [ 52  35 110  45]
 [ 65  33  98  41]
 [ 70  40 120  50]
 [ 75  42 125  55]]

--- Part 2: Statistical Operations ---
Weekly crop yield (Tomatoes, Carrots, Potatoes, Onions): [427 240 753 311]
Daily average across all crops (Mon to Sun): [55.   55.   58.75 60.5  59.25 70.   74.25]
Maximum single-crop daily yield: 125

--- Part 3: Broadcasting ---
Harvest data after fertilizer bonus:
 [[ 50  55  60  52  70  80  90]
 [ 30  32  28  35  38  50  57]
 [100  95 105 110 103 130 140]
 [ 40  38  42  45  46  60  70]]

Final transported weight after shrinkage:
 [[ 42.5   46.75  51.    44.2   59.5   68.    76.5 ]
 [ 29.4   31.36  27.44  34.3   37.24  49.    55.86]
 [ 99.    94.05 103.95 108.9  101.97 128.7  138.6 ]
 [ 38.8   36.86  40.74  43.65  44.62  58.2   67.9 ]]

