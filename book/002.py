import sys
input = sys.stdin.readline
n, m = map(int, input().split())
l = list(map(int, input().split()))
s = 0
r = [0]
for i in l:
    s = s + i
    r.append(s)
for _ in range(m):
    i, j = map(int, input().split())
    print(r[j]-r[i-1])