
# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
10 10 9
.X...X.S.X
6..5X..X1X
...XXXX..X
X..9X...X.
8.X2X..X3X
...XX.X4..
XX....7X..
X..X..XX..
X...X.XX..
..X.......
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

from collections import deque

h, w, n = map(int, input().split())

S = [-1, -1]
grid = []
for i in range(1, h+1):
    row = list('X'+input()+'X')
    if i == 1:
        grid.append(['X' for _ in range(len(row))])
    grid.append(row)
    if i == h:
        grid.append(['X' for _ in range(len(row))])
    for j in range(len(row)):
        if row[j] == 'S':
            S = [i, j]

time = [[0 for _ in range(len(grid[0]))] for __ in range(h+2)]
time[S[0]][S[1]] = 0

flag = [[False for _ in range(len(grid[0]))] for __ in range(h+2)]
flag[S[0]][S[1]] = True

life = 1
queue = deque()
queue.append(S)
while life <= n:
    now = queue.popleft()
    y, x = now[0], now[1]
    if grid[y][x] == str(life):
        saved_time = time[now[0]][now[1]]
        time = [[0 for _ in range(len(grid[0]))] for __ in range(h+2)]
        time[y][x] = saved_time

        flag = [[False for _ in range(len(grid[0]))] for __ in range(h+2)]
        flag[y][x] = True

        queue.clear()
        life += 1
    if life > n:
        print(time[now[0]][now[1]])
        break
    for cell in [[y-1, x], [y, x+1], [y+1, x], [y, x-1]]:
        if flag[cell[0]][cell[1]] == False and grid[cell[0]][cell[1]] != 'X':
            queue.append([cell[0], cell[1]])
            time[cell[0]][cell[1]] += time[y][x] + 1
            flag[cell[0]][cell[1]] = True




# ====================できたコード====================
# h, w, n = map(int, input().split())

# S = [-1, -1]
# grid = []
# for i in range(1, h+1):
#     row = list('X'+input()+'X')
#     if i == 1:
#         grid.append(['X' for _ in range(len(row))])
#     grid.append(row)
#     if i == h:
#         grid.append(['X' for _ in range(len(row))])
#     for j in range(len(row)):
#         if row[j] == 'S':
#             S = [i, j]

# time = [[0 for _ in range(len(grid[0]))] for __ in range(h+2)]
# time[S[0]][S[1]] = 0

# flag = [[False for _ in range(len(grid[0]))] for __ in range(h+2)]
# flag[S[0]][S[1]] = True
# life = 1
# queue = deque()
# queue.append(S)
# while life <= n:
#     now = queue.popleft()
#     y, x = now[0], now[1]
#     if grid[y][x].isdigit():
#         life += 1
#     if life > n:
#         print(time[now[0]][now[1]])
#     for cell in [[y-1, x], [y, x+1], [y+1, x], [y, x-1]]:
#         if flag[cell[0]][cell[1]] == False and grid[cell[0]][cell[1]] != 'X':
#             queue.append([cell[0], cell[1]])
#             time[cell[0]][cell[1]] += time[y][x] + 1
#             flag[cell[0]][cell[1]] = True

# time[S[0]][S[1]] -= 1
# print(time)

