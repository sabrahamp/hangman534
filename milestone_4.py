import random

word = ''
my_favourite_fruits = ['Mango', 'Jackfruit', 'Strawberry', 'Grapes', 'Pineapple']
word_list = my_favourite_fruits
print(my_favourite_fruits)
print(my_favourite_fruits[3])
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
            print("index :",index)
            print("len - 1",  (len(word)-1))
            if guess == char:
                print(index, guess, ' was found in ', word)
                word_guessed[index]=guess
                print("Word guessed appended :", word_guessed)
                found=True
                #break
            elif (index) == (len(word)-1) and not found:
                print(f"Sorry, your {guess} is not found in the word")
        self.num_lives-=1
        print(f"Your have {self.num_lives} lives left")

    def ask_for_input(self):
        guess = '  '
        print(len(guess))
        while(len(guess) != 1 or not guess.isalpha()):
            guess = input("Enter your value as one alpabetical char: ")
            print(guess)
            if len(guess) == 1 and guess.isalpha():
                print('Good guess!')
                self.check_guess(guess)
                list_of_guesses.append(guess)
            elif guess in list_of_guesses:
                print("You already tried that letter!")
                ## for i in list_of_guesses:
                ##    if list_of_guesses[i]==guess
                ##        print("You already tried that letter!")
                list_of_guesses.append(guess)
                continue
            else:
                print('Invalid letter. Please, enter a single alphabetical character.')
                continue
            print("List of guesses : ", list_of_guesses)

hangman=Hangman(word_list, 5) 
hangman.ask_for_input()


