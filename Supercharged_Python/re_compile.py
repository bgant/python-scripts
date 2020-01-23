# Supercharged Python, page 190

import re  # Import Regular Expression module

reg1 = re.compile(r'ca*b$')  # Compile the pattern so it can be used multiple times

def test_item(s):
    if re.match(reg1, s):
        print(s, 'is a match.')
    else:
        print(s, 'is not a match')

test_item('caab')
test_item('caaxb')
