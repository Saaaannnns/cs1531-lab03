'''
Number Guessing Game.

Guesses are made until all numbers are guessed.
The game reveals whether the closest unguessed number is higher or lower than each guess.
Numbers are distinct.
Typing 'q' quits the game.
'''

import random

MIN = 0
MAX = 10
NUM_VALUES = 3

def handle_guess(guess, values):
    # This function should return a duplicate list of values
    # with the guessed value removed if it was present.
    pass
    if int(guess) in values:
        values.remove(int(guess))
    return values

def find_closest(guess, values):
    # This function should return the closest value
    # to the guessed value.
    pass
    closest = values[0]
    for i in range(1,len(values)):
        if abs(int(guess) - closest) >= abs(int(guess) - values[i]):
            closest = values[i]
    return closest

def run_game(values):
    # While there are values to be guessed and the user hasn't
    # quit (with 'q'), the game should wait for the user to input
    # their guess and then reveal whether the closest number is
    # lower or higher.
    print(f'Numbers are between {MIN} and {MAX} inclusive.')
    # Your code goes here.
    while len(values) != 0:
        guess = input(f'There are {len(values)} values left. Guess: ')        
        if guess == 'q': break
        closest = find_closest(guess, values)
        if int(guess) == closest: print(f'You found {guess}! It was in the list.')
        elif int(guess) < closest: print(f'The closest to {guess} is higher')
        else: print(f'The closest to {guess} is lower')
        values = handle_guess(guess, values)

    if guess == 'q': print('Thanks for playing! See you soon.')
    else:
        print('Congratulations! You won!')
        print('Thanks for playing! See you soon.')

if __name__ == '__main__':
    values = sorted(random.sample(range(MIN, MAX+1), NUM_VALUES))
    run_game(values)
