
# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
2
1 2 3
aaa
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

s = input()
s = s[::-1]

array = ['dream', 'dreamer', 'erase', 'eraser']
for i in range(4):
    array[i] = array[i][::-1]

index = 0
can = True
for i in range(len(s)):
    can_divide = False
    for j in range(4):
        if s[index:index + len(array[j])] == array[j]:
            index += len(array[j])
            can_divide = True
            break
        else:
            can_divide = False
    if can_divide == False:
        can = False
        break
    if index >= len(s):
        break
if can == True:
    print("Yes")
else:
    print("No")