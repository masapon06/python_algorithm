# ===================デバッグ用入力===================
import io
import sys
from collections import deque

_INPUT = """\
3 7
abcdefgh
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

x, y = map(int, input().split())

S = list(input())

r_s = []
for i in range(x-1, y):
    r_s.append(S[i])

r_s.reverse()

for i in range(x-1, y):
    S[i] = r_s[i - (x-1)]
print(''.join(S))