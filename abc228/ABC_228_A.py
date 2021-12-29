[s, t, x] = input().strip().split()
[s, t, x] = [int(s), int(t), int(x)]

if x >= s and x < t:
    print('Yes')
elif s > t:
    if (s <= x and x <= 23) or (x < t):
        print('Yes')
    else:
        print('No')
else:
    print('No')


# S=7, T=20, X=12
# xがsより大きいかつ、xがtより小さい　→ yes

# 例外　s>tのとき
# s=23, t=4, x=3
# s <= x and x =< t → yes

# s=23, t=0, x=23

# s=23, t=1, x=23