n = int(input())
m = n - 1

star = '*'
space = ' '

for i in range(n):
    print((space*i)+(star*(2*(n-i)-1)))

for i in range(m):
    print((space*((m-i)-1))+(star*(2*(i+2)-1)))