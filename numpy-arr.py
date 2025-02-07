import numpy as np

cols = 7000
rows = 7000
array = np.arange(cols, dtype=np.int64).repeat(rows).reshape(rows, cols)

summa = sum(np.sum(array, axis=0))

print(summa)