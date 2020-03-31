#!/usr/bin/python3

# 3_5_double_dice_break
import random

count = 0
while True:
    count += 1
    throw_one = random.randint(1,6)
    throw_two = random.randint(1,6)
    print (throw_one, throw_two)
    if throw_one == 6 and throw_two == 6:
        break
print(count, 'throws to get Double Six!')
