T = int(input())
for i in range(1, T+1):
    n, s, e, k = map(int, input().split())
    nums = list(map(int, input().split()))
    m = nums[s-1:e]
    m.sort()
    print('#%d %d' %(i, m[k-1]))