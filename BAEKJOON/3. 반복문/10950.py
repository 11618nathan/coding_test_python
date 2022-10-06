case_num = input()
case_num = int(case_num)
r1 = case_num + 1
r1 = int(r1)

sum = [0 for i in range(0, r1)]

for i in range(0, case_num):
  x, y = input().split()
  x = int(x)
  y = int(y)
  m = x + y
  sum[i] = m

for i in range(0, r1-1):
  print(sum[i])