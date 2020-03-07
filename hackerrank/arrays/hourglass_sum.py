#!/bin/python3

import math
import os
import random
import re
import sys

'''
                        00 01 02 03 04 05 -> index
+1 -2 +4 +1 +4 +9 ----> +1 -2 +4 +1 +4 +9
                        06 07 08 09 10 11 -> index
-9 -4 -8 00 -3 +5 ----> -9 -4 -8 00 -3 +5
                        12 13 14 15 16 17 -> index
00 +9 +2 +1 +1 -1 ----> 00 +9 +2 +1 +1 -1
                        18 19 20 21 22 23 -> index
-1 +2 +4 -4 -6 +7 ----> -1 +2 +4 -4 -6 +7
                        24 25 26 27 28 29 -> index
+5 +5 -5 -2 +2 +1 ----> +5 +5 -5 -2 +2 +1
                        30 31 32 33 34 35 -> index
00 +3 00 -3 00 00 ----> 00 +3 00 -3 00 00
--------------------------------------------------------
+1 -2 +4 -----> 00 01 02 -----> i + 0   i + 1   i + 2
   -4    ----->    07    ----->         i + 7
00 +9 +2 -----> 12 13 14 -----> i + 12  i + 13  i + 14
--------------------------------------------------------
'''

def hourglassSum(arr):
    d = [] # i.e. "1"-d version of 2d array
    for l in arr:
        d += l

    # Hourglass indices are consistent Final one found at len(d) - 14 index
    hourglasses = []
    for i in range(len(d) - 14):
        hgidxs = [0, 1, 2, 7, 12, 13, 14]
        if i % 6 < 4:
            hg = sum([d[i+x] for x in hgidxs])
            hourglasses.append(hg)

    maxhg = max(hourglasses)
    return maxhg

if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)
    print('ANSWER: {}'.format(result))
