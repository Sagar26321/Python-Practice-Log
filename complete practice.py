# # stats = (100, 45, 88)
# # strength = stats[0]
# # magic = stats[1]
# # print(f"mage level:magic is {magic}, strength is {strength}")


# # above is old and time consuming, the new and advanced way is below

# stats = (100, 45, 88)

# # THE MAGIC LINE (Unpacking)
# # Python automatically assigns 100->strength, 45->magic, 88->agility
# strength, magic, agility = stats 

# print(f"Mage Level: Magic is {magic}, Strength is {strength}")





# cart = ["apple", "Banana", "milk"]
# cart.append("eggs")
# cart[1] = "grapes"
# print(cart)


# contacts = {
#     "Sagar": "98756",
#     "rahul": "12345"
# }
# contacts["amit"] = "55555"
# print(contacts)


# racers = ["Max", "Lewis", "Lando", "Charles"]
# print(f"the winner is :{racers[0]} , silver medalist is:{racers[1]} ")

# dimensions = (10, 5, 2)
# l, w, h = dimensions
# volume = l* w * h
# print(f"The volume is: {volume}")



# menu = {
#     "Burger": 50,
#     "Pizza": 100,
#     "Coke": 20
# }

# total = menu["Pizza"] + menu["Coke"]
# print(f"The total bill is: {total}")



# Task:

# Retrieve the list of marks for "Sagar".

# Calculate his average score (Sum of the two marks divided by 2).

# Print exactly: "Sagar's Average: 79.5"



# students = {
#     "Rahul": [85, 92],
#     "Sagar": [78, 81]
# }
# sagar_marks = students["Sagar"]
# average_score = sum(sagar_marks) / len(sagar_marks)
# print(f"Sagar's Average: {average_score}")


# vip_ids = (101, 102, 550, 999)
# user_id = int(input("Enter your user ID: "))

# if user_id in vip_ids:
#     print("Welcome, VIP Member.")
# else:
#     print("Access Denied.")



# library = ["1984", "The Hobbit", "Harry Potter"]
# new_book = input("Enter Your book name: ")

# if new_book not in  library:
#     print("Adding book to library.")
#     library.append(new_book)
# else:
#     print("Book already exists in library.")

# print(f"Updated library: {library}")



# guests = ["Sagar", "Rahul"]
# name = input("Enter your name: ")
# if name in guests:
#     print("You are already on the guest list.")
# else:
#     guests.append(name)
#     print("Welcome to the party!")

# print(f"Updated guest list: {guests}")

# wrong code:-

# playlist = ["Song A", "Song B", "Song C"]

# print(f"Final Playlist: {playlist.remove[0]}, {playlist.append("Song D")}, {playlist.insert(0, "Song X")}")


# correct code:-

# playlist = ["Song A", "Song B", "Song C"]

# # Step 1: Remove "Song B" (Use the name, and parenthesis)
# playlist.remove("Song B")

# # Step 2: Add "Song D" to the end
# playlist.append("Song D")

# # Step 3: Insert "Song X" at Index 0 (Start)
# playlist.insert(0, "Song X")

# # Step 4: NOW print the list
# print(f"Final Playlist: {playlist}")





# portfolio = {"Apple": 10, "Tesla": 5}
# portfolio["Apple"] = 12  # Update Apple shares to 12
# portfolio["Tesla"] = 4 # Update Tesla shares to 4
# print(f"The Final Number of apple shares: {portfolio['Apple']}")



# professional way :-

portfolio = {"Apple": 10, "Tesla": 5}

# The "Long" Way
portfolio["Apple"] = portfolio["Apple"] + 2

# The "Pro" Way (Short-hand)
portfolio["Tesla"] -= 1  # Same as saying 'equals itself minus 1'

print(f"Apple Shares: {portfolio['Apple']}")