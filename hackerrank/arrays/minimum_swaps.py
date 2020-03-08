#!/bin/python3

import math
import os
import random
import re
import sys

def minimumSwaps(arr):
    ans = 0
    num = len(arr)
    pos = [*enumerate(arr)]
    pos.sort(key = lambda it: it[1])
    vis = {k: False for k in range(num)}
    for i in range(num):
        if vis[i] or pos[i][0] == i:
            continue

        cycles = 0
        j = i
        while not vis[j]:
            vis[j] = True
            j = pos[j][0]
            cycles += 1

        if cycles > 0:
            ans += (cycles - 1)

    return ans


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    res = minimumSwaps(arr)
    print('ANSWER: {}'.format(result))

