# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
1 2 3
4 5 6
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================
import bisect

arr = [1, 2, 3, 4, 5, 5, 5, 7, 8, 9, 9, 10]

li = [sum(list(map(int, input().split()))) for _ in range(2)]

print(li)