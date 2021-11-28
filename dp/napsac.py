# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
4 5
4 2
5 2
2 1
8 3
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

v = []
w = []

[N, Weight] = array = list(map(int, input().split()))

for i in range(N):
    item = list(map(int, input().split()))
    v.append(item[0])
    w.append(item[1])

dp = [[-1]*(Weight+1) for j in range(N+1)]

def search(i, j):
    if dp[i][j] != -1:
        return dp[i][j]
    res = 0
    if i == N:
        res = 0
    elif w[i] > j:
        res = search(i+1, j)
    else:
        res = max(
            search(i+1, j - w[i]) + v[i],
            search(i+1, j)
        )
    dp[i][j] = res
    return dp[i][j]

print(search(0, Weight))
# print(dp)