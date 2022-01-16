# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
10 3141
314944731 649
140276783 228
578012421 809
878510647 519
925326537 943
337666726 611
879137070 306
87808915 39
756059990 244
228622672 291
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

n, w = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
arr = sorted(arr, reverse=True, key=lambda x: x[0])

weight = 0
deli = 0

for c in arr:
    for i in range(c[1]):
        if weight + 1 > w:
            break
        else:
            weight += 1
            deli += c[0]
print(deli)