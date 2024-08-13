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
python milestone_5.py

# File structure of the project

imports
### class definition
class Hangman:
    ## Class initializations 
    def __init__(self, word_list, num_lives):

        ## function definition
    def check_guess(self, guess):

        ## function definition
    def ask_for_input(self):
        self.check_guess(guess)

### Main function definition
def play_game(word_list):
    game=Hangman(word_list, num_lives)
    game.ask_for_input()
### Main function call
if __name__ == '__main__':
    play_game(word_list)

# License information
MIT License

Copyright (c) [2024] [Shibu Abraham]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
