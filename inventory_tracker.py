# The main dictionary stores the item name (Key) and the stock level (Value).
inventory = {
    "Laptop": 15,
    "Mouse": 50,
    "Keyboard": 30,
    "Monitor": 10
}

print("--- Welcome to the Inventory Console ---")

# The main loop keeps the program running until the user types 'exit'
while True:
    print("\n--- Menu ---")
    print("Type 'list' to see all stock.")
    print("Type 'check' to look up a specific item.")
    print("Type 'add' to increase stock.")
    print("Type 'exit' to quit the program.")

    command = input("Enter your command: ").lower().strip()

    # 1. Exit Logic
    if command == 'exit':
        print("Exiting Inventory Console. Goodbye!")
        break # This command stops the 'while True' loop and ends the program

    # 2. List All Stock Logic (Using a for loop)
    elif command == 'list':
        print("\nCurrent Warehouse Stock:")
        # Iterate over the dictionary to print keys and values
        for item, count in inventory.items(): 
            print(f"- {item}: {count} in stock")

    # 3. Check Specific Item Logic (Using if/else)
    elif command == 'check':
        item_to_check = input("Enter the item name to check: ").strip()
        
        # Check if the item exists in the dictionary using the 'in' keyword
        if item_to_check in inventory:
            print(f"Stock for {item_to_check}: {inventory[item_to_check]}")
        else:
            print(f"Error: '{item_to_check}' is not found in inventory.")

    # 4. Add Stock Logic (Updating dictionary value)
    elif command == 'add':
        item_to_add = input("Enter the item name to add stock to: ").strip()
        
        if item_to_add in inventory:
            try:
                # Ask for quantity and convert it to an integer
                quantity_input = input(f"How many units of {item_to_add} are you adding? ")
                quantity = int(quantity_input)
                
                # Update the stock value
                inventory[item_to_add] += quantity
                print(f"Successfully added {quantity} units to {item_to_add}. New stock: {inventory[item_to_add]}")
            except ValueError:
                print("Error: Quantity must be a whole number (integer).")
        else:
            print(f"Error: '{item_to_add}' is not found in inventory. Cannot add stock.")

    # 5. Invalid Command Logic
    else:
        print("Invalid command. Please enter 'list', 'check', 'add', or 'exit'.")