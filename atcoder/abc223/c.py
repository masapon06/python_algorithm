# ===================デバッグ用入力===================
import io
import sys
from collections import deque

_INPUT = """\
20
224 433
987654321 987654321
2 0
6 4
314159265 358979323
0 0
-123456789 123456789
-1000000000 1000000000
124 233
9 -6
-4 0
9 5
-7 3
333333333 -333333333
-9 -1
7 -10
-1 5
324 633
1000000000 -1000000000
20 0
"""
sys.stdin = io.StringIO(_INPUT)
# ====================コード====================

import itertools

# def judge_same_tilt(x1, y1, x2, y2, x3, y3):
#     if (x3 - x1) == 0 or (x2 - x1) == 0:
#         if (x3 - x1) == (x2 - x1):
#             return True
#         else:
#             return False
#     elif (y3 - y1) / (x3 - x1) == (y2 - y1) / (x2 - x1):
#         return True
#     else:
#         return False
def judge_no_menseki(x1, y1, x2, y2, x3, y3):
    if abs((x1-x3)*(y2-y3)-(x2-x3)*(y1-y3)) / 2 == 0:
        return True
    else:
        return False

n = int(input())

coordinates = []
for i in range(n):
    coordinates.append(list(map(int, input().split())))

minus_count = 0
count = 0
all = list(itertools.combinations(coordinates, 3))
for x in all:
    count += 1
    isNoMenseki = judge_no_menseki(x[0][0], x[0][1], x[1][0], x[1][1], x[2][0], x[2][1])
    if isNoMenseki:
        minus_count += 1
print(count - minus_count)


