from colorama import Fore, Back
from art import *
import os
import random
import time


# ASCII font on the start screen
tprint(" Rock-Paper-Scissors", font="shimrod", chr_ignore=True,)
tprint("  --Extended--", font="utopiab", chr_ignore=True)

print('Welcome to Rock-Paper-Scissors Extended!\n')

user_name = input("Please enter your Name:\n")
# The strip() method ensures that something has to be entered and
# the isalpha() method ensures that only letters can be entered
while not user_name.strip() or not user_name.isalpha():
    user_name = input("The input field must not be left blank.\n"
                      "The user name must not contain any spaces, "
                      "only letters are permitted!\n"
                      "Please enter your Name:\n")
print()
print(f"{Fore.YELLOW}{user_name}{Fore.RESET} nice to have you here.\n"
      "This is an extension of the classic game Rock-Paper-Scissors.\n"
      "Compete against the computer and test your luck!\n")

# Input from user what should happen next
menu_selection = input(f"{Fore.YELLOW}{user_name}{Fore.RESET}, "
                       f"to start the game and play press "
                       f"{Back.MAGENTA} P {Back.RESET}.\n"
                       f"To read the rules, press "
                       f"{Back.MAGENTA } R {Back.RESET}.\n"
                       f"If you want to quit the game press "
                       f"{Back.MAGENTA} Q {Back.RESET}.\n").upper()

# Global variables that are counted and printed during the program
won_games = 0
lost_games = 0
played_games = 0
drawn_games = 0


