#  ATM Simulation
balance = 10000.00
transactions = []

def deposit(current_balance, amount):
    new_balance = current_balance + amount
    return new_balance

def withdraw(current_balance, amount):
    if amount > current_balance:
        print("Insufficient Balance!!")
        return current_balance
    else:
        return current_balance - amount
    
while True:
        print("\n--- ATM MENU----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")    
        print("4. Exit")
        print("5. View Transactions History")
        choice = input("Enter your choice (1-5): ")
        if choice == '1':
            print(f"Your current balance is: ${balance}")
        elif choice == '2':
            dep_amount = float(input("Enter amount to deposit: $"))
            balance = deposit(balance, dep_amount)
            print(f"deposited ${dep_amount}. New balance is: ${balance}")

        elif choice == '3':
            with_amount = float(input("Enter amount to withdraw: $"))
            old_balance = balance
            balance = withdraw(balance, with_amount)
            if balance < old_balance:
                print(f"Withdrew ${with_amount}. New balance is: ${balance}")
            transactions.append(f"Withdraw: ${with_amount}")
        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break   
        elif choice == '5':
            print("\n--- Transactions History ---")
            for transaction in transactions:
                print(transaction)
        else:
            print("Invalid choice. Please select a valid option.")
            transactions.append((choice, balance))
            