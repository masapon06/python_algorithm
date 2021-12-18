# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
atcoder
atcoder
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

alp = [chr(ord("a")+i) for i in range(26)]

hash = {}
for i in range(26):
    hash[alp[i]] = i

S = input()
T = input()

diff = (hash[T[0]] - hash[S[0]] + 26) % 26

flag = 0
for i in range(1, len(S)):
    if alp[(hash[S[i]] + diff) % 26] == T[i]:
        flag += 1

if flag == len(S) - 1:
    print('Yes')
else:
    print('No')
