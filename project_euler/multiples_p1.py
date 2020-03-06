#!/usr/local/bin/python3
# date: 2020-03-05
# author: Nachiket Bhujbal
'''
Problem #1:

    If we list all the natural numbers below 10 that are multiples
    of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1,000.
'''
# note: gentools in https://github.com/nachiketbhujbal/playground/py
import sys
import time
from gentools import custominput, customoutput, sum_k

def iterative_solution(N):
    t0 = time.time()
    result = sum([x for x in range(N) if (x % 3 == 0) or (x % 5 == 0)])
    customoutput('Order (N)', N, result, t0)

def order1_solution(N):
    t0 = time.time()
    result = sum_k(N, k=3) + sum_k(N, k=5) - sum_k(N, k=15)
    customoutput('Order (1)', N, result, t0)

def main():
    N = custominput('upper bound')
    print('Finding sum of all multiples of 3 or 5 below N = {}...'.format(N))
    iterative_solution(N=N)
    order1_solution(N=N)


if __name__ == '__main__':
    main()
