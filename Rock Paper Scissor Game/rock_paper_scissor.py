import random
import time

def get_computer_choice():
    # Generate a random choice for the computer
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user, computer):
    # Core game logic implementation
    if user == computer:
        return "tie"
    
    # Rock beats scissors, scissors beat paper, and paper beats rock
    if (user == 'rock' and computer == 'scissors') or \
       (user == 'scissors' and computer == 'paper') or \
       (user == 'paper' and computer == 'rock'):
        return "user"
    else:
        return "computer"

def display_scoreboard(user_score, computer_score, ties):
    # User Interface score tracking dashboard
    print("\n" + "📊 " + "─"*13 + " SCOREBOARD " + "─"*13 + " 📊")
    print(f"🏆  You: {user_score}   |   🤖  Computer: {computer_score}   |   🤝  Ties: {ties}")
    print("═"*42)

def main():
    # Initialize score variables
    user_score = 0
    computer_score = 0
    ties = 0

    print("="*42)
    print("🎮  WELCOME TO THE ARCADE: ROCK-PAPER-SCISSORS  🎮")
    print("="*42)

    while True:
        # User Input prompt
        print("\nChoose your weapon:")
        print("🪨  [r] Rock")
        print("📄  [p] Paper")
        print("✂️  [s] Scissors")
        print("-" * 42)
        
        user_input = input("👉 Your choice (r/p/s): ").strip().lower()

        # Mapping short inputs for a smoother user interface experience
        input_mapping = {'r': 'rock', 'p': 'paper', 's': 'scissors', 
                         'rock': 'rock', 'paper': 'paper', 'scissors': 'scissors'}

        if user_input not in input_mapping:
            print("\n❌ Invalid choice! Please enter 'r', 'p', or 's'.")
            continue

        user_choice = input_mapping[user_input]
        computer_choice = get_computer_choice()

        # Visual dramatic pause for the video demo
        print("\n🪨  ROCK...")
        time.sleep(0.4)
        print("📄  PAPER...")
        time.sleep(0.4)
        print("✂️  SCISSORS... SHOOT!")
        time.sleep(0.3)
        print("-" * 42)

        # Display selections
        print(f"🧑 You chose:     {user_choice.capitalize()}")
        print(f"🤖 Computer chose: {computer_choice.capitalize()}")
        print("-" * 42)

        # Evaluate the round winner
        result = determine_winner(user_choice, computer_choice)

        # Display specific outcome feedback and record scores
        if result == "tie":
            print("🤝 IT'S A TIE ROUND!")
            ties += 1
        elif result == "user":
            print("🎉 YOU WIN THIS ROUND! 🔥")
            user_score += 1
        else:
            print("💀 COMPUTER WINS THIS ROUND! 💥")
            computer_score += 1

        # Keep track of scores for multiple rounds
        display_scoreboard(user_score, computer_score, ties)

        # Play Again logic functionality
        play_again = input("🔄 Do you want to play another round? (y/n): ").strip().lower()
        if play_again != 'y' and play_again != 'yes':
            print("\n" + "="*42)
            print("🏁 FINAL TOURNAMENT RESULTS 🏁")
            display_scoreboard(user_score, computer_score, ties)
            if user_score > computer_score:
                print("🏆 CONGRATULATIONS! YOU DEFEATED THE COMPUTER! 🏆\n")
            elif user_score < computer_score:
                print("🤖 THE MACHINE OVERLORD WINS THIS TIME. BETTER LUCK NEXT TIME! 🤖\n")
            else:
                print("🤝 AN EVENLY MATCHED TOURNAMENT! IT'S A DRAW! 🤝\n")
            break

if __name__ == "__main__":
    main()