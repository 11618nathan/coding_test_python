n = int(input())

for i in range(n):
    sum = 0
    l = list(map(int, input().split()))
    for j in l:
        if ((j % 2) == 1):
            sum += j
    print('#%d %d' % ((i + 1), sum))