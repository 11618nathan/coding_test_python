n = int(input())
l = [0 for i in range(n)]

for i in range(n):
  x, y = map(int, input().split())
  print("Case #%d: %d + %d = %d" %(i+1, x, y, (x + y)))