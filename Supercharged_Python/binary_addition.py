# Supercharged Python, page 176

def calc_binary():
    print('Enter values in binary only:')
    b1 = int(input('Enter b1:'), 2)
    b2 = int(input('Enter b2:'), 2)
    print('Total is: {:#b}'.format(b1 + b2))
    print('{} + {} = {}'.format(b1, b2, b1 + b2))

calc_binary()  
