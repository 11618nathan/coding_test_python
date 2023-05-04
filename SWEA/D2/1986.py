T = int(input())
for i in range(T):
    N = int(input())
    s = 0
    for j in range(1, N+1):
        if j % 2 == 1:
            s += j
        else:
            s -= j
    print('#%d %d' %((i+1), s))