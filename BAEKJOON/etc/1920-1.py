N = int(input())
A = list(map(int, input().split()))
A.sort()
M = int(input())
T_list = list(map(int, input().split()))

for i in range(M):
    find = False
    target = T_list[i]
    s = 0
    e = len(A) - 1
    while s <= e:
        midi = int((s+e)/2)
        midv = A[midi]
        if midv > target:
            e = midi -1
        elif midv < target:
            s = midi + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)