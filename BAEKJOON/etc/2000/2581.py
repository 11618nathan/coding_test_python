M = int(input())
N = int(input())
result = []
for i in range(M, N+1):
    for j in range(2, i+1):
        if i == j:
            result.append(i)
        if i % j == 0:
            break
if not result:
    print(-1)
else:
    print(sum(result))
    print(result[0])