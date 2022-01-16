# 復習

# ===================デバッグ用入力===================
import io
import sys
from collections import deque

_INPUT = """\
4
1 2
4 2
3 1
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

# import sys
sys.setrecursionlimit(10**7)

n = int(input())

connect = [[] for _ in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

for node in connect:
    node.sort()

road = []
def dfs(now, pre):
    road.append(now)
    for node in connect[now]:
        if node != pre:
            dfs(node, now)
            road.append(now)

dfs(1, -1)
print(' '.join(map(str, road)))