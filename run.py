# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from art import *
import os
import random

tprint(" Rock-Paper-Scissors", font="shimrod", chr_ignore=True,)
tprint("  --Extended--", font="utopiab", chr_ignore=True)

print('Welcome to Rock-Paper-Scissors Extended!\n')

user_name = input("Please enter your Name:\n")
# The strip() method ensures that something has to be entered and the isalpha()
# method ensures that no numbers are entered
while not user_name.strip() or not user_name.isalpha():
    user_name = input("The text field must not be left blank"
                      " and only letters are permitted!\n"
                      "Please enter your Name:\n")
print()
print(f"{user_name} nice to have you here.\n"
      "This is an extension of the classic game Rock-Paper-Scissors.\n"
      "Compete against the computer and test your luck!\n")

menu_selection = input(f"{user_name}, to start the game and play press P.\n"
                       "To read the rules, press R\n"
                       "If you want to quit the game press Q.\n"
                       "Want to see the highscore list press H.\n").upper()

won_games = 0
lost_games = 0
played_games = 0
drawn_games = 0


def start_game():
    """
    The Start game function starts the game.
    It contains the computer_choice function and
    the player-choice function and the Find winner function.
    The next question is asked until the player cancels by pressing quit.
    """
    options_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

    def computer_choice():
        """
        The random selection of the computer is made here .
        """
        computer_choice = random.choice(options_list)
        print("Computer choose: " + computer_choice)
        return computer_choice

    def player_choice(user_name):
        """
        Here the player makes his selection.
        It is also ensured that non-validated entries are
        taken into account and handled.
        """
        options_list = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
        while True:
            try:
                player_choice_num = int(input(f"{user_name}, please choose:\n"
                                              "1) for Rock\n"
                                              "2) for Paper\n"
                                              "3) for Scissors\n"
                                              "4) for Lizard\n"
                                              "5) for Spock\n"
                                              "Your selection: "))-1
                print()
                if player_choice_num not in range(5):
                    print("")
                    raise ValueError("Invalid input."
                                     "Please enter a number between 1 and 5.")

                player_choice = options_list[player_choice_num]
                print("You choose: " + player_choice)
                return player_choice
            except ValueError as ve:
                print("")
                print("Invalid input. Please enter a number between 1 and 5.")

    def find_winner(computer_choice, player_choice):
        """
        The computer's choice and the player's choice are compared and
        it is decided who has won.
        If both answers are the same, the game is played again.
        """
        global won_games
        global lost_games
        global played_games
        global drawn_games
        if player_choice == computer_choice:
            print("You have chosen the same thing."
                  "The attempt will be repeated.")
            drawn_games += 1
            played_games += 1
            start_game()
        elif player_choice == "Rock" and computer_choice == "Paper":
            print("You loose: Paper covers Rock")
            lost_games += 1
            played_games += 1
        elif player_choice == "Rock" and computer_choice == "Scissors":
            print("You win: Rock crushes Scissors")
            won_games += 1
            played_games += 1
        elif player_choice == "Rock" and computer_choice == "Lizard":
            print("You win: Rock crushes Lizard")
            won_games += 1
            played_games += 1
        elif player_choice == "Rock" and computer_choice == "Spock":
            print("You loose: Spock vaporizes Rock")
            lost_games += 1
            played_games += 1
        elif player_choice == "Paper" and computer_choice == "Rock":
            print("You win: Paper covers Rock")
            won_games += 1
            played_games += 1
        elif player_choice == "Paper" and computer_choice == "Scissors":
            print("You loose: Scissors cuts Paper")
            lost_games += 1
            played_games += 1
        elif player_choice == "Paper" and computer_choice == "Lizard":
            print("You loose: Lizard eats Paper")
            lost_games += 1
            played_games += 1
        elif player_choice == "Paper" and computer_choice == "Spock":
            print("You win: Paper disproves Spock")
            won_games += 1
            played_games += 1
        elif player_choice == "Scissors" and computer_choice == "Rock":
            print("You loose: Rock crushes Scissors")
            lost_games += 1
            played_games += 1
        elif player_choice == "Scissors" and computer_choice == "Paper":
            print("You win: Scissors cuts Paper")
            won_games += 1
            played_games += 1
        elif player_choice == "Scissors" and computer_choice == "Lizard":
            print("You win: Scissors decapitates Lizard")
            won_games += 1
            played_games += 1
        elif player_choice == "Scissors" and computer_choice == "Spock":
            print("You loose: Spock smashes Scissors")
            lost_games += 1
            played_games += 1
        elif player_choice == "Lizard" and computer_choice == "Rock":
            print("You loose: Rock crushes Lizard")
            lost_games += 1
            played_games += 1
        elif player_choice == "Lizard" and computer_choice == "Paper":
            print("You win: Lizard eats Paper")
            won_games += 1
            played_games += 1
        elif player_choice == "Lizard" and computer_choice == "Scissors":
            print("You loose: Scissors decapitates Lizard")
            lost_games += 1
            played_games += 1
        elif player_choice == "Lizard" and computer_choice == "Spock":
            print("You win: Lizard poisons Spock")
            won_games += 1
            played_games += 1
        elif player_choice == "Spock" and computer_choice == "Rock":
            print("You win: Spock vaporizes Rock")
            won_games += 1
            played_games += 1
        elif player_choice == "Spock" and computer_choice == "Paper":
            print("You loose: Paper disproves Spock")
            lost_games += 1
            played_games += 1
        elif player_choice == "Spock" and computer_choice == "Scissors":
            print("You win: Spock smashes Scissors")
            won_games += 1
            played_games += 1
        elif player_choice == "Spock" and computer_choice == "Lizard":
            print("You loose: Lizard poisons Spock")
            lost_games += 1
            played_games += 1

    os.system('clear')
    player_choice_result = player_choice(user_name)
    computer_choice_result = computer_choice()
    find_winner(computer_choice_result, player_choice_result)
    game_end(won_games, lost_games, played_games, drawn_games)


