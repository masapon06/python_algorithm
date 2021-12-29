# # ===================デバッグ用入力===================
# import io
# import sys

# _INPUT = """\

# """
# sys.stdin = io.StringIO(_INPUT)
# # ====================ここから入力====================
import bisect

arr = [1, 2, 3, 4, 5, 5, 5, 7, 8, 9, 9, 10]

# t = bisect.bisect_left(arr, 9)

# print(t) # >> 9

u = bisect.bisect_right(arr, 1)
print(u)
