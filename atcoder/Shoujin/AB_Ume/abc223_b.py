# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
z
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================
s = input()

str_list = [s]
 
for i in range(len(s)-1):
    st = str_list[i][1:]+str_list[i][0]
    str_list.append(st)

# 以下pythonで文字"列"の大小を比較する手段がないことを前提として解いていく。
# 文字の大小比較はできることとする。
min_str_list = str_list
min_char = ['z'*1001] # どんな文字が来ても絶対その文字より小さくなるような数で初期化
# 最小を探索して出力
for i in range(len(s)):
    min_char = [min_char[0]] # 初期化
    for string in min_str_list:
        if min_char[0][i] > string[i]:
            min_char = []
            min_char.append(string)
        elif min_char[0][i] == string[i]:
            if min_char[0] != string:
                if i == 0 and string == str_list[0]:
                    min_char[0] = string
                else:
                    min_char.append(string)
    
    if len(min_char) == 1:
        print(min_char[0])
        break

    if i == len(s)-1:
        print(min_char[0])
    min_str_list = min_char

max_char = ['a'] # どんな文字が来ても絶対その文字より大きくなるような数で初期化
max_str_list = str_list
# 最大を探索して出力
for i in range(len(s)):
    max_char = [max_char[0]] # 初期化
    for string in max_str_list:
        if max_char[0][i] < string[i]:
            max_char = []
            max_char.append(string)
        elif max_char[0][i] == string[i]:
            max_char.append(string)
            if max_char[0] != string:
                max_char.append(string)
    if len(max_char) == 1:
        print(max_char[0])
        break

    if i == len(s)-1:
        print(max_char[0])
    max_str_list = max_char