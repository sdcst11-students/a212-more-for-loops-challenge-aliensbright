#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''
# generate random integer values
from random import seed
from random import randint
# seed random number generator
ran=str(input('Enter a number to start the game=>'))
seed(ran)
# generate some integers
for _ in (ran):
    value = randint(0, 100)
for i in range(1,11):
    x=int(input(f"\n\nWhat is your {i}th guess?==>"))
    if x<value:
        print('Your guess is too low.')
    if x>value:
        print('Your guess is too high.')
    if x==value:
        print(f'You guessed the answer correct, the number was {value}.')
        break
else:
    print(f'\nYou did not guess the number {value} in 10 guesses.\nYou lost :(')