# ===================入力===================
import io
import sys

_INPUT = """\
5
"""
sys.stdin = io.StringIO(_INPUT)
# ====================以下コード====================


# === WAが混ざる。 url: https://atcoder.jp/contests/abc216/submissions/28374176 ===
# n = int(input())
# num = n

# s = ''
# for i in range(120):
#     if num == 0:
#         print(s[::-1])
#         break
#     if num % 2 == 0:
#         s += 'B'
#         num = num // 2
#     else:
#         s += 'A'
#         num -= 1

# ========================================