def game_end(won_games, lost_games, played_games, drawn_games):
    """
    After each game the player is asked whether he wants to stop,
    play again or see the highscore list.
    It also ensures that no invalid entries can be made.
    """
    print()
    print(f"won_games: {won_games}\n"
          f"lost_games: {lost_games}\n"
          f"played_games: {played_games}\n"
          f"drawn_games: {drawn_games}")
    print()
    play_again = input("Do you want to play again press P.\n"
                       "If you want to stop, press Q.\n"
                       "Want to see the highscore list press H.\n").upper()
    if play_again == 'P':
        start_game()
    elif play_again == 'Q':
        print(f"Thank you {user_name} for playing"
              "Rock-Paper-Scissors Extended!\n"
              "I look forward to your next game!\n")
    elif play_again == 'H':
        print("selcted H")
    else:
        input("Please select P, Q or H."
              "All other entries are not permitted: \n").upper()


def main_menu(menu_selection, user_name):
    """
    The function provides the selection in the main menu.
    The valid data input is checked and the game is started,
    terminated or the rules are displayed
    according to the user input.
    Before the input is called up, the previous
    entries in the console are deleted.
    """
    os.system('clear')
    while True:
        if menu_selection == 'R':
            print("This version of Rock-Paper-Scissors has been made famous\n"
                  "by the TV series 'The Big Bang Theory'.\n"
                  "The two additional elements make it less likely that players"
                  "will choose the same thing,\n"
                  "and providing more variety and excitement.\n"
                  "Rock-Paper-Scissors-Lizard-Spock is a game based on luck."
                  "Choose an item Rock, Paper, Scissors, Lizard or Spock.\n"
                  "The computer also makes a random choice."
                  "Afterwards it is checked who has won.\n"
                  "This is displayed and the scrore is counted up."
                  "After 10 games you can enter your score in"
                  "the high score list.\n"
                  "Here is a list of which item wins against which other item.\n"
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

            menu_selection = input("If you want to start the game, press P,\n"
                                   "If you do not want to play press Q.\n"
                                   "If you do not want to play press H.\n"
                                   "All other entries are not permitted: \n").upper()
            
        elif menu_selection == 'Q':
            print(f"Thank you {user_name} for playing"
                   "Rock-Paper-Scissors Extended!\n"
                   "I look forward to your next game!\n")
            break

        elif menu_selection == 'P':
            start_game()
            break

        elif menu_selection == 'H':
            print("selcted H")
            break

        else:
            menu_selection = input("Please select P, R or Q."
                                   "All other entries are not permitted: \n").upper()


main_menu(menu_selection, user_name)
