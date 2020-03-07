#!/bin/python3

import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    d1 = {k: 0 for k in ar}
    for k in ar:
        d1[k] += 1

    d2 = {k: v // 2 for k, v in d1.items()}
    return sum(d2.values())


if __name__ == '__main__':
    n = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    print('ANSWER: {}'.format(result))
