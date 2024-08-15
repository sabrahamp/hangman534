# About Hangman project
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Installation instructions
    Please make sure Python is installed
    Please use below command to clone the environment:
    git clone https://github.com/sabrahamp/hangman534.git

# Usage instructions
python milestone_2.py
python milestone_4.py
### Main version of the Hangman game
python milestone_5.py

# File structure of the project

imports
## Class Definition
class Hangman:
   ### Class initializations 
    def __init__(self, word_list, num_lives):

   ### function definition
    def check_guess(self, guess):

   ### function definition
    def ask_for_input(self):
        self.check_guess(guess)

## Main function definition
def play_game(word_list):
    game=Hangman(word_list, num_lives)
    game.ask_for_input()
## Main function call
if __name__ == '__main__':
    play_game(word_list)

# License information
License file can be found in this folder of repository.
