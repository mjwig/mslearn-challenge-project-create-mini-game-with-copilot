import random

CHOICES = ["rock", "paper", "scissors"]
WIN_RULES = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}


def get_player_choice():
    while True:
        choice = input("Choose rock, paper, scissors, or quit: ").strip().lower()
        if choice in CHOICES:
            return choice
        if choice in {"quit", "q", "exit"}:
            return None
        print("Invalid option. Please enter rock, paper, scissors, or quit.")


def get_computer_choice():
    return random.choice(CHOICES)


def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    if WIN_RULES[player_choice] == computer_choice:
        return "player"
    return "computer"


def ask_play_again():
    while True:
        answer = input("Play again? (y/n): ").strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no"}:
            return False
        print("Invalid answer. Please enter y or n.")


def main():
    print("Welcome to Rock, Paper, Scissors!")
    print("You will play against the computer opponent.")
    scores = {"player": 0, "computer": 0, "ties": 0}

    while True:
        player_choice = get_player_choice()
        if player_choice is None:
            print("\nYou chose to quit the game.")
            break

        computer_choice = get_computer_choice()

        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(player_choice, computer_choice)

        if result == "player":
            print("You win this round!")
            scores["player"] += 1
        elif result == "computer":
            print("You lose this round.")
            scores["computer"] += 1
        else:
            print("This round is a tie.")
            scores["ties"] += 1

        if not ask_play_again():
            break
        print()

    print("\nGame over!")
    print(f"Your score: {scores['player']}")
    print(f"Computer score: {scores['computer']}")
    print(f"Ties: {scores['ties']}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main()
