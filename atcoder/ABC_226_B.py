from itertools import combinations

n = int(input())

L = []
a = []
for i in range(n):
    Li = list(map(int,input().split()))
    L.append(Li[0])
    a.append(Li[1:])

list=[]
for i in range(n):
    list.append(i)

ans = n
com=combinations(list,2)
for patern in com:
    count = 0
    for i in range(L[patern[0]]):
        if L[patern[0]] == L[patern[1]]:
            if a[patern[0]][i] == a[patern[1]][i]:
                count += 1
            else:
                break
    else:
        break
    if count == L[max(patern)]:
        ans -= 1
print(ans)
