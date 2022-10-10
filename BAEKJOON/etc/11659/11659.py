import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = list(map(int, input().split()))
r = [0]
temp = 0

for i in l:
    temp = temp + i
    r.append(temp)

for i in range(m):
    x, y = map(int, input().split())
    print(r[y] - r[x-1])