# ===================入力===================
import io
import sys

_INPUT = """\
3 2
0 1000000000 999999999
1000000000 1
123456789 1
"""
sys.stdin = io.StringIO(_INPUT)
# ====================コード====================

# n, q = map(int, input().split())

# a = list(map(int, input().split()))

# queries = [list(map(int, input().split())) for _ in range(q)]

# data = [[0] for _ in range(200100)]

# for i in range(n):
#     data[a[i]].append(i+1)

# for q in queries:
#     x = q[0]
#     k = q[1]

#     if k >= len(data[x]):
#         print(-1)
#     else:
#         print(data[x][k])


n, q = map(int, input().split())

a = list(map(int, input().split()))

queries = [list(map(int, input().split())) for _ in range(q)]

data = {}

for i in range(n):
    if a[i] in data:
        row = data[a[i]]
        row.append(i+1)
        data[a[i]] = row
    else:
        data[a[i]] = [i+1]

for q in queries:
    x = q[0]
    k = q[1]
    if x in data:
        if k > len(data[x]):
            print(-1)
        else:
            print(data[x][k-1])
    else:
        print(-1)