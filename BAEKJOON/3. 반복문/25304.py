sum = input()
sum = int(sum)
item_sum = input()
item_sum = int(item_sum)

r = item_sum + 1
x = 0
y = 0
count = 0

for i in range(1, r):
  x, y = input().split()
  x = int(x)
  y = int(y)
  count = count + (x*y)

if (sum == count):
  print("Yes")
else :
  print("No")