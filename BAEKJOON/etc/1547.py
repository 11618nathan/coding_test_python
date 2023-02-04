m = int(input())
C = [0,1,2,3]
for _ in range(m):
    x, y = map(int, input().split())
    C[x], C[y] = C[y], C[x]
print(C.index(1))