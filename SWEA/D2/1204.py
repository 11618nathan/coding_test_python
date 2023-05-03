T = int(input())
for tc in range(1, T+1):
    N = int(input())
    l = list(map(int, input().split()))
    result = 0
    dic = {}
    for i in l:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    max_count = 0
    for key, value in dic.items():
        if max_count < value:
            max_count = value
            result = key
        elif max_count == value:
            if result < key:
                result = key
    print('#%d %d' %(tc, result))