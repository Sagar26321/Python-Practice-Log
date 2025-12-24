user = input("Enter your name: ")
print(f"Hello, {user}!")
'''
1 for Snake
-1 for Water
0 for Gun

'''
import random
print("Welcome to Snake, Water, Gun Game!")

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice (s for Snake, w for Water, g for Gun): ")
youDict = {'s': 1, 'w': -1, 'g': 0}
reverseDict = {1: 'Snake', -1: 'Water', 0: 'Gun'}


you = youDict[youstr]

print(f"You chose: {reverseDict[you]}\nComputer chose: {reverseDict[computer]}")

if (computer == you):
        print("It's a Tie!")

else:
        if (computer == -1 and you == 1):
            print("You Win! Snake drinks Water.")
        elif (computer == -1 and you == 0):
            print("You Lose! Water extinguishes Gun.")
        elif (computer == 1 and you == -1):
            print("You Lose! Snake drinks Water.")
        elif (computer == 1 and you == 0):
            print("You Win! Gun kills Snake.")
        elif (computer == 0 and you == -1):
            print("You Win! Water extinguishes Gun.")
        elif (computer == 0 and you == 1):
            print("You Lose! Gun kills Snake.")
            
        else:
           print("Invalid input! Please enter 's', 'w', or 'g'.")