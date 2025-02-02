import numpy as np

# Create a 7000 x 7000 NumPy array
cols = 7000
rows = 7000
array = np.arange(cols, dtype=np.int64).repeat(rows).reshape(rows, cols)

# Compute the sum of all elements (column-wise traversal)
total_sum = np.sum(array.T)  # Transposing ensures column-wise traversal

print(total_sum)
