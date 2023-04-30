N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]
max = 0
for i in range(N):
    sum1, sum2 = 0, 0
    for j in range(N):
        sum1 += l[i][j]
        sum2 += l[j][i]
    if max < sum1:
        max = sum1
    if max < sum2:
        max = sum2 
sum1, sum2 = 0, 0
for i in range(N):
    sum1 += l[i][i]
    sum2 += l[i][N-i-1]
    if max < sum1:
        max = sum1
    if max < sum2:
        max = sum2
print(max)