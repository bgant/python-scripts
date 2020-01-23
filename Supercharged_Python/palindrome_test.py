# Supercharged Python, page 107
# Test to see if input is a palindrome.
# Examples:
#   racecar
#   A man, a plan, a canal, Panama!

test_str = input('Enter test string: ')
a_list = [c.upper() for c in test_str if c.isalnum()]
print(a_list == a_list[::-1])

