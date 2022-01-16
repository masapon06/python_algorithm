
n = 5

# {0, 1, ..., n-1} の部分集合の全探索
for bit in range(1<<n):
    # bit で表される集合の処理を書く

    # きちんとできていることを確認してみる
    # bit の表す集合を求める
    S = []
    for i in range(n):
        if (bit & (1<<i)): # i が bit に入るかどうか
        # if ((bit >> j) & 1): とも書ける
            S.append(i)

    # bit の表す集合の出力
    print(": {", end="")
    for i in range(len(S)):
        print(S[i], " ", end="")
    print("}", "\n")