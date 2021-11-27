[n, x] = list(map(int, input().split()))
array = [0, * list(map(int, input().split()))]

bool_arr = [False] * (n+1)
for sim in range(n+1):
    if sim == 0:
        i = x
    else:
        i = array[i]
    if bool_arr[i] == True:
        break
    else:
        bool_arr[i] = True
count = 0   
for i in range(len(bool_arr)):
    if bool_arr[i] == True:
        count += 1
print(count)