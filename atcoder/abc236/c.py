# ===================入力===================
import io
import sys

_INPUT = """\
7 7
a t c o d e r
a t c o d e r
"""
sys.stdin = io.StringIO(_INPUT)
# ====================コード====================

n, m = map(int, input().split())

S = list(map(str, input().split()))
T = list(map(str, input().split()))

pointer = 0
for s_i in S:
    if s_i == T[pointer]:
        print('Yes')
        pointer += 1
    else:
        print('No')