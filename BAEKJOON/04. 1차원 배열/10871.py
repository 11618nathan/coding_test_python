n, x = map(int, input().split())

l = [0 for i in range(n)] 

l = list(map(int, input().split()))

for i in range(n):
    if (x > l[i]):
        print(l[i], end=' ')