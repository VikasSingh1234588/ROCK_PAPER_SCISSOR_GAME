import random

def get_user_choice():
    '''Get user input for rock, paper, or scissors.'''
    while True:
        user_action = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_action in ["rock", "paper", "scissors"]:
            return user_action
        else:
            print("Invalid choice. Please enter 'rock', 'paper', or 'scissors'.")

def get_computer_choice():
    '''Generate a random choice for the computer.'''
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    '''Determine the winner based on user and computer choices.'''
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or (user == "paper" and computer == "rock") or (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    '''Play a single game of Rock-Paper-Scissors.'''
    user_choice=get_user_choice()
    computer_choice=get_computer_choice()
    print(f"Computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))

# Play the game
play_game()