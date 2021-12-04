# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
xoxxoxx
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================


s = input()
replaced_s = s.replace('oxx', '')

t = 'xxox'

flag = False

# if len(replaced_s) == 0:
#     flag = True

for i in range(5):
    for j in range(5):
        if i > j:
            continue
        print(i, j, t[i:j])
#         if replaced_s == t[i:j]:
#             flag = True
# if flag == True:
#     print('Yes')
# else:
#     print('No')



# =================================================

# s = input()

# t = "oxx" * 10 ** 5

# flag = False
# for i in range(10 ** 5):
#     for j in range(10 ** 5):
#         if i > j:
#             continue
#         if s == t[i:j]:
#             flag = True

# if flag == True:
#     print('Yes')
# else:
#     print('No')
