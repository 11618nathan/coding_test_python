n = int(input())

for i in range(n):
    i = i + 1
    if i == 1:
        print(1, end=' ')
    else:
        m = n % i
        if m == 0:
            print(i, end=' ')