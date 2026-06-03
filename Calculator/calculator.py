import time

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    while True:
        # Show the calculator heading
        print("\n" + "="*40)
        print("   🧮  WELCOME TO THE SMART CALCULATOR  🧮")
        print("="*40)
        
        # Get two numbers from the user
        try:
            num1 = float(input("👉 Enter the first number: "))
            num2 = float(input("👉 Enter the second number: "))
        except ValueError:
            print("\n❌ Invalid input! Please enter numerical values.")
            print("="*40)
            continue

        # Display the list of operations
        print("\n✨ Available Operations:")
        print("  [1] ➕ Addition")
        print("  [2] ➖ Subtraction")
        print("  [3] ✖️  Multiplication")
        print("  [4] ➗ Division")
        print("-" * 40)

        # Ask the user which operation to perform
        choice = input("Select an operation (1/2/3/4): ").strip()

        # Small pause before showing the result
        print("\n⚙️  Processing your calculation...")
        time.sleep(0.6) # Simulates a tiny loading delay for style

        # Calculate and display the answer
        print("-" * 40)
        if choice == '1':
            print(f"🎉 SUCCESS! Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"🎉 SUCCESS! Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"🎉 SUCCESS! Result: {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"🎉 SUCCESS! Result: {num1} / {num2} = {divide(num1, num2)}")
        else:
            print("❌ Invalid choice! Please select a number from 1 to 4.")
        print("="*40)

        # Ask if the user wants another calculation
        repeat = input("\n🔄 Do you want to perform another calculation? (yes/no): ").strip().lower()
        if repeat != 'yes' and repeat != 'y':
            print("\n👋 Thank you for using Smart Calculator! Goodbye!\n")
            break

if __name__ == "__main__":
    calculator()
