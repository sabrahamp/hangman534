## Importing relevant packages
import random

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
        ## Variables of the class being initialized 
        self.word_list=word_list
        self.num_lives=num_lives

        self.word = random.choice(self.word_list).lower()
        print(self.word)
        self.word_guessed=[]
        ## Appending "_" for the number of letters in the mystry word
        for i in self.word:
            self.word_guessed.append("_")
        print(self.word_guessed)
        ## Storing the length of the word
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
        ## Specific validations of the input letter with the word
        for index, char in enumerate(self.word):
            ## Check to confirm if the letter is a character and not already been an input
            if guess == char and char not in enumerate(self.word_guessed):
                self.word_guessed[index]=guess
                found=True
            ## If the word is not found prompt the message to user and update lives variable
            elif (index) == (len(self.word)-1) and not found:
                print(f"Sorry, your letter {guess} is not found in the word")
                self.num_lives-=1
                # found=False
                print(f"Your have {self.num_lives} lives left")
        ## If the letter is valid and found in the word then display a message and display number of tries remaining
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
            ## If the input is one character and not already used call check_guess function & store the letter
            if len(guess) == 1 and guess.isalpha() and not guess in self.list_of_guesses:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
            ## Validation failure check for using the same letter again so, displaying a message indicating no. of lives remaining 
            elif guess in self.list_of_guesses:
                print("You already tried that letter!")
                self.num_lives-=1
                print(f"Your have {self.num_lives} lives left")
                continue
            ## Validation failure check for invalid letter and displaying a message 
            else:
                print('Invalid letter.')
                continue
            ## Displaying all list of gusses
            print("List of guesses : ", self.list_of_guesses)



## Main function definition
def play_game(word_list):
    num_lives = 5

    ## Object creation
    game=Hangman(word_list, num_lives) 
    
    ## Main while loop based on "no. of lives" variable from the object 
    while(game.num_lives >= 0):
        ## If no more lives then display message that user lost the game and the actual word
        if(game.num_lives == 0):
            print("You Lost!")
            print("The word was :", game.word)
            break
        ## If the user hasn't lost all no. of chances call main function to get input from the object
        elif(game.num_letters > 0):
            game.ask_for_input()
            print("The word looks like this now : ", game.word_guessed)
        ## If no. of lives is not 0 and reached total no. of letters in the word then diplay message indicating user has won the game and the word
        elif(game.num_lives != 0 and not game.num_letters > 0):
            print('Congratulations. You won the game!')
            print("The word was :", game.word)
            break

## Main function call
if __name__ == '__main__':
    ## List of fruits stored for a random choice for the game
    word_list = ['Mango', 'Jackfruit', 'Strawberry', 'Grapes', 'Pineapple']

    ## Sample commands to see the Docstrings
    ## help(Hangman) 
    ## help(ask_for_input)

    ## Main function call with word-list as parameter 
    play_game(word_list)
