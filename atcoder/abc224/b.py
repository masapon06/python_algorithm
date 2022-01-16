# ===================入力===================
import io
import sys

_INPUT = """\
2 4
4 3 2 1
5 6 7 8
"""
sys.stdin = io.StringIO(_INPUT)
# ====================以下コード====================
import itertools

h, w = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]

h_all = list(range(0, h))
w_all = list(range(0, w))

h_combinations = list(itertools.combinations(h_all, 2))
w_combinations = list(itertools.combinations(w_all, 2))

count = 0
score = 0

for i in range(len(h_combinations)):
    for j in range(len(w_combinations)):
        count += 1

        i1 = h_combinations[i][0]
        i2 = h_combinations[i][1]
        j1 = w_combinations[j][0]
        j2 = w_combinations[j][1]

        if grid[i1][j1] + grid[i2][j2] <= grid[i2][j1] + grid[i1][j2]:
            score += 1
if count == score:
    print('Yes')
else:
    print('No')

