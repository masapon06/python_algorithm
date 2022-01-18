# ===================入力===================
import io
import sys

_INPUT = """\
2 767090
"""
sys.stdin = io.StringIO(_INPUT)
# ====================コード====================
# ====================↓どっかにバグがあってWAなる====================
# 原因わからず。

# from collections import deque

# a, n = map(int, input().split())
# digit = len(str(n))
# queue = deque()

# memo = [False for _ in range(1000001)]
# count = 0
# queue.append([1, 0])

# output_flag = False
# while len(queue) > 0:
#     queue_head = queue.popleft()
#     num = queue_head[0]
#     count = queue_head[1]

#     if num == n:
#         print(count)
#         output_flag = True
#         break

#     # 操作1
#     times_a_num = num * a

#     # 操作2
#     s = str(num)
#     last = s[-1]
#     left_shift_num = int(last+s[:-1]) # O(n)

#     for numb in [times_a_num, left_shift_num]:
#         if len(str(numb)) <= digit:
#             if memo[numb] == False:
#                 memo[numb] = True
#                 queue.append([numb, count+1])
#     if len(queue) == 0 and output_flag == False:
#         print(-1)

# ====================以下修正コード====================
# from collections import deque

# a, n = map(int, input().split())
# digit = len(str(n))
# queue = deque()

# memo = [False for _ in range(1000001)]
# count = 0
# queue.append([1, 0])

# output_flag = False
# while len(queue) > 0:
#     queue_head = queue.popleft()
#     num = queue_head[0]
#     count = queue_head[1]

#     if num == n:
#         print(count)
#         output_flag = True
#         break

#     # 操作1
#     times_a_num = num * a

#     # 操作2
#     left_shift_num = 10 ** 7
#     if num >= 10 and num % 10 != 0:
#         s = str(num)
#         last = s[-1]
#         left_shift_num = int(last+s[:-1]) # O(n)

#     for numb in [times_a_num, left_shift_num]:
#         if len(str(numb)) <= digit:
#             if memo[numb] == False:
#                 memo[numb] = True
#                 queue.append([numb, count+1])
#     if len(queue) == 0 and output_flag == False:
#         print(-1)

# ====================以下模範解答見たあとのコード====================
from collections import deque

a, n = map(int, input().split())

M = 10 ** (len(str(n)))
d = [-1]*M

d[1] = 0
queue = deque()
queue.append(1)

output_flag = False
while len(queue) > 0:
    c = queue.popleft()
    dc = d[c]

    # 操作1
    op1 = c * a
    if op1 < M and d[op1] == -1:
        queue.append(op1)
        d[op1] = dc + 1
    
    # 操作2
    if not (c >= 10 and c % 10 != 0):
        continue
    s = str(c)
    op2 = int(s[-1] + s[:-1])
    if op2 < M and d[op2] == -1:
        queue.append(op2)
        d[op2] = dc + 1

if output_flag == False:
    print(d[n])
    print(d)
