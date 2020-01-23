# Supercharged Python, page 201

import re

pattern1 = r'(\w|[@#$%^&*!]){8,}$'  # Contains at least 8 of the allowed characters
pattern2 = r'.*\d'                  # Contains at least one digit
pattern3 = r'.*[a-z]'               # Contains at least one lower-case letter
pattern4 = r'.*[A-Z]'               # Contains at least one upper-case letter
pattern5 = r'.*[@#$%^&*!]'          # Contains at least one special character

def verify_password(s):
    b = (re.match(pattern1, s) and 
         re.match(pattern2, s) and
         re.match(pattern3, s) and
         re.match(pattern4, s) and
         re.match(pattern5, s))
    return bool(b)

def main():
    password = input('Enter Test Password: ')
    test = verify_password(password) 
    if test:
        print('That would be a valid password')
    else:
        print('That would not be a valid password')

if __name__ == '__main__':
    main()

