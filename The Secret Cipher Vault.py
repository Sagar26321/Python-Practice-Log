def mirror_text(original):
    return original[::-1]

while True:
    # Adding 'Decoration' lines makes the menu look like a real app
    print("\n" + "="*30)
    print("      🔐 SECRET VAULT 🔐")
    print("="*30)
    
    choice = input("[E]ncrypt | [D]ecrypt | [Q]uit\nChoice: ").upper()

    if choice == "Q":
        print("\n>>> Vault Locked. Goodbye.")
        break
    
    elif choice == "E":
        msg = input("\nEnter message: ")
        # Using symbols makes the process look 'Visual'
        print(f"🔒 Locking... \nScrambled: {mirror_text(msg)}")

    elif choice == "D":
        code = input("\nEnter code: ")
        print(f"🔓 Unlocking... \nOriginal: {mirror_text(code)}")