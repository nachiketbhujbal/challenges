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
import time
from gentools import custominput, customoutput

def prime_factors(n):
    factors = []
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0: # this number divides w/o remainder
                factors.append(i)
                break

        n = n // factors[-1]
        if n == 0:
            sys.exit(1)

    return factors

def main():
    N = custominput('integer number')
    factors = prime_factors(N)
    print(factors)
    lpf = max(factors)
    print('The largest prime factor of N = {} is {}'.format(N, lpf))

if __name__ == '__main__':
    main()
