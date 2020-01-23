# What number am I thinking of?
# Supercharged Python, page 15

from random import randint

maximum = 50
n = randint(1, maximum)

print("I'm thinking of a number between 1 and %s" %  maximum)
while True:
    answer = int(input('Enter a guess: '))
    if answer > n:
        print('Too High... ')
    elif answer < n:
        print('Too Low... ')
    else:
        print('You got it!')
        break

