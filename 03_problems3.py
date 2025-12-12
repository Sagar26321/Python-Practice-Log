# # # todo = ["Sleep", "Work", "Gym"]
# # # todo.append("Read")
# # # todo.remove("Sleep")
# # # todo[1] = "Tired"
# # # print(todo)


# # guests = ["sagar", "tom", "alice"]
# # if "sagar".lower() in guests:
# #     print("Welcome!")
# # else:
# #     print("Not on the list")



# # numbers = [5, 1, 9, 3]
# # numbers.sort()
# # print(numbers [-1])


# # If the score is less than 50, add 5 bonus points to it.

# # Print the new score.

# profile = {"name": "Sagar", "score": 10}
# if profile["score"] < 50:
#     profile["score"] += 5
# print("The new score is:", profile["score"])


# student = {
#     "name": "Sagar",
#     "marks": [85, 92, 78]  # A list inside a dictionary!
# }

# student["marks"][1] = 95 # Update the second mark to 95
# student["marks"].append(88) # Add a new mark of 88
# print("Updated marks:", student["marks"])


password = " Admin123 "
clean_pass = password.replace(" ", "")
if clean_pass == "Admin123":
    print("Access Granted")
else:
    print("Access Denied")
