import random
import string
import time

def generate_password(length, use_digits, use_special):
    # Start with uppercase and lowercase letters
    characters = string.ascii_letters

    # Add numbers if the user wants them
    if use_digits:
        characters += string.digits

    # Add special characters if selected
    if use_special:
        characters += string.punctuation

    # Build the password one character at a time
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        # Display the program title
        print("\n" + "═"*45)
        print("   🔐  SECURE PASSWORD GENERATOR ULTRA  🔐")
        print("═"*45)

        # Ask the user for the password length
        try:
            length = int(input("📏 Enter the desired password length (Min: 6): "))

            # Make sure the password is at least 6 characters long
            if length < 6:
                print("\n⚠️ Password length should be at least 6 characters.")
                length = 6
                print("👉 Length set to 6.")
        except ValueError:
            print("\n❌ Please enter a valid number.")
            print("═"*45)
            continue

        # Ask which character types to include
        print("\n🛠️ Configure Complexity Settings:")
        include_digits = input("👉 Include numbers? (0-9) (y/n): ").strip().lower() == 'y'
        include_special = input("👉 Include special symbols? (!@#$) (y/n): ").strip().lower() == 'y'

        # Short loading effect
        print("\n🔑 Generating password...")
        time.sleep(0.7)
        print("─" * 45)

        # Generate the password
        secure_password = generate_password(length, include_digits, include_special)

        # Show the generated password
        print("✨ Your generated password:")
        print(f"👉 \033[1;32m{secure_password}\033[0m")
        print("─" * 45)

        # Give a basic strength rating
        if length >= 12 and include_digits and include_special:
            print("💪 PASSWORD STRENGTH: 🟢 EXCELLENT")
        elif length >= 8 and (include_digits or include_special):
            print("📈 PASSWORD STRENGTH: 🟡 GOOD")
        else:
            print("⚠️ PASSWORD STRENGTH: 🔴 WEAK")

        print("═"*45)

        # Ask if the user wants to generate another password
        repeat = input("\n🔄 Generate another password? (yes/no): ").strip().lower()

        if repeat not in ('yes', 'y'):
            print("\n👋 Thanks for using the Password Generator. Goodbye!\n")
            break

if __name__ == "__main__":
    main()
