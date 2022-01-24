[n, a, b] = input().strip().split()
[n, a, b] = [int(n), int(a), int(b)]

ans = 0
for i in range(1, n):
    calc = 0
    num = i
    for j in range(5):
        calc += num % 10
        num = (num - num % 10) / 10
        if num == 0:
            if calc >= a and calc <= b:
                ans += calc
            break
print(ans)