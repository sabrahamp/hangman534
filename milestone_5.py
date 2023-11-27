import random

word = ''
my_favourite_fruits = ['Mango', 'Jackfruit', 'Strawberry', 'Grapes', 'Pineapple']
word_list = my_favourite_fruits
print(my_favourite_fruits)
word = random.choice(word_list).lower()
print(word)
word_guessed=[]
for i in word:
    word_guessed.append("_")
print(word_guessed)
num_letters=len(set(word))
print("num_letters", num_letters)
num_lives=0
list_of_guesses=[]

class Hangman:
    def __init__(self, word_list, num_lives):
        self.word_list=word_list
        self.num_lives=num_lives

    def check_guess(self, guess):
        guess = guess.lower()
        found=False
        for index, char in enumerate(word):
            if guess == char and char not in enumerate(word_guessed):
                word_guessed[index]=guess
                found=True
            elif (index) == (len(word)-1) and not found:
                print(f"Sorry, your {guess} is not found in the word")
                self.num_lives-=1
                found=False
                print(f"Your have {self.num_lives} lives left")
        if(found):
            global num_letters
            num_letters-=1
            print('Good guess!')
            print("Number of guesses remaining :",num_letters)

    def ask_for_input(self):
        guess = '  '
        print(len(guess))
        while(len(guess) != 1 or not guess.isalpha()):
            guess = input("Enter your value as one alpabetical char: ")
            print(guess)
            if len(guess) == 1 and guess.isalpha() and not guess in list_of_guesses:
                self.check_guess(guess)
                list_of_guesses.append(guess)
            elif guess in list_of_guesses:
                print("You already tried that letter!")
                self.num_lives-=1
                print(f"Your have {self.num_lives} lives left")
                continue
            else:
                print('Invalid letter. Please, enter a single alphabetical character.')
                continue
            print("List of guesses : ", list_of_guesses)



def play_game(word_list):
    num_lives = 5
    game=Hangman(word_list, num_lives) 
    while(game.num_lives >= 0):
        if(game.num_lives == 0):
            print("You Lost!")
            break
        elif(num_letters > 0):
            game.ask_for_input()
        elif(num_lives != 0 and not num_letters > 0):
            print('Congratulations. You won the game!')
            print("The word was :", word)
            break


play_game(word_list)


