# Supercharged Python, page 108
# Remove all vowels from string.

my_input = input('Enter string: ')
a_list = [ c for c in my_input if c not in 'aeiou']
print(''.join(a_list))
