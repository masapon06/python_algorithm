# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
4 4
1 2
1 3
1 4
3 4
1 3
1 4
2 3
3 4
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================
import itertools
import numpy as np

n, m = map(int, input().split())

t_graph = [[] for _ in range(m+1)]
a_graph = [[] for _ in range(m+1)]

for i in range(m):
    a, b = map(int, input().split())
    t_graph[a].append(b)
    t_graph[b].append(a)

for i in range(m):
    a, b = map(int, input().split())
    a_graph[a].append(b)
    a_graph[b].append(a)

inp_list = list(range(1,n+1))
permutations = list(itertools.permutations(inp_list))

for perm in permutations:
    changed_graph = a_graph
    for i in range(len(changed_graph)):
        for j in range(len(changed_graph[i])):
            changed_graph[i][j] = perm[changed_graph[i][j]-1]
    flag = np.array_equal(t_graph, changed_graph)

if flag == True:
    print('Yes')
else:
    print('No')
