T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    result = [ i for i in range(1, N+1)]
    l_k = list(map(int, input().split()))
    for i in range(1, N+1):
        if i in l_k:
            result.remove(i)
    print('#%d' %(tc+1 ), end=' ')
    for i in result:
        print(i, end=' ')
    print()