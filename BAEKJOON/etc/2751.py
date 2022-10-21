n = int(input())

l = [0 for i in range(n)]

for i in range(n):
    l[i] = int(input())

l.sort()

for i in range(n):
    print(l[i])