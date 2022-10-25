t = int(input())

for i in range(t):
    l = list(map(int, input().split()))
    sum = 0
    n = len(l)
    for j in l:
        sum += j
    avg = round(sum / n)
    print('#%d %d' % ((i+1), avg))