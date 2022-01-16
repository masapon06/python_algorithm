# ===================入力===================
import io
import sys

_INPUT = """\
11 5
3 7 2 5 11 6 1 9 8 10 4
"""
sys.stdin = io.StringIO(_INPUT)
# ====================以下コード====================

# ====================TLE*15====================
# 計算量bisectで減らしはしたが、insertはO(1)ではなくO(n)らしい
import bisect

n, k = map(int, input().split())
arr = list(map(int, input().split()))

s_arr = sorted(arr[:k-1])

for i in range(k-1, n):
    index = bisect.bisect_right(s_arr, arr[i])
    s_arr.insert(index, arr[i])
    print(s_arr[-k])
# ====================TLE====================


