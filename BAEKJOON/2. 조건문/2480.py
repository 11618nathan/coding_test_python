a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
r = 0

if (a == b and b == c and c == a):
  r = 10000 + (a * 1000)
  print(r)
elif ((a == b) and (b != c) and (c != a)):
  r = 1000 + (a * 100)
  print(r)
elif ((a != b) and (b == c) and (c != a)):
  r = 1000 + (b * 100)
  print(r)
elif ((a != b) and (b != c) and (c == a)):
  r = 1000 + (c * 100)
  print(r)
else:
  r = max(a, b, c)
  print(r * 100)