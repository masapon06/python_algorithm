# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
4 5
4 2
5 2
2 1
8 3
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

v = []
w = []

[N, Weight] = array = list(map(int, input().split()))

for i in range(N):
    item = list(map(int, input().split()))
    v.append(item[0])
    w.append(item[1])

# def sac(i, n):
#     print(i, n)
