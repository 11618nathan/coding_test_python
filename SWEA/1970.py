t = int(input())

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]


for i in range(t):
    n = int(input())
    result = []
    m = 0
    for j in money:
        m = n // j
        result.append(m)
        n = n - (m * j)
    print('#%d' %(i+1))
    for k in result:
        print(k, end=' ')
    print('')