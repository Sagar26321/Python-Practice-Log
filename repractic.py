# # # fruits = ["apple", "banana"]


# # # for index, fruit in enumerate(fruits):
# # # 	print(f"Index {index}: {fruit}")
	

# # # enumerate function adds a counter to an iterable and returns it as an enumerate object.
# # # example usage:
# # items = ["pen", "notebook", "eraser"]
# # for idx, item in enumerate(items):
# #     print(f"Item {idx}: {item}")   
# # word = "Python"

# # for char in word:
# #     print(char)
# person = {"name": "Bob", "age": 40, "city": "New York"}

# # Iterating over both key and value
# for k, v in person.items():
#     print(f"The key is '{k}' and the value is '{v}'")

data_list = [5, 12, 3, 18, 9]
total_sum = 0
# Your code goes here: Loop through data_list and add each number to total_sum
# ...
# Expected Output: 47
for number in data_list:
    total_sum += number
print (f"Total Sum: {total_sum}")
