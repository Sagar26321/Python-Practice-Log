#  Conditional Array Operations
import numpy as np
numbers = np.array([1,2,3,4,5,6,7,8,9,10])
condition_array = numbers > 5
np.where(condition_array)
print("Condition Array:", condition_array)
condition_array = np.where(numbers > 5, numbers * 3, numbers) # numbers * 3 is the value if the condition is true, numbers is the value if the condition is false
print("Condition Array:", condition_array)
