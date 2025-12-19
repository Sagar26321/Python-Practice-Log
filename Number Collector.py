def collect_numbers():
    my_list = []
    while True:
        data = input("Enter a number (or 'done'): ")
        if data == "done":
            break
        else:
            my_list.append(int(data))
    
    return my_list # The "Cash Slot" handing back the list

# --- CALL THE MACHINE ---
user_data = collect_numbers()

print("Your final list is:", user_data)
