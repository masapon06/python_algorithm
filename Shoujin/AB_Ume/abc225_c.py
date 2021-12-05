# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
2 3
1 2 3
8 9 10
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

n, m = map(int, input().split())

B = []
for _ in range(n):
    B.append(list(map(int, input().split())))

flag = 0
y_zero = int((B[0][0] - (B[0][0] % 7)) / 7 + 1) - 1
x_zero = int(B[0][0] % 7) - 1
for i in range(n):
    for j in range(m):
        now = B[i][j]
        y = y_zero + i
        x = x_zero + j

        if now == (y)*7 +x+1:
            flag += 1
        # score = 0
        # # 上
        # if i != 0:
        #     if B[i-1][j] == now - 7:
        #         score += 1
        # else:
        #     score += 1
        
        # # 右
        # if j != m-1:
        #     if B[i][j+1] == now + 1:
        #         score += 1
        # else:
        #     score += 1
        
        # # 下
        # if i != n-1:
        #     if B[i+1][j] == now + 7:
        #         score += 1
        # else:
        #     score += 1
        
        # # 左
        # if j != 0:
        #     if B[i][j-1] == now - 1:
        #         score += 1
        # else:
        #     score += 1
        
        # if score == 4:
        #     flag += 1

if flag == n*m:
    print('Yes')
else:
    print('No')