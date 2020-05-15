#!/usr/local/bin/python3
# date: 2020-05-14
# author: Nachiket Bhujbal
# Problem #3:
'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
'''
# note: gentools in https://github.com/nachiketbhujbal/playground/py
import sys
import math
import time
from gentools import custominput, customoutput

# This solution is most efficient on numbers less than 20 digits,
def prime_factors(n):
    if n < 2:
        print('BAD INPUT: Must enter an integer greater than 1. EXITING')
        sys.exit()

    factors = []
    while n != 1:
        print(n)
        start = factors[-1] if len(factors) > 0 else 2
        endat = math.ceil(math.sqrt(n)) + 1 # only need to check up to sqrt(n)
        print('start: {}, end: {}'.format(start, endat))
        for i in range(start, endat):
            # print('dividing {} / {}'.format(n, i))
            if n % i == 0: # if n divides w/o remainder
                factors.append(i)
                break # exit this for loop after we find another prime factor

        # The following three conditions test for end cases to return our list
        # print(factors)
        if len(factors) < 1: # this means this is already prime:
            return [n]

        if n > factors[-1]: # n should be > than our last factor or we are done
            # n / last factor has remainder -> it is prime, so we are also done
            if n % factors[-1] != 0:
                factors.append(n)
                return factors

            # print('Dividing n = {} by last factor: {}'.format(n, factors[-1]))
            n = n // factors[-1]
        else:
            return factors

        if n == 0: # in case of erroneous divide, just exit and warn
            print('ERROR: Erroneous n = 0 condition met. EXITING')
            sys.exit()

    return factors

def main():
    N = custominput('integer number')
    factors = prime_factors(N)
    print('The prime factors of {} are: {}'.format(N, factors))
    lpf = max(factors)
    print('The largest prime factor of N = {} is {}'.format(N, lpf))

if __name__ == '__main__':
    main()
