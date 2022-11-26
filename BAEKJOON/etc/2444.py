n = int(input())
m = n-1

star = '*'
space = ' '

for i in range(n):
    print((space*((n-1)-i))+(star*((2*i)+1)))

for i in range(m):
    print((space*(i+1))+(star*((2*(m-i))-1)))