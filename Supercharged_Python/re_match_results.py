# Supercharged Python, page 203

import re

pattern = r'(a+)(b+)(c+)'
m = re.match(pattern, 'abbccceeee')

print(m.group(0))    # Entire pattern matched
print(m.group(1))    # First group matched
print(m.group(2))    # Second group matched
print(m.group(3))    # Third group matched

print(m.groups())    # Returns a tuple
print(m.groupdict()) # Returns a dictionary of named groups
