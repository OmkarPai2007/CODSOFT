import random
import time

def get_computer_choice():
    # Pick a random option for the computer
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user, computer):
    # Check who wins the round
    if user == computer:
        return "tie"

    # Winning combinations for the player
    if (user == 'rock' and computer == 'scissors') or \
       (user == 'scissors' and computer == 'paper') or \
       (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def display_scoreboard(user_score, computer_score, ties):
    # Show the current scores
    print("\n" + "📊 " + "─"*13 + " SCOREBOARD " + "─"*13 + " 📊")
    print(f"🏆  You: {user_score}   |   🤖  Computer: {computer_score}   |   🤝  Ties: {ties}")
    print("═"*42)

def main():
    # Starting scores
    user_score = 0
    computer_score = 0
    ties = 0

    print("="*42)
    print("🎮  WELCOME TO THE ARCADE: ROCK-PAPER-SCISSORS  🎮")
    print("="*42)

    while True:
        # Ask the player for a choice
        print("\nChoose your weapon:")
        print("🪨  [r] Rock")
        print("📄  [p] Paper")
        print("✂️  [s] Scissors")
        print("-" * 42)

        user_input = input("👉 Your choice (r/p/s): ").strip().lower()

        # Allow both short and full-word inputs
        input_mapping = {
            'r': 'rock',
            'p': 'paper',
            's': 'scissors',
            'rock': 'rock',
            'paper': 'paper',
            'scissors': 'scissors'
        }

        if user_input not in input_mapping:
            print("\n❌ Invalid choice! Please enter 'r', 'p', or 's'.")
            continue

        user_choice = input_mapping[user_input]
        computer_choice = get_computer_choice()

        # Add a little suspense before showing the result
        print("\n🪨  ROCK...")
        time.sleep(0.4)
        print("📄  PAPER...")
        time.sleep(0.4)
        print("✂️  SCISSORS... SHOOT!")
        time.sleep(0.3)
        print("-" * 42)

        # Show both choices
        print(f"🧑 You chose: {user_choice.capitalize()}")
        print(f"🤖 Computer chose: {computer_choice.capitalize()}")
        print("-" * 42)

        # Decide the winner
        result = determine_winner(user_choice, computer_choice)

        # Update scores and show the outcome
        if result == "tie":
            print("🤝 IT'S A TIE ROUND!")
            ties += 1
        elif result == "user":
            print("🎉 YOU WIN THIS ROUND!")
            user_score += 1
        else:
            print("💀 COMPUTER WINS THIS ROUND!")
            computer_score += 1

        # Display updated scores
        display_scoreboard(user_score, computer_score, ties)

        # Ask if the player wants another round
        play_again = input("🔄 Do you want to play another round? (y/n): ").strip().lower()

        if play_again not in ('y', 'yes'):
            print("\n" + "="*42)
            print("🏁 FINAL RESULTS 🏁")
            display_scoreboard(user_score, computer_score, ties)

            # Show the overall winner
            if user_score > computer_score:
                print("🏆 Congratulations! You won the game! 🏆\n")
            elif user_score < computer_score:
                print("🤖 The computer wins this time. Better luck next game!\n")
            else:
                print("🤝 The game ends in a draw!\n")
            break

if __name__ == "__main__":
    main()
