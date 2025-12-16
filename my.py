# 1. Starter: Initialize the accumulator
total = 0 

print("Enter numbers one by one. Type 'done' to see the sum.")

# 2. Condition: Start an infinite loop
while True:
    
    # Action 1: Get input from the user (always a string)
    user_input = input("Enter a number or 'done': ")
    
    # 3. Stopper Check: If the user types 'done', exit the loop.
    if user_input == "done":
        break # Exit the loop immediately!
    
    # Logic 1: Check if the input is empty (a simple validation)
    if user_input == "":
        print("Empty entry, please try again.")
        continue # Skip the rest of this loop cycle and go back to 'while True:'
        
    # Logic 2: If we get here, we assume the input is a valid number.
    try: 
        # Convert the string input to an integer
        number = int(user_input)
        
        # Logic 3: Accumulate the value
        total += number
        
    except ValueError:
        # If the conversion fails (e.g., user typed "hello"), handle the error
        print("Invalid input. That was not a number.")
        # Loop continues because there is no 'break' or 'continue' here.
        
# Final Output: Runs only after the 'break' is executed.
print(f"\n--- Calculation Complete ---")
print(f"The total sum of all numbers entered is: {total}")