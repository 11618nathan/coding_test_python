N = int(input())
l = [list(map(int, input().split())) for _ in range(N)] 
s = N // 2
e = N // 2
result = 0
for i in range(N):
    for j in range(s, e+1):
        result += l[i][j]
    if i < N // 2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(result)