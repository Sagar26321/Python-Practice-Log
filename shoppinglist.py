budget = float(input("What is your total budget for today? "))
total_spent = 0
item_list = []


while True:
    item = input("What's the name of the item? (or type 'done' to finish): ")
    
    if item.lower() == 'done':
       break
    price = float(input(f"What is the price of {item}? "))
    total_spent =( total_spent + price)
    item_list.append(item)

    if total_spent > budget:
        diff = total_spent - budget
        print(f" ALERT! You are over budget by {diff}!")
        choice = input("Would you like to remove this item? (yes/no): ")

        if choice.lower() == 'yes':
            total_spent = total_spent - price  
            item_list.pop()                    
            print("Item removed successfully.")
            print(f"Balance remaining: {round(budget - total_spent, 2)}")
        else:
            print(f"Item kept. Current total: {round(total_spent, 2)}")
    else:
        remaining = budget - total_spent
        print(f"Balance remaining: {round(remaining, 2)}")

print("\n--- Final Receipt ---")
print(f"Items bought: {', '.join(item_list)}")
print(f"Final Total: {round(total_spent, 2)}")
