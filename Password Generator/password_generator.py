import random
import string
import time

def generate_password(length, use_digits, use_special):
    # Base character set: lower and uppercase letters
    characters = string.ascii_letters
    
    # Adding extra complexity layers based on user preference
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    # Randomly selecting characters to form the password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    while True:
        # Cyber-security themed visual banner
        print("\n" + "═"*45)
        print("   🔐  SECURE PASSWORD GENERATOR ULTRA  🔐")
        print("═"*45)

        # 1. User Input: Prompt for desired length
        try:
            length = int(input("📏 Enter the desired password length (Min: 6): "))
            if length < 6:
                print("\n⚠️  For security, length should be at least 6 characters.")
                length = 6
                print("👉 Setting length to minimum default: 6")
        except ValueError:
            print("\n❌ Invalid entry! Please enter a valid whole number.")
            print("═"*45)
            continue

        # Advanced options for complexity
        print("\n🛠️  Configure Complexity Settings:")
        include_digits = input("👉 Include numbers? (0-9) (y/n): ").strip().lower() == 'y'
        include_special = input("👉 Include special symbols? (!@#$) (y/n): ").strip().lower() == 'y'

        # Visual feedback during generation
        print("\n🔑 Generating cryptographic key matrix...")
        time.sleep(0.7)
        print("🛡️  Injecting high-entropy entropy pools...")
        time.sleep(0.5)
        print("─" * 45)

        # 2. Generate the Password
        secure_password = generate_password(length, include_digits, include_special)

        # 3. Display the Password
        print("✨ SUCCESS! YOUR SECURE PASSWORD GENERATED:")
        print(f"👉 \033[1;32m{secure_password}\033[0m") # Prints the password in bold green text
        print("─" * 45)

        # Dynamic password rating logic
        if length >= 12 and include_digits and include_special:
            print("💪 PASSWORD STRENGTH: 🟢 EXCELLENT (Military Grade)")
        elif length >= 8 and (include_digits or include_special):
            print("📈 PASSWORD STRENGTH: 🟡 GOOD (Strong Enough)")
        else:
            print("⚠️  PASSWORD STRENGTH: 🔴 WEAK (Easy to crack!)")
        
        print("═"*45)

        # Option to generate another password
        repeat = input("\n🔄 Generate another secure password? (yes/no): ").strip().lower()
        if repeat != 'yes' and repeat != 'y':
            print("\n👋 Stay secure! Closing Vault. Goodbye!\n")
            break

if __name__ == "__main__":
    main()