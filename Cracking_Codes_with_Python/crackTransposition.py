
import scrabbleCheat
from collections import Counter
import random
import math
import itertools
import sys


def main():
    ciphertext = input('ciphertext: ') 
    minimum_word_length = int(input('minimum word length: '))
    leftover_characters = int(input('leftover characters: '))
    print()
    
    allResults = decrypt(ciphertext, minimum_word_length, leftover_characters)

    print() 
    print(allResults)


def listPerms(stuff):
    stuff = list(stuff)
    generator_object = (subset for subset in itertools.permutations(stuff, len(stuff)))
    for value in generator_object:
        yield value


def decrypt(ciphertext, minimum_word_length=4, leftover_characters=0):

    ciphertext = ciphertext.lower()
    ciphertext = ciphertext.split()
    ciphertext = ''.join(ciphertext)

    # Mix things up to improve chance of hit?
    ciphertext = list(ciphertext)
    random.shuffle(ciphertext)
    ciphertext = ''.join(ciphertext)
    print('scrambled ciphertext: ', ciphertext)
    print()

    AVAILABLE_WORDS = scrabbleCheat.words(ciphertext, minimum_word_length=4)
    print('Dictionary words available: ', len(AVAILABLE_WORDS))
    print()

    generator_object = listPerms(ciphertext)  # Generator Object
    totalPerms = math.factorial(len(ciphertext))

    messagesWithWords = []
    for i in range(1, totalPerms+1):
        message = ''.join(next(generator_object))  # Next Value in Generator Object
        wordsFound = []
    
        for word in AVAILABLE_WORDS:
            if word in message:
                wordsFound.append(word)
                remainderText = message.split(word)
                message = ''.join(remainderText)

        #if len(message) <= scrabbleCheat.MINIMUM_WORD_LENGTH:
        if len(message) <= leftover_characters:
            wordsFound.append(message)
            if wordsFound not in messagesWithWords:
                messagesWithWords.append(wordsFound)
                print('Permutation %s:\t %s' % (i,' '.join(wordsFound)))

    return messagesWithWords


if __name__ == '__main__':
    main()
