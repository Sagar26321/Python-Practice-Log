# sorting arrays
import numpy as np
unsorted_array = np.array([3,1,4,1,5,9,2,6,5,3,5])
print("sorted Array:", np.sort(unsorted_array))

arr_2d = np.array([[3,1,4], [1,5,9], [2,6,5]])
print("Sorted 2D Array:", np.sort(arr_2d, axis=0))