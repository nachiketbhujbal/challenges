#!/bin/python3

import math
import os
import random
import re
import sys

def jumpingOnClouds(c):
    jumps = 0
    player = 0 # first index
    while player + 1 <= len(c) - 1:
        # print('Player Start: {}'.format(player))
        jumps += 1
        player += 1
        j2 = player + 1
        if j2 <= len(c) - 1 and c[j2] != 1:
            player = j2

        # print('Player Ended: {}'.format(player))

    return jumps

if __name__ == '__main__':
    n = int(input())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print('ANSWER: {}'.format(result))
