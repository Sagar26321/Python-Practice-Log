# -------------------- THE ADVENTURE GAME --------------------


def start_room():
    print("\n" + "="*30)
    print("      🏰 THE TOWER LOBBY 🏰")
    print("="*30)
    print("You see a 🟡 GOLD door and a ⚪ SILVER door.")
    choice = input("Which door do you choose? (Gold/Silver): ").lower()
    
    if choice == "gold":
        return "treasure"
    elif choice == "silver":
        return "dragon"
    else:
        print("\n👀 You wandered in circles and stayed in the lobby.")
        return "start"

current_room = "start"

while True:
    if current_room == "start":
        current_room = start_room()
    
    elif current_room == "treasure":
        print("\n✨💰 VICTORY! 💰✨")
        print("The gold door led to a room full of jewels!")
        print("🏆 GAME OVER - YOU ARE RICH!")
        break
        
    elif current_room == "dragon":
        print("\n🔥🐲 OH NO! 🐲🔥")
        print("The silver door led to a dragon's den!")
        print("💀 GAME OVER - YOU WERE TOASTED!")
        break