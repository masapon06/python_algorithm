# ===================入力===================
import io
import sys

_INPUT = """\
999
"""
sys.stdin = io.StringIO(_INPUT)
# ====================コード====================

s = input()

abc = s[0]+s[1]+s[2]
bca = s[1]+s[2]+s[0]
cab = s[2]+s[0]+s[1]
print(int(abc)+int(bca)+int(cab))