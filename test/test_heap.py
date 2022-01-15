# # ===================デバッグ用入力===================
# import io
# import sys

# _INPUT = """\

# """
# sys.stdin = io.StringIO(_INPUT)
# # ====================ここから入力====================

import heapq

x = [7, 5, 3, 2, 4, 8, 10, 1]
heapq.heapify(x)

print(x)

a = heapq.heappop(x)
print(a)
print(x)

b = heapq.heappop(x)

print(b)
print(x)