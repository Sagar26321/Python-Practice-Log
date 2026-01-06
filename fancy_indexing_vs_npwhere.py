# Fancy Indexing vs np.where
import numpy as np
numbers = np.array([1,2,3,4,5,6,7,8,9,10])
indices = [0,2,4] # 0 is the first element, 2 is the third element, 4 is the fifth element
print("Fancy Indexing:", numbers[indices])

where_result = np.where(numbers > 5)
print("np.where result:", numbers[where_result])
print(where_result)
