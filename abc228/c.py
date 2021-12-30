# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
3 1
178 205 132
112 220 96
36 64 20
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================
import bisect

n, k = map(int, input().split())

p_sum = []
p_add = []
for i in range(n):
    p1, p2, p3 = map(int, input().split())
    sum_num = sum([p1, p2, p3])
    p_sum.append(sum_num)
    p_add.append(sum_num + 300)

sorted_p_sum = sorted(p_sum)

for score in p_add:
    rank = n + 1 - bisect.bisect_right(sorted_p_sum, score)
    if rank <= k:
        print('Yes')
    else:
        print('No')