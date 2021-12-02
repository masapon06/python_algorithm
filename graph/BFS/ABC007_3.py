# 幅優先探索（BFS）
# youtube解説：https://www.youtube.com/watch?v=6QKW-HQV-hE

# ===================デバッグ用入力===================
import io
import sys
from collections import deque

_INPUT = """\
7 8
2 2
4 5
########
#......#
#.######
#..#...#
#..##..#
##.....#
########
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

r, c = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())

grid = [list(input()) for i in range(r)]


print(grid)