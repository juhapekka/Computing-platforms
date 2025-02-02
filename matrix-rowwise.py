# Create a <cols> x <rows> size two-dimensional array
cols = 7000
rows = 7000
array = [[i for i in range(cols)] for j in range(rows)]

# Compute the sum of all elements in the array
sum = 0
for j in range(rows):
    for i in range(cols):
        sum += array[j][i]

print(sum)
