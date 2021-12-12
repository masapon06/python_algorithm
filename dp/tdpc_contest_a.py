# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
3
2 3 5
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

n = int(input())
scores = list(map(int, input().split()))

table = []

def rec(i, score):
    if i == n:
        if score == 0:
            return True
        else:
            return False
    if rec(i+1, score - scores[i]) == True:
        return True
    if rec(i+1, score) == True:
        return True
    return False

ans = 0
for i in range(sum(scores) * n):
    if(rec(0, i) == True):
        ans += 1
print(ans)


# ===============再帰で全探索=====================
# n = int(input())
# scores = list(map(int, input().split()))

# table = []

# def rec(i, score):
#     if i == n:
#         if score == 0:
#             return True
#         else:
#             return False
#     if rec(i+1, score - scores[i]) == True:
#         return True
#     if rec(i+1, score) == True:
#         return True
#     return False

# ans = 0
# for i in range(sum(scores) * n):
#     if(rec(0, i) == True):
#         ans += 1
# print(ans)
# =============================================