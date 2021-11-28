# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
1 2 3 4 5
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here\
    arr.sort()
    for i in range(5):
        mini = sum(arr[:4])
        maxi = sum(arr[1:])
    print(mini, maxi)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

