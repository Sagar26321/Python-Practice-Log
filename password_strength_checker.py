# Password Strength Checker Project
# This script checks the strength of a given password based on various criteria.
password = input("Enter a password to check its strength: ")
score = 0
has_upper = False
has_digit = False
has_special = False

for char in password:
    if char.isupper():
        has_upper = True
    if char.isdigit():
        has_digit = True
    if not char.isalnum():
        has_special = True

if len(password) >= 8:
    score += 1
if has_upper:
    score += 1
if has_digit:
    score += 1
if has_special:
    score += 1

print("\nPassword Strength Checker")
if score == 4:
    print("Strength: Very Strong")  
elif score == 3:
    print("Strength: Strong")
elif score == 2:
    print("Strength: Moderate")
elif score == 1:
    print("Strength: Weak")
else:
     print("Strength: Very Weak")

if not has_special:
    print(" Add a special character (e.g., @, #, !) to make it stronger.")
if len(password) < 8:
    print(" Make your password at least 8 characters long.")

print(f'Your password score is: {score}/4')