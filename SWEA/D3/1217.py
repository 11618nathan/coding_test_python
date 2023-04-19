def mul(N, M):
    if M < 2:
        return N
    else:
        return N * mul(N, M-1)
for tc in range(10):
    T = int(input())
    N, M = map(int, input().split())
    print('#%d %d' %((tc+1), mul(N, M)))