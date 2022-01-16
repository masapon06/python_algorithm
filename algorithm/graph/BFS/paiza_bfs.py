# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
3 6
0 0 1 0 0 0
1 0 1 0 1 0
0 0 0 0 1 0
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================
from collections import deque

h, w = map(int, input().split())

# 迷路で障害物で上下左右を囲いたいときに使う関数
# 【注意】：スペース区切りの入力で使える。ほかの入力形式のときは使えないので注意。
#
# hight: int
# width: int
# obstacle: string
#
def Generate_Grid(hight, width, obstacle):
    grid = [[] for _ in range(hight+2)]
    for i in range(hight+2):
        if i == 0:
            grid[0] = [1 for _ in range(width+2)]
        elif i == hight+1:
            grid[hight+1] = [1 for _ in range(width+2)]
        else:
            row = obstacle+' '+input()+' '+obstacle
            grid[i] = (list(map(int, row.split())))
    return grid

grid = Generate_Grid(h, w, '1')

scores_table = [[-1 for _ in range(w+2)] for __ in range(h+2)]

queue = deque()
queue.append([1, 1])
scores_table[1][1] = 1

while len(queue) > 0:
    now = queue.popleft()
    connects = [
        [now[0]-1, now[1]], # 上
        [now[0], now[1]+1], # 右
        [now[0]+1, now[1]],
        [now[0], now[1]-1],
    ]
    for cell in connects:
        if grid[cell[0]][cell[1]] == 0 and scores_table[cell[0]][cell[1]] == -1:
            scores_table[cell[0]][cell[1]] = scores_table[now[0]][now[1]] + 1
            queue.append(cell)

print(scores_table[h][w])
