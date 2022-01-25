# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

n, p = map(int, input().split())

a = list(map(int, input().split()))

count = 0
for score in a:
    if score < p:
        count += 1

print(count)