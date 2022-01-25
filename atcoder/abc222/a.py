# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
4 50
80 60 40 0
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

n = input()

length = len(n)

print('0'*(4 - length)+n)
