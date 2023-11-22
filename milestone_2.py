import random
word = ''
my_favourite_fruits = ['Mango', 'Jackfruit', 'Strawberry', 'Grapes', 'Pineapple']
word_list = my_favourite_fruits
print(my_favourite_fruits)
print(my_favourite_fruits[3])
word = random.choice(word_list).lower()
print(word)

def check_guess(guess):
    guess = guess.lower()
    for char in word:
        if guess == char:
            print(guess, ' was found in ', word)
            break

def ask_for_input():
    guess = '  '
    print(len(guess))
    while(len(guess) != 1 or not guess.isalpha()):
        guess = input("Enter your value as one Alpabetical char: ")
        print(guess)
        if len(guess) == 1 and guess.isalpha():
            print('Good guess!')
        else:
            print('Ooops!, That is not a valid input.')
            continue
    check_guess(guess)




ask_for_input()