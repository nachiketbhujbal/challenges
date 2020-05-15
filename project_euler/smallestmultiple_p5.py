#!/usr/local/bin/python3
# date: 2020-05-15
# author: Nachiket Bhujbal
# Problem #5:
'''
2520 is the smallest number that can be divided by each
of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
'''
# note: gentools in https://github.com/nachiketbhujbal/playground/py
import sys
import time
from gentools import custominput, customoutput


def main():
    N = int(input('Enter how many numbers to find a product of: N = '))
    D = int(input('Enter how many digits each number has: D = ')) - 1
    palin_prods = palindrome_product(N, D)
    P = max(palin_prods)
    printans = 'Largest palindrome product of {}, {} digit numbers is: {}'
    print(printans.format(N, D, P))



if __name__ == '__main__':
    main()


