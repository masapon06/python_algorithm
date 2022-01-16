# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
50
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

n = input()

if int(n) >= 42:
    n = str(int(n)+1)

if len(n) == 1 or len(n) == 2:
    for i in range(3 - int(len(n))):
        n = '0'+n
    print('AGC'+n)
else:
    print('AGC'+n)