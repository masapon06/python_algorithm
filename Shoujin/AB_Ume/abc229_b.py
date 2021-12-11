num1, num2 = map(str, input().split())

zero_num = max(len(num1), len(num2)) - min(len(num1), len(num2))

if len(num1) > len(num2):
  num2 = '0'*zero_num + num2
if len(num2) > len(num1):
  num1 = '0'*zero_num + num1

flag = False
for i in range(len(num1)):
  if int(num1[i]) + int(num2[i]) >= 10:
    flag = True

if flag:
  print('Hard')
else:
  print('Easy')