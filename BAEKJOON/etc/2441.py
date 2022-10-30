n = int(input())

for i in range(n):
    k = n - i
    star = '*'
    space = ' '
    if i > 0:
        print(space*i, end = '')
    print(star*k)