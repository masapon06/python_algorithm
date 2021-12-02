# # ===================デバッグ用入力===================
# import io
# import sys
from collections import deque

# _INPUT = """\

# """
# sys.stdin = io.StringIO(_INPUT)
# # ====================ここから入力====================


a = 37 # 100101
b = 41 # 101001

queue = deque()

queue.append(1)
queue.append(3)
queue.append(7)
queue.append(8)

num = 0
while (len(queue) > 0):
    num += 1
    print(num)
    print(queue)
    queue.popleft()
    if len(queue) == 0:
        queue.append(5)
    if num >= 20:
        break


#print(a ^ b) 1101