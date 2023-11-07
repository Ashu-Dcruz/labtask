import random

def get_user_choice():
    print("Enter  choice: Rock, Paper or Scissors")
    return input().lower()

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def check_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = check_winner(user_choice, computer_choice)
    print(result)

if __name__ == "__main__":
    main()

