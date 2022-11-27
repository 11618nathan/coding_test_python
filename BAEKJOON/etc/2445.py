n = int(input())
m = n - 1

star = '*'
space = ' '

for i in range(n):
    print((star*(i+1))+(space*(2*(n-(i+1))))+(star*(i+1)))

for i in range(m):
    print((star*(m-i))+(space*(2*(i+1)))+(star*(m-i)))