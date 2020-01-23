# Supercharged Python, page 137

def make_fibo_gen(n):
    a, b = 1, 1
    while a <= n:
        yield a
        a, b = a + b, a

n = int(input('Enter number: '))
if n in make_fibo_gen(n):
    print('number is a Fibonacci.')
else:
    print('number is NOT a Fibonacci.')
