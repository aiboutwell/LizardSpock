# Author: Amanda Boutwell
#
# This program will create the game of Rock Paper Lizard Spock
# Rules:
# Scissors cuts Paper
# Paper covers Rock
# Rock crushes Lizard
# Lizard poisons Spock
# Spock smashes Scissors
# Scissors decapitates Lizard
# Lizard eats Paper
# Paper disproves Spock
# Spock vaporizes Rock
# (and as it always has) Rock crushes Scissors
#
# Import random number function to generate a random number.
import random
# Import os to clear the screen
import os

optionslist = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

def random_guess():
    # Let the computer chose a random number to select the computer's guess
    x = random.randint(0,4)
    return optionslist[x]

def user_input():
    # Ask the user for a guess.  Invalid input will display an error and ask for another guess.
    # If the user has already had 5 guesses excluding ties then no more questions.
    x=9
    while(x < 0 or x >4):
        try:
            x = int(input("\n (0)Rock, (1)Paper, (2)Sissors, (3)Liszard, (4)Spock: "))
        except ValueError:
            pass
        if x < 0 or x > 4:
            print("\n ERROR: Your choice was invalid.  Please try again.\n")
    return optionslist[x]

def compare_guess(user_guess,computer_guess,user_score,computer_score,tie_score):
    # Based on the number chosen by the user, compare the guess to the option randomly chosen by the computer
    if user_guess == computer_guess:
        print(f"Tie: You both chose {computer_guess}.")
        tie_score += 1
    elif user_guess == "Scissors" and computer_guess == "Paper":
        print(f"You win: Scissors cuts Paper.")
        user_score += 1
    elif user_guess == "Paper" and computer_guess == "Rock":
        print(f"You win: Paper covers Rock.")
        user_score += 1
    elif user_guess == "Rock" and computer_guess == "Lizard":
        print(f"You win: Rock crushes Lizard")
        user_score += 1
    elif user_guess == "Rock" and computer_guess == "Scissors":
        print(f"You win: Rock crushes Scissors")
        user_score += 1
    elif user_guess == "Lizard" and computer_guess == "Spock":
        print(f"You win: Lizard poisons Spock")
        user_score += 1
    elif user_guess == "Spock" and computer_guess == "Scissors":
        print(f"You win: Spock smashes Scissors")
        user_score += 1
    elif user_guess == "Scissors" and computer_guess == "Lizard":
        print(f"You win: Scissors decapitates Lizard")
        user_score += 1
    elif user_guess == "Lizard" and computer_guess == "Paper":
        print(f"You win: Lizard eats Paper")
        user_score += 1
    elif user_guess == "Paper" and computer_guess == "Spock":
        print(f"You win: Paper disproves Spock")
        user_score += 1
    elif user_guess == "Spock" and computer_guess == "Rock":
        print(f"You win: Spock vaporizes Rock")
        user_score += 1
    elif computer_guess == "Scissors" and user_guess == "Paper":
        print(f"You lose: Scissors cuts Paper.")
        computer_score += 1
    elif computer_guess == "Paper" and user_guess == "Rock":
        print(f"You lose: Paper covers Rock.")
        computer_score += 1
    elif computer_guess == "Rock" and user_guess == "Lizard":
        print(f"You lose: Rock crushes Lizard")
        computer_score += 1
    elif computer_guess == "Rock" and user_guess == "Scissors":
        print(f"You lose: Rock crushes Scissors")
        computer_score += 1
    elif computer_guess == "Lizard" and user_guess == "Spock":
        print(f"You lose: Lizard poisons Spock")
        computer_score += 1
    elif computer_guess == "Spock" and user_guess == "Scissors":
        print(f"You lose: Spock smashes Scissors")
        computer_score += 1
    elif computer_guess == "Scissors" and user_guess == "Lizard":
        print(f"You lose: Scissors decapitates Lizard")
        computer_score += 1
    elif computer_guess == "Lizard" and user_guess == "Paper":
        print(f"You lose: Lizard eats Paper")
        computer_score += 1
    elif computer_guess == "Paper" and user_guess == "Spock":
        print(f"You lose: Paper disproves Spock")
        computer_score += 1
    elif computer_guess == "Spock" and user_guess == "Rock":
        print(f"You lose: Spock vaporizes Rock")
        computer_score += 1
    else:
        # If something goes awry it will be a no win scenario
        print("ERROR: Kobayashi Maru")
    return user_score,computer_score,tie_score


def game_play():
    # Main structure of the game.
    # clear the screen and run the game
    os.system("cls")
    user_score = 0
    computer_score = 0
    tie_score = 0
    n = 0
    while (n < 5):
        computer_guess = random_guess()
        user_guess = user_input()
        user_score, computer_score, tie_score = compare_guess(user_guess, computer_guess, user_score, computer_score, tie_score)
        print(f"            YOU: {user_score}  .....  Computer: {computer_score}  .....  Tie: {tie_score}")
        n += 1
        if n == 5 and user_score == computer_score:
            n -= 1
    if user_score > computer_score:
        print("\n Congratulations!  You win.\n")
    elif computer_score > user_score:
        print("\n Sorry you lose.\n")
    else:
        # If something goes awry it will be a no win scenario
        print("ERROR: Kobayashi Maru")
		
# Give instructions and start the game.

print("\nWelcome to Rock, Paper, Scissors, Lizard, Spock.\n")
print("There are 5 rounds with additional rounds, if there is a tie.")
print("Type the number that corresponds to your choice.  Good luck. \n")

# Call game_play for the first run
game_play()
# rerun the game until the user chooses to quit.
while True:
    again = str(input("\nWould you like to play again? (Y/N): ").upper().strip())
    if again == "Y":
        game_play()
        continue
    elif again == "N":
        print("Good Bye.")
        break
    else:
        print("\nPlease enter either Y or N")
