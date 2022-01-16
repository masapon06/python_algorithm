# ===================入力===================
import io
import sys

_INPUT = """\
5
315 271
-2 -621
-205 -511
-952 482
165 463
"""
sys.stdin = io.StringIO(_INPUT)
# ====================以下コード====================\
import math

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

max_num = 0

for a in arr:
    for b in arr:
        calc_num = math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)
        if calc_num > max_num:
            max_num = calc_num
print(max_num)
        