# ゆっくり解説のbfsの問題

# ===================デバッグ用入力===================
import io
import sys
from collections import deque

_INPUT = """\
4 3
1 2
2 3
2 4
2 10
1 100
3 1
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

n, q = map(int, input().split())

tree = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

count_list = [0 for _ in range(n+1)]
for __ in range(q):
    node, count = map(int, input().split())
    count_list[node] += count

flag = [False for _ in range(n+1)]

queue = deque()
queue.append(1)
while len(queue) > 0:
    now = queue.popleft()
    flag[now] = True
    for node in tree[now]:
        if flag[node] == False:
            count_list[node] += count_list[now]
            queue.append(node)

print(' '.join(map(str, count_list[1:])))
# 行ったことにする
# つながっているものかついったときないものなら、すでに行ったカウンタを足してqueに入れる
# ひとつqueから取り出す
# 1にもどる
