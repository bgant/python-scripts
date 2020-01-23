# Generate Fibonacci Sequence
# Supercharged Python, page 14

def main():
    n = int(input('Input number: '))
    print(fibonacci(n))

def fibonacci(n):
    the_list = []
    a, b = 1, 0
    while a < n:
        the_list.append(a)
        a, b = a + b, a
    return the_list

if __name__ == '__main__':
    main()
