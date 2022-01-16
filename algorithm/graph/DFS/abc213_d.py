# 深さ優先探索(DFS)
# notion: https://www.notion.so/59a0cedb08004e2caed37bcc20651c3b

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

n = int(input())

connect = [[] for i in range(n+1)]
for i in range(n-1):
    a, b = map(int, input().split())
    connect[a].append(b)
    connect[b].append(a)

ans = []
def dfs(now, pre):
    ans.append(now)
    for city in connect[now]:
        if city != pre:
            dfs(city, now)
            ans.append(now)

dfs(1, -1)

print(ans)
