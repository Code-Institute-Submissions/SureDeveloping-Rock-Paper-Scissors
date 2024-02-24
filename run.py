# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from art import *
import os
import random

tprint("Rock-Paper-Scissors",font="clb6x10",chr_ignore=True,)
tprint("---Extended---",font="hyper",chr_ignore=True)

print('Welcome to Rock-Paper-Scissors Extended!\n')

user_name = input("Please enter your Name:")
# The strip() method ensures that something has to be entered and the isalpha() method ensures that no numbers are entered 
while not user_name.strip() or not user_name.isalpha():
    print("The text field must not be left blank and only letters are permitted!")
    user_name = input("Please enter your Name:")
print()
print(f"{user_name} nice to have you here. This is an extension of the classic game Rock-Paper-Scissors.\n"
"Compete against the computer and test your luck!\n"
)

menu_selection = input(f"{user_name}, to start the game and play press P.\n"
"To read the rules, press R. \n"
"If you want to quit the game press Q\n").upper()

def main_menu(menu_selection):
    """ 
    The function provides the selection in the main menu. 
    The valid data input is checked and the game is started, 
    terminated or the rules are displayed according to the user input. 
    Before the input is called up, the previous entries in the console are deleted 
    """
    os.system('clear')
    if menu_selection == 'R':
        print("This version of Rock-Paper-Scissors has been made famous by the TV series 'The Big Bang Theory'.\n"
            "The two additional elements make it less likely that players will choose the same thing, \n"
            "and providing more variety and excitement.\n"
            "Rock-Paper-Scissors-Lizard-Spock is a game based on luck. Choose an item Rock, Paper, Scissors, Lizard or Spock.\n"
            "The computer also makes a random choice. Afterwards it is checked who has won.\n" 
            "This is displayed and the scrore is counted up. After 10 games you can enter your score in the high score list.\n"
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
            "Rock crushes Scissors\n"
            "Spock vaporizes Rock\n"
            "Lizard poisons Paper\n"
        )

    elif menu_selection == 'Q':
        print(f"Thank you {user_name} for playing Rock-Paper-Scissors Extended!\n"
        "I look forward to your next game!\n")

    elif  menu_selection == 'P':
        print('P selected')
        
    else:
        input("Please select P, R or Q. All other entries are not permitted: ").upper()

main_menu(menu_selection)
