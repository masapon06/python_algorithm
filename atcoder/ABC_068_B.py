
# コンテスト時間: 2017-07-29(土) 21:00 ~ 2017-07-29(土) 22:40 (100分)
# 16:55開始

N = int(input())

ans_count = 0
ans = 1
for i in range(N):
    num = N - i
    count = 0
    for j in range(10):
        if num % 2 == 0:
            count += 1
            num = num / 2
        else:
            break
    if ans_count < count:
        ans_count = count
        ans = N - i

print(ans)