
# ===================デバッグ用入力===================
import io
import sys
from collections import deque

_INPUT = """\
5 5
804289384 846930887 681692778 714636916 957747794
424238336
719885387
649760493
596516650
189641422
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

# アイデア1. Aがインデックスの最大10^9の長さのバケットをつくって、バケットそれぞれに"以上の数"を入れる




# ====================TLE====================
import bisect

n, q = map(int, input().split())

a = list(map(int, input().split()))
a.sort()

arr = [int(input()) for _ in range(q)]

for x in arr:
    index = bisect.bisect_left(a,x)

    print(n - index)
# ============================================