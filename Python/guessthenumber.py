'''
1.Generate a random number
#loop
2.Ask the user to make a guess
3.If not a valid number
4.Print an error
5.If number < guess
6.Print too low
7.If number > guess
8. else
9. print well done
'''

import random

num_guess = random.randint(1, 10)

while True:
    try:
        guess = int(input("Guess the number between 1 and 10: "))
        if guess < num_guess:
            print('TOO LOW')
        elif guess > num_guess:
            print("TOO HIGH")
        else:
            print("WELL DONE! YOU HAVE GUESSED THE RIGHT NUMBER")
            break
    except ValueError:
        print('Please enter a valid number:')

