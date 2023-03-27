n = int(input())
m = n - 1

star = '*'
space = '_'

for i in range(n):
    print(star*(i+1))
for i in range(m):
    print(star*(m-i))