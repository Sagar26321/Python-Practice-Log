# # # # # # # # fruits = ["apple", "banana"]


# # # # # # # # for index, fruit in enumerate(fruits):
# # # # # # # # 	print(f"Index {index}: {fruit}")
	

# # # # # # # # enumerate function adds a counter to an iterable and returns it as an enumerate object.
# # # # # # # # example usage:
# # # # # # # items = ["pen", "notebook", "eraser"]
# # # # # # # for idx, item in enumerate(items):
# # # # # # #     print(f"Item {idx}: {item}")   
# # # # # # # word = "Python"

# # # # # # # for char in word:
# # # # # # #     print(char)
# # # # # # person = {"name": "Bob", "age": 40, "city": "New York"}

# # # # # # # Iterating over both key and value
# # # # # # for k, v in person.items():
# # # # # #     print(f"The key is '{k}' and the value is '{v}'")

# # # # # # data_list = [5, 12, 3, 18, 9]
# # # # # # total_sum = 0
# # # # # # # Your code goes here: Loop through data_list and add each number to total_sum
# # # # # # # ...
# # # # # # # Expected Output: 47
# # # # # # for number in data_list:
# # # # # #     total_sum += number
# # # # # # print (f"Total Sum: {total_sum}")


# # # # # sentence = "A quick brown fox jumps over the lazy dog"
# # # # # vowels_only = ""
# # # # # vowels = "aeiouAEIOU"

# # # # # # Your code goes here: Loop through the sentence, check if the character is in 'vowels', and append it to vowels_only
# # # # # # ...

# # # # # # Expected Output: Auiouooueeao
# # # # # for char in sentence:
# # # # #     if char in vowels:
# # # # #         vowels_only += char
# # # # # print(f"Vowels Only: {vowels_only}")

# # # # number_list = [1, 4, 9, 12, 5, 20, 7]

# # # # # 1. Initialize: Create a variable called even_count and set its starting value to 0.
# # # # even_count = 0

# # # # # 2. Start Loop: Begin iterating through the number_list.
# # # # for number in number_list:
    
# # # #     # 3. Check Condition: Calculate the remainder when dividing it by 2.
# # # #     # 4. Decision: Is the remainder equal to 0?
# # # #     if number % 2 == 0:
        
# # # #         # 5. Action (If True): If the number is even, increase the even_count by 1.
# # # #         even_count = even_count + 1 # or even_count += 1
        
# # # # # 7. Final Output: Once the list is finished, print the final value.
# # # # print(f"Total even numbers found: {even_count}")



# # # # words = ["apple", "banana", "cat", "grapefruit", "dog", "kiwi"]

# # # # for word in words:
# # # #     if len(word) > 4:
# # # #         print(word)
# # # #     else:
# # # #         print("Short word")
# # # # Goal: Create a new list containing only the words from the input list that have more than 5 characters.

# # # prices = {"apple": 1.5, "banana": 0.5, "grape": 2.0, "kiwi": 1.0}
# # # total_prices =  0
# # # for fruits in prices:
# # #     total_prices += prices[fruits]
# # # print(f"Total Prices: {total_prices}")

# # # text = "Programming is awesome and challenging."
# # # a_count = 0
# # # for char in text:
# # #     if char == 'a' or char == 'A':
# # #         a_count += 1
# # # print (f"Total 'a' or 'A' characters: {a_count}")
# # # Goal: Print a list of the numbers 1 through 5, each prefixed with its index starting from 1 (i.e., "1. 1", "2. 2", ... "5. 5").
# # # for index, number in enumerate(range(1, 6), start=1):
# # #     print(f"{index}. {number}")

# # # The loop variable 'i' will take on the values 1, 2, 3, 4, 5 sequentially.
# # for i in range(1, 6):
    
# #     # We use the f-string to combine the variable 'i' (for the index)
# #     # with the variable 'i' again (for the value).
# #     print(f"{i}. {i}")


# numbers = [2, 7, 4, 1, 6, 9]
# squares = []
# for number in numbers:
#     squares.append(number ** 2)
# print(squares)  # Output: [4, 49, 16, 1, 36, 81]

scores = {"Alice": 92, "Bob": 78, "Charlie": 85, "David": 60}
#Expected Output: {'Alice': 92, 'Charlie': 85}
high_scorers = {}
for name, score in scores.items():
    if score >= 80:
        high_scorers[name] = score
print(high_scorers)