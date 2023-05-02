a = [list(map(int, input().split())) for _ in range(7)]

result = 0
for i in range(3): 
    for j in range(7):
        tmp = a[j][i:i+5]
        if tmp == tmp[::-1]:
            result += 1
        for k in range(2):
            if a[i+k][j] != a[i+5-k-1][j]:
                break
        else:
            result += 1

print(result)      