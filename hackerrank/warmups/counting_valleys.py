#!/bin/python3

import math
import os
import random
import re
import sys

def countingValleys(n, s):
    countvals = 0
    start_level = 0
    for letter in s:
        if letter == 'U':
            new_level = start_level + 1
        elif letter == 'D':
            new_level = start_level - 1

        if new_level < start_level and start_level == 0:
            countvals += 1

        start_level = new_level

    return countvals

if __name__ == '__main__':
    n = int(input())
    s = input()
    result = countingValleys(n, s)
    print('ANSWER: {}'.format(result))
