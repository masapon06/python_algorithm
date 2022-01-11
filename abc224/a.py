# ===================入力===================
import io
import sys

_INPUT = """\
er
"""
sys.stdin = io.StringIO(_INPUT)
# ====================以下コード====================
s = input()

if s[-1] == 'r':
    print('er')
else:
    print('ist')