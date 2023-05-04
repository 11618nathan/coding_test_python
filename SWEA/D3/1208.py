for tc in range(10):
    dump = int(input())
    l = list(map(int, input().split()))
    for i in range(dump):
        l_max = max(l)
        l_min = min(l)
        l_max_index = l.index(l_max)
        l_min_index = l.index(l_min)
        l[l_max_index] -= 1
        l[l_min_index] += 1
    print('#%d %d' %((tc+1), max(l)-min(l)))