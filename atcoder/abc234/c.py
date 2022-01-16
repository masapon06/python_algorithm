# ===================入力===================
import io
import sys

_INPUT = """\
923423423420220108
"""
sys.stdin = io.StringIO(_INPUT)
# ====================以下コード====================
k = int(input())

print(bin(k)[2:].replace('1', '2'))
