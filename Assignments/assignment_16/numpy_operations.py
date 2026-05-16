import numpy as np

# Set the random seed and generate the initial array
np.random.seed(42)
data_array = np.random.randint(1, 501, size=(10, 10))

# 1. Find global mean and replace elements greater than the mean with 0
global_mean = data_array.mean()
data_array[data_array > global_mean] = 0

# 2. Calculate sum of each column and standard deviation of each row
col_sums = data_array.sum(axis=0)
row_stds = data_array.std(axis=1)

# 3. Slice center 4x4 sub-matrix (rows 3-6, columns 3-6) and flatten to 1D
# Note: In Python indexing, rows/columns 3-6 correspond to index bounds [3:7]
center_matrix = data_array[3:7, 3:7]
flat_center = center_matrix.flatten()

# Print results
print("Global Mean:", global_mean)
print("Column Sums:", col_sums)
print("Row Standard Deviations:\n", row_stds)
print("Flattened Center Matrix:\n", flat_center)
