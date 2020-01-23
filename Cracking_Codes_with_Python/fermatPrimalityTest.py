# Fermat's Little Theorem (Primality Test)
# a**n % n = a  or  a**(n-1) % n = 1 where a < n and a > 1
# if True,  it is probably Prime (need to test more a < n numbers)
# if False, it is definitely not Prime
#
# "Carmichael Numbers" can fool Fermat's test (i.e. 561)
# So must run multiple tests to see if any values of "a" are not = 1
#
# Side Note: Prime numbers can only end with digits 1, 3, 7, 9

import random


def main():
    n = int(input('Number to Test> '))

    if isPrime(n) == True:
        print('%s is a Prime Number!' % n)
    else:
        print('%s is not a prime number.' % n)


def isPrime(n):
    if n <= 1:    # All numbers less than 1 are not Prime
       return False
    elif n == 2:  
       return True
    else:
        random.seed()  # Set by clock value

        # Run x number of Tests
        for x in range(10):
            a = random.randint(2, n-1)
            if a**(n - 1) % n != 1:
                return False
        return True


if __name__ == '__main__':
    main()

