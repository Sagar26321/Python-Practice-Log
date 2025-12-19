def check_password():
    while True:
        entry = input("Enter password: ")
        
        if entry == "python123":
            # Break the loop to reach the return line
            break
        else:
            print("Wrong! Try again.")
            
    return "Access Granted"

# Calling the function
status = check_password()
print(status)