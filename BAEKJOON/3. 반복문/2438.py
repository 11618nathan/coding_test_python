n = input()
n = int(n)
r = 0

for i in range(0, n):
  r = i + 1
  for j in range(0, r):
    print("*", end='')
  print()