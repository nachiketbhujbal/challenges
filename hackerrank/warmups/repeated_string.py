#!/bin/python3

import math
import os
import random
import re
import sys

def repeatedString(s, n):
    ains = [1 if x == 'a' else 0 for x in s]
    ndiv = n // len(s)
    nmod = n % len(s)
    numa = ndiv * sum(ains) + sum(ains[:nmod])
    return numa

if __name__ == '__main__':
    s = input()
    n = int(input())
    result = repeatedString(s, n)
    print('ANSWER: {}'.format(result))
