import numpy as np

a = np.array([1, 2, 3])

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])

# Get Dimension
a.ndim

# Get Shape
b.shape

# Get Type
a.dtype

# Get Size
a.itemsize

# Get total size
a.size * a.itemsize # or a.nbytes