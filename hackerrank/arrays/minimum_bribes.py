#!/bin/python3

import math
import os
import random
import re
import sys

def minimumBribes(q):
    bribes = 0
    for i, v in enumerate(q):
        c = v - (i + 1)
        if c > 2:
            print('Too chaotic')
            return

        for j in range(max(0, v - 2), i):
            if q[j] > v:
                bribes += 1

    print(bribes)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())
        q = list(map(int, input().rstrip().split()))
        minimumBribes(q)
