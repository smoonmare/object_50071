#!/usr/bin/env python3

from math import *

# Function to generate all prime numbers which are less then given N
def make_it_prain(n, isPrime):
    # Initializing that 0 and 1 aren't prime numbers
    # and the rest of the array as prime
    isPrime[0], isPrime[1] = False, False

    for i in range(2, n+1):
        isPrime[i] = True
    
    # if P is not changed - it's prime
    for p in range(2, int(sqrt(n)) + 1):
        if isPrime[p] == True:
            for i in range(p*2, n+1, p):
                isPrime[i] = False


def product_of_primes(n):
    flag = 0

    # Generating prime array
    # using Sieva of Eratisthenes
    isPrime = [False] * (n+1)
    make_it_prain(n, isPrime)

    # Traversing through to find a pair
    for i in range(2, n):
        x = int(n / i)

        if (isPrime[i] & isPrime[x] and 
            x != i and x * i == n):
            print("{0} * {1} = {2}".format(x, i, n))
            flag = 1
            break

    if not flag:
        print("There are no prime numbers")         


if __name__ == "__main__":
    n = 2060

    product_of_primes(n)
