# ===================入力===================
import io
import sys

_INPUT = """\
"""
sys.stdin = io.StringIO(_INPUT)
# ====================コード====================

data = {}

data[1] = []
data[1].append(2)
print(data)

data[2] = [3, 4]
data[2].append(5)
print(data)
