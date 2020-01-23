# Supercharged Python, page 135

def print_evens():
    for n in range(2, 21, 2):
        print(n, end=' ')

print('Standard print in a for loop:')
print_evens()
print()
print()
print('What type of function is it:')
print(type(print_evens))
print()

def make_evens_gen():
    for n in range(2, 21, 2):
        yield n                # Defines iterator object

print('What type of function when print is replaced with yield:')
print(type(make_evens_gen()))
print()

print('Calling the function directly just resets the generator object:')
print(next(make_evens_gen()))
print(next(make_evens_gen()))
print(next(make_evens_gen()))
print()

print('Assigning the generator to a variable lets us keep track of the state of the iterator')
my_gen = make_evens_gen()
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))
for i in my_gen:
    if i > 11:
        break
    print(i, end=' ')
print()
print(next(my_gen))
print(*[i for i in my_gen], end=' ')
print()

