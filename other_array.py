import numpy as np
#  Flattened Array :-  Means in a single line
arr = np.arange(15)
print(arr)

reshape = arr.reshape((3,5))
print("Reshaped Array: ", reshape)

flattened  = reshape.flatten()
print("\n Flattened array: ", flattened)

raveled = reshape.ravel()  # ravel returns view instead of copy
print("\n raveled Array: ", raveled)

# TRANSPOSE:-
transpose = reshape.T
print("\n Transpose Array: ", transpose)