from collections import Counter

import matplotlib.pyplot as plt
import numpy as np
import datetime
import random


def guessing_game():
    # randomly generate the index of the letter
    i = random.randrange(0, len(x))
    # a variable that keeps track of the user's attempts
    count_attempts = 1

    try:
        # the first try of the user
        user_input = int(input(f"Can you guess how many times the letter '{x[i]}'\
                               \nhas occured in a text of {sum(y)} words?\n>>> "))

        # loop until the user guesses the number
        while user_input != y[i]:

            if y[i] + round(y[i] * 0.1) >= user_input > y[i]:
                user_input = int(input(''' (1) '''))
                count_attempts += 1

            elif y[i] - round(y[i] * 0.1) <= user_input < y[i]:
                user_input = int(input(''' (2) '''))
                count_attempts += 1

            elif user_input > y[i]:
                user_input = int(input(''' (3) '''))
                count_attempts += 1

            else:
                user_input = int(input(''' (4) '''))
                count_attempts += 1

        string = ''
        if count_attempts == 1:
            string = 'try'
        else:
            string = 'tries'

        print(f"\nCongratulations! You guessed it in {count_attempts} {string}!\
                  \nThe letter '{x[i]}' has occured {y[i]} times in a text of\
                  \n{sum(y)} words.")

    except ValueError:
        print("Please, enter only integers.")


# main function

text = "sojdisodsdkjd"

dictonary = dict(Counter(text))

dictonary = {k: v for k, v in dictonary.items() if k.isalpha()}

print(dictonary)

# dictonary to x and y using zip

x, y = zip(*dictonary.items())

print(type(x))
print(type(y))
