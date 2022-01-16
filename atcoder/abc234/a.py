# ===================入力===================
import io
import sys

_INPUT = """\
10
"""
sys.stdin = io.StringIO(_INPUT)
# ====================以下コード====================
t = int(input())

def f(x):
    return x**2 + 2*x + 3

print(f(f(f(t)+t)+f(f(t))))