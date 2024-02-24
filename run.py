# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

from art import *

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

