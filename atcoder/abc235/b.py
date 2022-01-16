# ===================入力===================
import io
import sys

_INPUT = """\
5
1 5 10 4 2
"""
sys.stdin = io.StringIO(_INPUT)
# ====================コード====================

n = int(input())
arr = list(map(int, input().split()))

now = [0, arr[0]]
for i in range(1, n):
    if i == now[0] + 1 and arr[i] > now[1]:
        now = [i, arr[i]]

print(now[1])