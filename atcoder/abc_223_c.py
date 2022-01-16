# ===================デバッグ用入力===================
import io
import sys
from collections import deque

_INPUT = """\
2 40
3 1 8 4
2 10 5
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

n, x = map(int, input().split())

L = []
for i in range(n):
    L.append(list(map(int, input().split()))[1:])

ans = [-1 for _ in range(n)]

def search(now, next_i):
        ans[now[0]] = now
    for node in ans[now]:
        if node != pre:
            search(node, now)
            ans.append(now)

search([0, 0], -1)