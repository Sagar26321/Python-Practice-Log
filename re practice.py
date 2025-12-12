# # # calculate income tax based on income brackets
# # def calculate_income_tax(income):
# #     if income <= 10000:
# #         tax_rate = 0.0
# #     elif income <= 30000:
# #         tax_rate = 0.1
# #     elif income <= 100000:
# #         tax_rate = 0.2
# #     else:
# #         tax_rate = 0.3

# #     tax = income * tax_rate
# #     return tax
# # income = float(input("Enter your income: "))
# # tax = calculate_income_tax(income)
# # print(f"The income tax for an income of {income} is: {tax}")



# # palindrome checker
# def is_palindrome(s):
#     s = s.replace(" ", "").lower()  # remove spaces and convert to lowercase
#     return s == s[::-1]
# string = input("Enter a string: ")
# if is_palindrome(string):
#     print(f'"{string}" is a palindrome.')
# else:
#     print(f'"{string}" is not a palindrome.')


# The anagram detector

def are_anagrams(str1, str2): 
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
if are_anagrams(string1, string2):
    print(f'"{string1}" and "{string2}" are anagrams.')
else:
    print(f'"{string1}" and "{string2}" are not anagrams.')

    