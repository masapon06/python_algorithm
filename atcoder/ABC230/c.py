# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
1000000000000000000 999999999999999999 999999999999999999
999999999999999998 1000000000000000000 999999999999999998 1000000000000000000
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())

left_op_1 = max(1-a, 1-b)
right_op_1 = min(n-a, n-b)

left_op_2 = max(1-a, b-n)
right_op_2 = min(n-a, b-1)
print(left_op_1, right_op_2, left_op_2, right_op_2)

# ans_grid = [['.']*(s-r+1) for i in range(q-p+1)]

for k in range(left_op_1, right_op_1+1):
    if a+k >= p and a+k <= q and b+k >= r and b+k <= s:
        # ans_grid[a+k -p][b+k - r] = '#'
        print(k)

for k in range(left_op_2, right_op_2+1):
    if a+k >= p and a+k <= q and b-k >= r and b-k <= s:
        # ans_grid[a+k -p][b-k -r] = '#'
        print(k)

# for i in range(q-p+1):
#     print(''.join(ans_grid[i]))