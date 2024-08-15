# About Hangman Project
Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is an implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

# Installation Instructions
    Please make sure Python is installed
    Please use below command to clone the environment:
    git clone https://github.com/sabrahamp/hangman534.git

# Usage Instructions
python milestone_2.py
python milestone_4.py
### Main Version Of The Hangman Game
python milestone_5.py

# File Structure Of The Project

imports
## Class Definition
class Hangman:
   ### Class Initializations 
    def __init__(self, word_list, num_lives):

   ### Function Definition
    def check_guess(self, guess):

   ### Function Definition
    def ask_for_input(self):
   ### Function Call Within The Class
        self.check_guess(guess)

## Main Function Definition
def play_game(word_list):
   ### Object creation
    game=Hangman(word_list, num_lives)
   ### Function Call In The Object
    game.ask_for_input()
## Main Function Call
if __name__ == '__main__':
    play_game(word_list)

# License Information
License file can be found in this folder of repository.
