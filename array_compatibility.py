# Array Compatibility
import numpy as np
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.array([7,8,9])

print("Compatibility Shapes:",arr1.shape == arr2.shape)
print("Compatibility Shapes:",arr1.shape == arr3.shape) 
print("Compatibility Shapes:",arr2.shape == arr3.shape)
print("Compatibility Shapes:",arr1.shape == arr2.shape == arr3.shape)
print("Compatibility Shapes:",arr1.shape == arr2.shape == arr3.shape)

original_array = np.array([[1,2], [3,4,]])
new_row = np.array([5,6])

with_new_row = np.vstack((original_array, new_row))
print("original_array: ", original_array)
print("with_new_row: ", with_new_row)

new_column = np.array([[7], [8]])
with_new_column = np.hstack((original_array, new_column))
print("original_array: ", original_array)
print("with_new_column: ", with_new_column)

arr = np.array([1,2,3,4,5,6])
deleted_element = np.delete(arr, 2) # delete the third element : Start, Stop, Step
print("deleted_element: ", deleted_element)