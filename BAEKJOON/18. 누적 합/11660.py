import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [[0] * (n + 1)]
r = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n):
    lr = [0] + [int(x) for x in input().split()]
    l.append(lr)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        r[i][j] = r[i][j - 1] + r[i - 1][j] - r[i - 1][j - 1] + l[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = r[x2][y2] - r[x1-1][y2] - r[x2][y1-1] + r[x1-1][y1 -1]
    print(result)