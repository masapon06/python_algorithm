# # ===================デバッグ用入力===================
# import io
# import sys

# _INPUT = """\

# """
# sys.stdin = io.StringIO(_INPUT)
# # ====================ここから入力====================

def fibonacci0(n):
    if n < 2:
        return n
    return fibonacci0(n - 1) + fibonacci0(n - 2)

print(fibonacci0(5))