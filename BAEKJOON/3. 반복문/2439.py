n = int(input())

s1 = " "
s2 = "*"
r = n

for i in range(n):
    i += 1
    n -= 1
    print(s1 * n, end='')
    print(s2 * i)