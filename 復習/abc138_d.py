# ===================デバッグ===================
import io
import sys

_INPUT = """\
6 2
1 2
1 3
2 4
3 6
2 5
1 10
1 10
"""
sys.stdin = io.StringIO(_INPUT)
# ====================コード====================
from collections import deque

n, q = map(int, input().split())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

score_bucket = [0 for _ in range(n+1)]

for _ in range(q):
    node, score = map(int, input().split())
    score_bucket[node] += score

flag_bucket = [False for _ in range(n+1)]
queue = deque()

queue.append(1)
flag_bucket[1] = True

while len(queue) > 0:
    now = queue.popleft()
    flag_bucket[now] = True
    connect = tree[now]
    for node in connect:
        if flag_bucket[node] == False:
            score_bucket[node] += score_bucket[now]
            queue.append(node)
print(' '.join(map(str, score_bucket[1:])))