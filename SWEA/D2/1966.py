T = int(input())
for tc in range(T):
    N = int(input())
    l = list(map(int, input().split()))
    l.sort()
    print('#%d' %(tc+1), end=' ')
    for i in l:
        print(i, end=' ')
    print()