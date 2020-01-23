# For a given string of characters:
#    1) How many total permutations are there (totalPerms)
#    2) Output a list of lists of every possible permutation (listPerms)
#
# Rather than create a full list of lists held in memory, this script
# generates/iterates each list on the fly.
#
# import permutations
# value = permutations.listPerms('abcd')
# while i <= permutations.totalPerms('abcd')
#     message = ''.join(next(value))
#     <do something with message>


import itertools, math

def main():
    symbols = input('symbols: ')
    print('Total Permutations: ', totalPerms(symbols))


def listPerms(stuff):
    stuff = list(stuff)
    generator_object = (subset for subset in itertools.permutations(stuff, len(stuff)))
    for value in generator_object:
        yield value

def totalPerms(stuff):
    return math.factorial(len(stuff))


if __name__ == '__main__':
    main()
