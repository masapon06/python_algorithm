# ===================入力===================
import io
import sys

_INPUT = """\
aaaabbbb
1 8
"""
sys.stdin = io.StringIO(_INPUT)
# ====================コード====================

s = list(input())

a, b = map(int, input().split())

s_a = s[a-1]
s_b = s[b-1]

s[a-1] = s_b
s[b-1] = s_a
print(''.join(s))