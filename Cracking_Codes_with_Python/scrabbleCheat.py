# This script takes a string of letters and creates a list of words that can be spelled by those letters

from collections import Counter

def main():
    ciphertext = input('ciphertext: ')

    AVAILABLE_WORDS = words(ciphertext)

    for k in AVAILABLE_WORDS:
        print(k)
    print('Total Words: ', len(AVAILABLE_WORDS))


def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    englishWords = {}
    for word in dictionaryFile.read().lower().split('\n'):
        englishWords[word] = None
    dictionaryFile.close()
    return englishWords


def words(ciphertext, minimum_word_length=3):
    ENGLISH_WORDS = loadDictionary()

    ciphertext = ciphertext.lower().split()  # make lowercase and remove spaces
    ciphertext = ''.join(ciphertext)  # Put string back together without spaces

    availableWords = {}
    for word in ENGLISH_WORDS:
        # Counter handles duplicate characters (i.e. 'hello' in 'xoleh' is False)
        # whereas set('hello').issubset(set('xoleh')) is True
        if not Counter(list(word)) - Counter(list(ciphertext)):
            if len(word) >= minimum_word_length:
                availableWords[word] = None  # Dictionaries can be searched faster than Lists

    # Returns sorted LIST instead of unstructured DICT (unless next line commented)
    availableWords = sorted(availableWords, key=len, reverse=True)
    return availableWords


if __name__ == '__main__':
    main()
