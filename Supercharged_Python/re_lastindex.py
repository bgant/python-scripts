# Supercharged Python, page 204

import re
pattern = r'(a+)(b+)(c+)'
m = re.match(pattern, 'abbccceeee')

for i in range(m.lastindex + 1):
    print(i, '. ', m.group(i), sep='')

