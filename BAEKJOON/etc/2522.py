n = int(input())
m = n - 1

star = '*'
space = ' '

for i in range(n):
    print((space*((n-i)-1))+(star*(i+1)))

for i in range(m):
    print((space*(i+1))+(star*(m-i)))