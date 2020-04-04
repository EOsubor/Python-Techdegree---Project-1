import sys
import random
import time
import os

high_score = []

def clear_screen():
    # Delay code execution.
    time.sleep(1.5)
    # Clear screen on all operating systems.
    os.system("cls" if os.name == "nt" else "clear")


def replay_game(count):
    high_score.append(count)
    high_score.sort()
    while True:
        answer = input('Would you like to play again? [Y]es / [N]o \n')
        if answer.upper() == 'Y':
            print(f'\nIt took {count} attempts to guess the answer!')
            print(f'\nThe highscore to beat is {high_score[0]}!')
            player_number()
        elif answer.upper() == 'N':
            print(f'\nYou have a final highscore of {high_score[0]}!')
            print(f'\nIt took {count} attempts to guess the answer!')
            if len(high_score) > 1:
                view_scores = input('Would you like to view your previous scores? [Y]es / [N]o \n')
                if view_scores == 'Y':
                    for i, score in enumerate(high_score, 1):
                        print('Game ', i, '. ', score)
            sys.exit('\nThanks for playing! Come back soon!')
        else:
            print("\nInvalid response. Please enter 'Y' or 'N'.")
            continue


def player_number():
    count = 1
    bottom_range = 1
    top_range = 25
    computer_choice = random.randint(bottom_range, top_range)
    while True:
        player_choice = input('\nPlease enter a number 1 and 25\n')
        try:
            player_choice = int(player_choice)
            if (player_choice < bottom_range) or (player_choice > top_range):
                raise ValueError('The number you entered was out of bounds.')
        except ValueError as err:
            print('Invalid entry. Please try again.')
            print(f'{err}')
            continue
        else:
            if player_choice == computer_choice:
                print('\nCongrats.')
                replay_game(count)
                #break
            elif player_choice > computer_choice:
                print("You're higher\n")
                count += 1
                continue
            else:
                print("You're lower\n")
                count += 1
                continue


def initialize_game():
    #import pdb; pdb.set_trace()
    high_score.clear()
    clear_screen()
    quit = 'q'
    print('----------> ' + 'Welcome to The Guessing Game' + ' <----------')

    while True:
        start_game = input("\n      Press ENTER to continue or 'q' to QUIT\n")
        if start_game.strip() == '':
            player_number()
        elif start_game.lower() == quit:
            sys.exit('\nThanks for playing! Come back soon!')
        else:
            print("\nInvalid response. Please press ENTER to play or 'q' to QUIT.")
            continue

    #print('You made it. #checkyouout')


# Prevent automatic script run on import.
if __name__ == '__main__':
  initialize_game()
