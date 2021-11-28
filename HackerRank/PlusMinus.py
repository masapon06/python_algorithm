# https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=preparation-kits&playlist_slugs%5B%5D=one-week-preparation-kit&playlist_slugs%5B%5D=one-week-day-one

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(n, arr):
    # Write your code here
    plus = 0
    minus = 0
    zero = 0
    for i in range(n):
        if arr[i] > 0:
            plus += 1
        if arr[i] < 0:
            minus += 1
        if arr[i] == 0:
            zero += 1
    print(plus / n)
    print(minus / n)
    print(zero / n)
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(n, arr)
