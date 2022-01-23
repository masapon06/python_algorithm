# ===================入力===================
import io
import sys

_INPUT = """\
2
4 0 1
5 3
2
"""
sys.stdin = io.StringIO(_INPUT)
# ====================コード====================
import itertools

n = int(input())
people = [i for i in range(2*n)]

a = []

length = 0
for i in range(2*n-1):
    for num in list(map(int, input().split())):
        a.append(num)
        length += 1

all = list(itertools.combinations(a, n))

max = 0
for x in all:
    now_max = 0
    for num in x:
        now_max ^= num
    if now_max > max:
        max = now_max

print(max)
