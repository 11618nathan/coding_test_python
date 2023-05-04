t = int(input())

one = [1, 3, 5, 7, 8, 10, 12]
zero = [4, 6, 9, 11]

for i in range(t):
    n  = input()
    y = n[0:4]
    m = n[4:6]
    d = n[6:]
    result = y+'/'+m+'/'+d
    if (int(m) > 12):
        result = -1
    elif (int(m) < 1):
        result = -1
    elif (int(m) == 2):
        if (int(d) > 29):
            result = -1
    elif (int(m) in one):
        if (int(d) > 32):
            result = -1
    elif (int(m) in zero):
        if (int(d) > 31):
            result = -1
    else:
        pass
    print('#%d %s' %((i+1), result))