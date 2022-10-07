t = input()
t = int(t)

r = t + 1

m = 0
a = 0
b = 0
sum = [0 for i in range(0, r)]

for i in range(0, t):
  a, b = input().split()
  a = int(a)
  b = int(b)
  m = a + b
  sum[i] = m

for i in range(0, t):
  print("Case #%d: %d" %(i+1, sum[i]))