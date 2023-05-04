t = int(input())

for i in range(t):
    l = list(map(int, input().split()))
    sum = 0
    m = max(l)
    n = min(l)
    l.remove(m)
    l.remove(n)
    for j in l:
        sum += j
    r = int(round(sum / len(l)))
    print('#%d %d' %((i+1), r))