def start_game():
    """
    The start_game function starts the game.
    It contains the computer_choice function and
    the player_choice function and the find_winner function.
    The next question is asked until the player cancels by pressing quit.
    """
    options_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    def computer_choice():
        """
        The random selection of the computer is made here .
        """
        computer_choice = random.choice(options_list)
        print(Fore.BLUE + "Computer choose: " + computer_choice+Fore.RESET)
        return computer_choice

    def player_choice(user_name):
        """
        Here the player makes his selection.
        It is also ensured that non-validated entries are
        taken into account and handled.
        """
        player_choice_num = None
        while True:
            player_choice_num = input(f"{Fore.YELLOW}{user_name}"
                                      f"{Fore.RESET}, "
                                      "please choose:\n"
                                      f"{Back.MAGENTA} 1)"
                                      f"{Back.RESET} for Rock\n"
                                      f"{Back.MAGENTA} 2)"
                                      f"{Back.RESET} for Paper\n"
                                      f"{Back.MAGENTA} 3)"
                                      f"{Back.RESET} for Scissors\n"
                                      f"{Back.MAGENTA} 4)"
                                      f"{Back.RESET} for Lizard\n"
                                      f"{Back.MAGENTA} 5)"
                                      f"{Back.RESET} for Spock\n"
                                      "Your selection: ")

            print()
            if not (" " in player_choice_num or not
                    player_choice_num.isdigit()):
                player_choice_num = int(player_choice_num) - 1

                if player_choice_num in range(5):
                    player_choice = options_list[player_choice_num]
                    print(Fore.YELLOW + "You choose: "
                          + player_choice + Fore.RESET)
                    return player_choice

            print("Invalid input. Please enter only one number "
                  "between 1 and 5.\n"
                  "No other characters are valid.")

        player_choice = options_list[player_choice_num]
        print(Fore.YELLOW + "You choose: " + player_choice + Fore.RESET)
        return player_choice

    def find_winner(computer_choice, player_choice):
        """
        The computer's choice and the player's choice are compared and
        it is decided who has won.
        It shows who has won and why. How many rounds the player has played
        The number of games won, lost or drawn is saved in global variables.
        """
        global won_games
        global lost_games
        global played_games
        global drawn_games
        if player_choice == computer_choice:
            print("Draw! You have chosen the same item.")
            drawn_games += 1
            played_games += 1
        elif player_choice == "Rock" and computer_choice == "Paper":
            print(Back.RED + "You loose: Paper covers Rock" + Back.RESET)
            lost_games += 1
            played_games += 1
        elif player_choice == "Rock" and computer_choice == "Scissors":
            print(Back.GREEN + "You win: Rock crushes Scissors" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Rock" and computer_choice == "Lizard":
            print(Back.GREEN + "You win: Rock crushes Lizard" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Rock" and computer_choice == "Spock":
            print(Back.RED + "You loose: Spock vaporizes Rock" + Back.RESET)
            lost_games += 1
            played_games += 1
        elif player_choice == "Paper" and computer_choice == "Rock":
            print(Back.GREEN + "You win: Paper covers Rock" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Paper" and computer_choice == "Scissors":
            print(Back.RED + "You loose: Scissors cuts Paper" + Back.RESET)
            lost_games += 1
            played_games += 1
        elif player_choice == "Paper" and computer_choice == "Lizard":
            print(Back.RED + "You loose: Lizard eats Paper" + Back.RESET)
            lost_games += 1
            played_games += 1
        elif player_choice == "Paper" and computer_choice == "Spock":
            print(Back.GREEN + "You win: Paper disproves Spock" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Scissors" and computer_choice == "Rock":
            print(Back.RED + "You loose: Rock crushes Scissors" + Back.RESET)
            lost_games += 1
            played_games += 1
        elif player_choice == "Scissors" and computer_choice == "Paper":
            print(Back.GREEN + "You win: Scissors cuts Paper" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Scissors" and computer_choice == "Lizard":
            print(Back.GREEN + "You win: Scissors "
                  "decapitates Lizard" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Scissors" and computer_choice == "Spock":
            print(Back.RED + "You loose: Spock smashes Scissors" + Back.RESET)
            lost_games += 1
            played_games += 1
        elif player_choice == "Lizard" and computer_choice == "Rock":
            print(Back.RED + "You loose: Rock crushes Lizard" + Back.RESET)
            lost_games += 1
            played_games += 1
        elif player_choice == "Lizard" and computer_choice == "Paper":
            print(Back.GREEN + "You win: Lizard eats Paper" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Lizard" and computer_choice == "Scissors":
            print(Back.RED + "You loose: Scissors decapitates "
                  "Lizard" + Back.RESET)
            lost_games += 1
            played_games += 1
        elif player_choice == "Lizard" and computer_choice == "Spock":
            print(Back.GREEN + "You win: Lizard poisons Spock" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Spock" and computer_choice == "Rock":
            print(Back.GREEN + "You win: Spock vaporizes Rock" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Spock" and computer_choice == "Paper":
            print(Back.RED + "You loose: Paper disproves Spock" + Back.RESET)
            lost_games += 1
            played_games += 1
        elif player_choice == "Spock" and computer_choice == "Scissors":
            print(Back.GREEN + "You win: Spock smashes Scissors" + Back.RESET)
            won_games += 1
            played_games += 1
        elif player_choice == "Spock" and computer_choice == "Lizard":
            print(Back.RED + "You loose: Lizard poisons Spock" + Back.RESET)
            lost_games += 1
            played_games += 1

    os.system('clear')
    player_choice_result = player_choice(user_name)
    computer_choice_result = computer_choice()
    find_winner(computer_choice_result, player_choice_result)
    game_end(won_games, lost_games, played_games, drawn_games)


def game_end(won_games, lost_games, played_games, drawn_games):
    """
    After each game the player is asked whether he wants to stop or
    play again. It also ensures that no invalid entries can be made.
    The global variables are printed here.
    """
    print()
    print(f"{Fore.GREEN}Won games: {won_games}{Fore.RESET}\n"
          f"{Fore.RED}Lost games: {lost_games}{Fore.RESET}\n"
          f"{Fore.BLUE}Played games: {played_games}{Fore.RESET}\n"
          f"{Fore.CYAN}Drawn games: {drawn_games}{Fore.RESET}")
    print()

    play_again = input(f"Do you want to play again press "
                       f"{Back.MAGENTA} P {Back.RESET}.\n"
                       f"If you want to stop, press "
                       f"{Back.MAGENTA} Q {Back.RESET}.\n").upper()

    while True:
        if play_again == 'P':
            start_game()
            break

        elif play_again == 'Q':
            os.system('clear')
            print(f"Thank you {Fore.YELLOW}{user_name}"
                  f"{Fore.RESET} for playing "
                  "Rock-Paper-Scissors Extended!\n"
                  "I look forward to your next game!\n")
            break

        else:
            play_again = input(f"Please select {Back.MAGENTA}"
                               f" P to play, or Q to quit {Back.RESET}. \n"
                               "All other entries are not "
                               "permitted: \n").upper()


def main_menu(menu_selection, user_name):
    """
    The function provides the selection in the main menu.
    The valid data input is checked and the game is started,
    terminated or the rules are displayed
    according to the user input.
    Before the input is called up, the previous
    entries in the console are cleared.
    Included options for the user are:
    display rules, play game or quit game.
    """
    os.system('clear')
    # Make sure the rules are only printed ones
    rules_displayed = False
    while True:
        if menu_selection == 'R' and not rules_displayed:
            os.system('clear')
            rules = ("This version of Rock-Paper-Scissors "
                     "has been made famous by the TV series\n"
                     "'The Big Bang Theory'. "
                     "The two additional elements make it less "
                     "likely that \n"
                     "players will choose the same thing and "
                     "providing more variety and excitement.\n"
                     "Rock-Paper-Scissors-Lizard-Spock is a "
                     "game based on luck. Choose an item Rock, \n"
                     "Paper, Scissors, Lizard or Spock. "
                     "The computer also makes a random choice.\n"
                     "Afterwards it is checked who has won. "
                     "This is displayed and the scrore is\n"
                     "counted up."
                     "\n"
                     "Here is a list of which item "
                     "wins against which other item:\n"
                     "Scissors cuts Paper\n"
                     "Paper covers Rock\n"
                     "Rock crushes Lizard\n"
                     "Lizard poisons Spock\n"
                     "Spock smashes Scissors\n"
                     "Scissors decapitates Lizard\n"
                     "Lizard eats Paper\n"
                     "Paper disproves Spock\n"
                     "Spock vaporizes Rock\n"
                     "Rock crushes Scissors\n")

            # Prints the rules slower
            for char in rules:
                print(char, end='', flush=True)
                time.sleep(0.02)

            print()
            menu_selection = input("If you want to start the game, press "
                                   f"{Back.MAGENTA} P {Back.RESET}.\n"
                                   "If you do not want to Quit press "
                                   f"{Back.MAGENTA} Q {Back.RESET}.\n"
                                   "All other entries are not "
                                   "permitted. \n").upper()

            rules_displayed = True

        elif menu_selection == 'Q':
            os.system('clear')
            print(f"Thank you {Fore.YELLOW}{user_name}"
                  f"{Fore.RESET} for playing "
                  "Rock-Paper-Scissors Extended!\n"
                  "I look forward to your next game!\n")
            break

        elif menu_selection == 'P':
            start_game()
            break

        else:
            # Ensures that the rules can no longer be choosen
            # when already displayed
            if rules_displayed:
                os.system('clear')
                menu_selection = input(f"Please select {Back.MAGENTA} "
                                       f"P to play or Q to quit "
                                       f"{Back.RESET}. \n"
                                       "All other entries are not "
                                       "permitted: \n").upper()
            else:
                menu_selection = input(f"Please select {Back.MAGENTA} "
                                       f"P to play, R for rules or Q to quit "
                                       f"{Back.RESET}. \n"
                                       "All other entries are not "
                                       "permitted: \n").upper()


main_menu(menu_selection, user_name)
