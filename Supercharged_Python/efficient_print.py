# Supercharged Python, page 114
# Slowest to Fastest ways to print() 40x20 block of asterisks.

print('Slowest way to print:')
for i in range(20):
    for j in range(40):
        print('*', end='')
    print()
print()

print('Faster by printing full row at a time:')
row_of_asterisks = '*' * 40
for i in range(20):
    print(row_of_asterisks)
print()

print('Even faster by calling print() function only once:')
row_of_asterisks = '*' * 40
s = ''
for i in range(20):
    s += row_of_asterisks + '\n'
print(s)
print()

print('Faster by using in-place appending instead of creating new string variables')
row_of_asterisks = '*' * 40
list_of_str = []
for i in range(20):
   list_of_str.append(row_of_asterisks)
print('\n'.join(list_of_str))
print()

print('Fastest in one-line:')
print('\n'.join(['*' * 40] * 20))
print()

