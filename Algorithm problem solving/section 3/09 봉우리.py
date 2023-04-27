N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]

dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]

l.insert(0, [0]*N)
l.append([0]*N)
for x in l:
    x.insert(0, 0)
    x.append(0)

result = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if all(l[i][j]>l[i+dx[k]][j+dy[k]] for k in range(4)):
            result += 1
print(result)