# Filtering numpy arrays and masking
import numpy as np
numbers = np.array([1,2,3,4,5,6,7,8,9,10])
even_numbers = numbers[numbers % 2 == 0]
print("Even Numbers:", even_numbers)

# filtering 2D arrays
arr_2d = np.array([[1,2,3], [4,5,6], [7,8,9]])
even_2d = arr_2d[arr_2d % 2 == 0]
print("Even 2D Array:", even_2d)

# filter with mask
mask = numbers > 5
print("Numbers greater than 5:", numbers[mask])

# what is mask?
# mask is a boolean array that is used to filter the array
#  in simple words, it is a way to filter the array based on a condition
# for example, if we want to filter the array based on a condition, we can use the mask