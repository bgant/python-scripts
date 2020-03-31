#!/usr/bin/python3

import string

try:
    words = []
    f = open('/usr/share/dict/american-english')
    line = f.readline().strip()
    while line != '':
        if line.find("'") != -1:
            print("Found apostrophe in " + line)
            next
        elif len(line) != len(line.encode()):
            print("Found unicode in " + line)
            next
        elif line.endswith('s') == True:
            print("Found ending 's' in " + line)
            next
        elif line.endswith('ed') == True:
            next
        elif line.endswith('est') == True:
            next
        elif line.endswith('ing') == True:
            next
        elif line.endswith('ier') == True:
            next
        else:
            words.append(line)
        line = f.readline().strip()
    f.close()
except IOError:
    print('Cannot find file: ' + f)

print(words)
