T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    l = [0 for i in range(N)]
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            l[j] = i
    print('#%d' %(tc), end=' ')
    for i in l:
        print(i, end=' ')
    print()