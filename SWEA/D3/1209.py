for tc in range(10):
    T = int(input())
    l = [list(map(int, input().split())) for i in range(100)]
    max = 0
    for i in range(100):
        s = 0
        for j in range(100):
            s += l[i][j]
        if max < s:
            max = s
    for i in range(100):
        s = 0
        for j in range(100):
            s += l[j][i]
        if max < s:
            max = s
    for i in range(100):
        s = 0
        s += l[i][i]
        if max < s:
            max = s
    for i in range(100):
        s = 0
        s += l[i][99-i]
        if max < s:
            max = s
    print('#%d %d' %((tc+1), max))