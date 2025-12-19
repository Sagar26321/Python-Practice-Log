def get_average():
    data = []
    
    while True:
        user_input = input("Enter a number (or '0' to finish): ")
        
        if user_input == "0":
            break
        else:
            # Add the integer version to our list
            data.append(int(user_input))
            
    # Calculate average: Total divided by Count
    avg = sum(data) / len(data)
    return avg

# Calling the function and showing the result
result = get_average()
print(f"The average is: {result}")