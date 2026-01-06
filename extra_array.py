# Extra Array Operations:- split, return index, return counts, move axis,swapaxes, flip
# split:- split the array into multiple sub-arrays
# return index:- return the index of the array
# return counts:- return the counts of the array
# move axis:- move the axis of the array
# swapaxes:- swap the axes of the array
# flip:- flip the array
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]]) 
print("Original 2D Array:\n", arr)
print("Shape:", arr.shape) 

# moveaxis:
move_axis_array = np.moveaxis(arr, 0, 1)
print("\nMove Axis Array (0 to 1):\n", move_axis_array)

# swapaxes: 
swapaxes_array = np.swapaxes(arr, 0, 1)
print("\nSwap Axes Array:\n", swapaxes_array)

# Flip:
flip_array = np.flip(arr, axis=0) 
print("\nFlipped Array (Rows):\n", flip_array)

# split:
split_array = np.split(arr, 2)
print("\nSplit Array:\n", split_array)
print("Shape of Split Array:", split_array[0].shape)
print("Shape of Split Array:", split_array[1].shape)

# return index:
index_array = np.where(arr == 3)
print("\nIndex Array (Tuple):", index_array)
print("Shape of Row Indices:", index_array[0].shape) 
print("Shape of Column Indices:", index_array[1].shape)

# return counts:
counts_array = np.count_nonzero(arr)
print("\nCounts Array:\n", counts_array)
print("Total Counts:", counts_array)
elements, counts = np.unique(arr, return_counts=True)
print("\nUnique Elements:", elements)
print("Counts of each element:", counts)
print("Shape of Counts Array:", counts.shape)