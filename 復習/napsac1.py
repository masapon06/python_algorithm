# ナップサック問題
# 問題url: https://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B&lang=jp

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

n, weight = map(int, input().split())

v = [0 for _ in range(n+1)]
w = [0 for _ in range(n+1)]
for i in range(1, n+1):
    v[i], w[i] = map(int, input().split())

dp = [[-1 for _ in range(weight+2)] for __ in range(n+2)]

def search(i, w_space):
    if dp[i][w_space] != -1:
        return dp[i][w_space]
    res = 0
    if i == n+1:
        res = 0
    elif w[i] > w_space:
        res = search(i+1, w_space)
    else:
        res = max(
            search(i+1, w_space),
            search(i+1, w_space - w[i]) + v[i]
        )
    dp[i][w_space] = res
    return res

print(search(1, weight))
print(dp)


# l = [[-1 for _ in range(3)] for __ in range(6)]
# print(l)
# print(l[1])

# =====================DFSだけのコード===================
# n, weight = map(int, input().split())

# v = [0 for _ in range(n+1)]
# w = [0 for _ in range(n+1)]
# for i in range(1, n+1):
#     v[i], w[i] = map(int, input().split())

# def search(i, w_space):
#     if i == n+1:
#         return 0
#     if w[i] > w_space:
#         return search(i+1, w_space)
#     return max(
#         search(i+1, w_space),
#         search(i+1, w_space - w[i]) + v[i]
#     )

# print(search(1, weight))
# ========================================
# =====================↓ミスってたコード===================
# dp = [[-1 for _ in range(weight+1)] for __ in range(n+2)]
# def search(i, w_space):
#     if i == n+1:
#         return 0
#     if w[i] > w_space:
#         if dp[i+1][w_space] == -1:
#             dp[i+1][w_space] = search(i+1, w_space)
#         return dp[i+1][w_space]
#     if dp[i+1][w_space] == -1:
#         dp[i+1][w_space] = search(i+1, w_space)
#     if dp[i+1][w_space - w[i]] == -1:
#         dp[i+1][w_space - w[i]] = search(i+1, w_space - w[i]) + v[i]
#     return max(
#         dp[i+1][w_space],
#         dp[i+1][w_space - w[i]]
#     )
# print(search(1, weight))
# print(dp)
# ========================================
# ==================ミスってるコード2======================
# def search(i, w_space):
#     if dp[i][w_space] != -1:
#         return dp[i][w_space]
#     res = 0
#     if i == n+1:
#         dp[i][w_space] = 0
#         res = 0
#     elif w[i] > w_space:
#         dp[i][w_space] = search(i+1, w_space)
#         res = dp[i][w_space]
#     else:
#         dp[i][w_space] = max(
#             search(i+1, w_space),
#             search(i+1, w_space - w[i]) + v[i]
#         )
#         res = dp[i][w_space]
#     return res
# ===================↓きれいなコード=====================
# def search(i, w_space):
#     if dp[i][w_space] != -1:
#         return dp[i][w_space]
#     res = 0
#     if i == n+1:
#         res = 0
#     elif w[i] > w_space:
#         res = search(i+1, w_space)
#     else:
#         res = max(
#             search(i+1, w_space),
#             search(i+1, w_space - w[i]) + v[i]
#         )
#     dp[i][w_space] = res
#     return res
# ========================================
# i: 1, 2, 3, 4
# v: 4, 5, 2, 8
# w: 2, 2, 1, 3