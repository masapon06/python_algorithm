# ===================デバッグ用入力===================
import io
import sys

_INPUT = """\
2 3
GCP
PPP
CCC
PPC
"""
sys.stdin = io.StringIO(_INPUT)
# ====================ここから入力====================

def janken(me, opposite):
    if me == opposite:
        return 'DRAW'
    if me == 'G':
        if opposite == 'C':
            return 'WIN'
        if opposite == 'P':
            return 'LOSE'
    if me == 'C':
        if opposite == 'G':
            return 'LOSE'
        if opposite == 'P':
            return 'WIN'
    if me == 'P':
        if opposite == 'G':
            return 'WIN'
        if opposite == 'C':
            return 'LOSE'

n, m = map(int, input().split())

sight = ['X'*(m+1)]
for i in range(2*n):
    sight.append('X'+input())

win = [-1]
for _ in range(2*n):
    win.append(0)

rank = [-1 for _ in range(2*n+1)]
for round in range(1, m+2):
    # rank決定
    now_rank = 1
    for win_count in range(round)[::-1]:
        sames = [i for i, x in enumerate(win) if x == win_count]
        for people in sames:
            rank[now_rank] = people
            now_rank += 1
    if round == m+1:
        for i in range(1, 2*n+1):
            print(rank[i])
        break

    # 対戦相手決定
    battle_list = []
    for k in range(1, n+1):
        a = rank[2*k-1]
        b = rank[2*k]
        battle_list.append([a, b])

    for battle in battle_list:
        result = janken(sight[battle[0]][round], sight[battle[1]][round])
        if result == 'WIN':
            win[battle[0]] += 1
        elif result == 'LOSE':
            win[battle[1]] += 1