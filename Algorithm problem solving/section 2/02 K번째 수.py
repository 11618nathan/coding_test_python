T = int(input())
for i in range(T):
    N, s, e, k = map(int, input().split())
    num = list(map(int, input().split()))
    result = sorted(num[s-1:e])
    print('#%d %d' %(i+1, result[k-1]))
    '''
    num=num[s-1:e]
    num.sort()
    '''