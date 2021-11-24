
[n, x] = input().rstrip().split()
[n, x] = [int(n), int(x)]

array = list(map(int, input().split()))

known = [0] * n
known[0] = x
for i in range(1, n):
    known[i] = array[known[i-1]-1]
print(len(set(known)))