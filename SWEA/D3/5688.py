T = int(input())
for tc in range(1, T+1):
    X = -1
    N = int(input())
    for i in range(1, N+1):
        if i*(i*i) > N:
            break
        if i*(i*i) == N:
            X = i
    print('#%d %d' %(tc, X))