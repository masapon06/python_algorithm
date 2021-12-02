# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
20
8 6 5 4 3 5 6 87 8 9 9 7 6 5 4 5 66 77 99 55
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
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#
# ====================ここからテストの回答====================
# def countingSort(arr):
#     # Write your code here
#     counts = [0 for i in range(n)]
#     sort_array = []
#     for i in range(n):
#         counts[arr[i]] += 1
#     return counts

# if __name__ == '__main__':
#     # fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     arr = list(map(int, input().rstrip().split()))

#     result = countingSort(arr)
#     print(result)
#     # fptr.write(' '.join(map(str, result)))
#     # fptr.write('\n')

#     # fptr.close()
# ====================ここまで問題の回答====================


# ====================以下ソートするとこまで====================
def countingSort(arr):
    # Write your code here
    counts = [0 for i in range(100)]
    sort_array = []
    for i in range(n):
        counts[arr[i]] += 1

    # ソート
    for i in range(100):
        if counts[i] != 0:
            for j in range(counts[i]):
                sort_array.append(i)

    # ちゃんとソートされてるのか確かめる
    num = 0
    arr.sort()
    for i in range(n):
        if arr[i] == sort_array[i]:
            num += 1
    if num == n:
        return True, sort_array
    else:
        return False

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)
    print(result)
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
