def add(x, y):
    return x + y
def multiply(x, y):
    return x * y
user_choice = input("Type 'A' to Add or 'M' to Multiply: ").upper()
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if user_choice == 'A':
    result = add(num1, num2)
    print(f"The sum is: {result}")
elif user_choice == 'M':
    result = multiply(num1, num2)
    print(f"The product is: {result}")
else:
    print("Invalid choice. Please type 'A' or 'M'.")