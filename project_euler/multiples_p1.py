#!/usr/local/bin/python3
'''
date: 2020-03-05
author: Nachiket Bhujbal
Problem #1:

If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1,000.

'''
import sys
import time

def summate(N, k=1):
    p = (N - 1) // k
    result = ((k * p * (p + 1)) // 2)
    return result

def printout(O, N, t0, result):
    t = round(1000000 * (time.time() - t0), 5)
    answer = 'Order ({}) Solution for N = {} -> {}\n\t-- Solved in {} us'
    print(answer.format(O, N, result, t))

def iterative_solution(N):
    t0 = time.time()
    result = sum([x for x in range(N) if (x % 3 == 0) or (x % 5 == 0)])
    printout('N', N, t0, result)

def order1solution(N):
    t0 = time.time()
    result = summate(N, k=3) + summate(N, k=5) - summate(N, k=15)
    printout('1', N, t0, result)

def main():
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = int(input('Enter an number N = ').strip())

    print('Finding sum of all multiples of 3 or 5 below N = {}...'.format(n))
    iterative_solution(N=n)
    order1solution(N=n)


if __name__ == '__main__':
    main()
