'''
date: 2020-03-05
author: Nachiket Bhujbal
Problem #1:

If we list all the natural numbers below 10 that are multiples
of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

'''
import sys
import time

def summate(N, k=1):
    p = (N - 1) // k
    result = ((k * p * (p + 1)) // 2)
    return result

def iterative_solution(N):
    t0 = time.time()
    result = sum([x for x in range(N) if (x % 3 == 0) or (x % 5 == 0)])
    answer = 'Sum of multiples of 3 or 5 {} is {}. Solved in {} ms'
    printout(N, t0, result)

def order1solution(N):
    t0 = time.time()
    result = summate(N, k=3) + summate(N, k=5) - summate(N, k=15)
    printout(N, t0, result)

def printout(N, t0, result):
    answer = 'Sum of multiples of 3 or 5 below {} is {}. Solved in {} us'
    t = round(1000000 * (time.time() - t0), 5)
    print(answer.format(N, result, t))

def main(N):
    print('\nThis solution is O(N)')
    iterative_solution(N=N)
    print('\nThis solution is O(1)')
    order1solution(N=N)



if __name__ == '__main__':
    try:
        assert len(sys.argv) == 2, 'Usage: python num1.py N (enter a number)'
        N = int(sys.argv[1])
        main(N)
    except Exception as e:
        raise e
