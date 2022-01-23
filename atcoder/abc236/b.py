# ===================入力===================
import io
import sys

_INPUT = """\
4
3 2 1 1 2 4 4 4 4 3 1 3 2 1 3
"""
sys.stdin = io.StringIO(_INPUT)
# ====================コード====================

n = int(input())

a = list(map(int, input().split()))
a.sort()
a.append(-1)

for i in range(n):
    if a[4*i+3] != i+1:
        print(i+1)
        break