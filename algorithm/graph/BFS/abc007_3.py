# 幅優先探索（BFS）
# youtube解説：https://www.youtube.com/watch?v=6QKW-HQV-hE

# ===================デバッグ用入力===================
import io
import sys
from collections import deque

_INPUT = """\
5 8
2 2
2 4
########
#.#....#
#.###..#
#......#
########
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

grid = [list(input()) for i in range(r)]

queue = deque()
score_map = [[-1 for i in range(c)] for i in range(r)]
score_map[sy-1][sx-1] = 0
queue.append([sy, sx])

# そのセルの座標を入れると、行ける方向を返す関数
# cell: [x, y]
def can_go(cell):
    can_go_list = []
    judge_can_go = [
        [cell[0]-1, cell[1]], # 上
        [cell[0], cell[1]+1], # 右
        [cell[0]+1, cell[1]], # 下
        [cell[0], cell[1]-1], # 左
    ]
    for one in judge_can_go:
        if grid[one[0]-1][one[1]-1] == '.':
            can_go_list.append(one)
    return can_go_list

while len(queue) > 0:
    sy, sx = queue.popleft()
    can_go_list = can_go([sy, sx])
    for cell in can_go_list: # すでに行った場所か、行ってないか確かめる
        if score_map[cell[0]-1][cell[1]-1] == -1:
            score_map[cell[0]-1][cell[1]-1] = score_map[sy-1][sx-1] + 1
            queue.append(cell)
print(score_map[gy-1][gx-1])