# ===================入力===================
import io
import sys

_INPUT = """\
5
1 3
1 5
3
2 2
3
"""
sys.stdin = io.StringIO(_INPUT)

# ====================import====================
import heapq 
# ==============================================
# ====================コード====================
# q = int(input())

# box = []
# p2_score = 0 # p2の操作をなんとか簡略化できそう...けど思いつかない。

# for i in range(q):
#     splitted = input().split()
#     length = len(splitted)
#     if length == 1: # p3
#         p = int(splitted[0])
#         print(heapq.heappop(box)+p2_score)
#     else: # p1 or p2
#         p, x = map(int, splitted)
#         if p == 1:
#             heapq.heappush(box, x)
#         else:
#             p2_score += x



# ==== 以下解説見たあとのコード　==== 
q = int(input())

box = []
p2_total = 0

query = []
for i in range(q):
    splitted = input().split()
    query.append(splitted)
    length = len(splitted)
    if length == 2: # p2
        p, x = map(int, splitted)
        if p == 2:
            p2_total += x

p2_score = 0
for i in range(q):
    splitted = query[i]
    length = len(splitted)
    if length == 1: # p3
        p = int(splitted[0])
        print(heapq.heappop(box) + p2_total)
    else: # p1 or p2
        p, x = map(int, splitted)
        if p == 1:
            heapq.heappush(box, x - p2_score)
        else:
            p2_score += x
