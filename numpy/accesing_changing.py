import numpy as np

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

# Get a specific element [r, c]
a[1, 5] # 13

# Get a specific row
a[0, :] # [1, 2, 3, 4, 5, 6, 7]

# Get a specific column
a[:, 2] # [3, 10]

# Getting a little more fancy [startindex:endindex:stepsize]
a[0, 1:6:2] # [2, 4, 6]

# Change an element
a[1, 5] = 20

# Change a column
a[:, 2] = [1, 2]

# Change a row
a[1, :] = [1, 2, 3, 4, 5, 6, 7]

# 3-D example
b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

# Get specific element (work outside in)
b[0, 1, 1] # 4

# Replace
b[:, 1, :] = [[9, 9], [8, 8]]

