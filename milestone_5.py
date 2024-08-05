## Importing relevant packages
import random

## All initializations
# word = ''

## Class definition
class Hangman:
    '''
    A Hangman Game that asks the user for a letter and checks if it is in the word.
    It starts with a default number of lives and a random word from the word_list.


    Parameters:
    ----------
    word_list: list
        List of words to be used in the game
    num_lives: int
        Number of lives the player has

    Attributes:
    ----------
    word: str
        The word to be guessed picked randomly from the word_list
    word_guessed: list
        A list of the letters of the word, with '_' for each letter not yet guessed
        For example, if the word is 'apple', the word_guessed list would be ['_', '_', '_', '_', '_']
        If the player guesses 'a', the list would be ['a', '_', '_', '_', '_']
    num_letters: int
        The number of UNIQUE letters in the word that have not been guessed yet
    num_lives: int
        The number of lives the player has
    list_letters: list
        A list of the letters that have already been tried

    Methods:
    -------
    check_letter(letter)
        Checks if the letter is in the word.
    ask_letter()
        Asks the user for a letter.
    '''
    ## Class initializations 
    def __init__(self, word_list, num_lives):
        self.word_list=word_list
        self.num_lives=num_lives

        self.word = random.choice(self.word_list).lower()
        print(self.word)
        self.word_guessed=[]
        for i in self.word:
            self.word_guessed.append("_")
        print(self.word_guessed)
        self.num_letters=len(set(self.word))
        print("num_letters", self.num_letters)
        self.list_of_guesses=[]

    ## function definition
    def check_guess(self, guess):
        '''
        Checks if the letter is in the word.
        If it is, it replaces the '_' in the word_guessed list with the letter.
        If it is not, it reduces the number of lives by 1.

        Parameters:
        ----------
        guess: str
            The letter to be checked

        '''
        guess = guess.lower()
        found=False
        ## Specific validations of the input with the word
        for index, char in enumerate(self.word):
            if guess == char and char not in enumerate(self.word_guessed):
                self.word_guessed[index]=guess
                found=True
            elif (index) == (len(self.word)-1) and not found:
                print(f"Sorry, your letter {guess} is not found in the word")
                self.num_lives-=1
                # found=False
                print(f"Your have {self.num_lives} lives left")
        if(found):
            self.num_letters-=1
            print('Good guess!')
            print("Number of guesses remaining :",self.num_letters)

    ## function definition
    def ask_for_input(self):
        '''
        Asks the user for a letter and checks two things:
        1. If the letter has already been tried
        2. If the character is a single character
        If it passes both checks, it calls the check_letter method.
        '''
        guess = '  '
        ## Initial validations of the input
        while(len(guess) != 1 or not guess.isalpha()):
            guess = input("Enter a letter as one alpabetical character: ")
            print(guess)
            if len(guess) == 1 and guess.isalpha() and not guess in self.list_of_guesses:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                self.num_lives-=1
                print(f"Your have {self.num_lives} lives left")
                continue
            else:
                print('Invalid letter.')
                continue
            print("List of guesses : ", self.list_of_guesses)



## Main function definition
def play_game(word_list):
    num_lives = 5

    game=Hangman(word_list, num_lives) 
    
    while(game.num_lives >= 0):
        if(game.num_lives == 0):
            print("You Lost!")
            print("The word was :", game.word)
            break
        elif(game.num_letters > 0):
            game.ask_for_input()
            print("The word looks like this now : ", game.word_guessed)
        elif(game.num_lives != 0 and not game.num_letters > 0):
            print('Congratulations. You won the game!')
            print("The word was :", game.word)
            break

## Main function call
if __name__ == '__main__':
    word_list = ['Mango', 'Jackfruit', 'Strawberry', 'Grapes', 'Pineapple']
    
    play_game(word_list)
