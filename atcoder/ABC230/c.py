# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
5 3 2
1 5 1 5
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())

grid = [['.' for i in range(n)] for i in range(n)]

left_op_1 = max(1-a, 1-b)
right_op_1 = min(n-a, n-b)

op_1 = list(range(left_op_1, right_op_1+1))

left_op_2 = max(1-a, b-n)
right_op_2 = min(n-a, b-1)

op_2 = list(range(left_op_2, right_op_2+1))

for k in op_1:
    grid[a+k-1][b+k-1] = '#'

for k in op_2:
    grid[a+k-1][b-k-1] = '#'

for i in range(q-p+1):
    print(''.join(grid[i]))