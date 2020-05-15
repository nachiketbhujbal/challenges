#!/usr/local/bin/python3
# date: 2020-05-15
# author: Nachiket Bhujbal
# Problem #4:
'''
A palindromic number reads the same both ways.
The largest palindrome made from the product of
two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the
product of two 3-digit numbers.
'''
# note: gentools in https://github.com/nachiketbhujbal/playground/py
import sys
import time
from gentools import custominput, customoutput

def isPalindrome(p):
    # check if number p is a palindrome number
    strlist = list(str(p))
    if strlist == strlist[::-1]:
        return True
    else:
        return False

def palindrome_product(n, d):
    # n is the quantity of numbers (i.e. 2 numbers)
    # d is the number of digits in each number (i.e. 2 digits)
    print('You\'ve chosen to find the largest palindrome number that is a '
          'product of {}, {} digit numbers'.format(n, d + 1))

    start = int('1' + ''.join(['0' for x in range(d)]))
    endat = int('1' + ''.join(['0' for x in range(d + 1)]))
    numls = list(range(start, endat))
    prods = []
    for i in numls:
        for j in numls:
            prod = i * j
            if isPalindrome(prod):
                prods.append(prod)
                # print(prods)

    return prods

def main():
    N = int(input('Enter how many numbers to find a product of: N = '))
    D = int(input('Enter how many digits each number has: D = ')) - 1
    palin_prods = palindrome_product(N, D)
    P = max(palin_prods)
    printans = 'Largest palindrome product of {}, {} digit numbers is: {}'
    print(printans.format(N, D, P))



if __name__ == '__main__':
    main()


