n = int(input())
l = [0 for i in range(n)]
l = list(map(int, input().split()))

r = 0
c = 0
m = max(l)

for i in range(n):
    r = (l[i] / m) * 100
    c = c + r
print(c/n)