# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
5
0 0 1 2 1
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
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(n, a):
    # Write your code here
    if n == 1:
        return a[0]
    bucket = [0] * 101
    for i in range(n):
        bucket[a[i]] += 1
    for i in range(101):
        if bucket[i] == 1:
            return i
    # return bucket

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(n, a)

    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()
