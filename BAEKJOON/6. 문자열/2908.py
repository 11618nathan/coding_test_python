x, y = input().split()

x = int(x[::-1])
y = int(y[::-1])

if (x < y):
    print(y)
else:
    print(x)