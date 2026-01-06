# NUMPY ARRAY OPERATIONS:-
import numpy as np
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print("Basic Slicing:", arr[2:7])
print("Step Slicing:", arr[1:8:2])
print("Reverse Slicing:", arr[::-1])
arr_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
print("Specific Element:", arr_2d[1,2])
print("Entire Row:", arr_2d[1])
print("Entire Column:", arr_2d[:,1])
