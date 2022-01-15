# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
1 2 3
4 5 6
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================
import bisect

data = {
    1: [1, 2],
    2: [3, 4],
}
data[1].append(3)
print(data[1])