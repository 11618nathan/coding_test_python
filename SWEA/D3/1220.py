for tc in range(10):
    N = int(input())
    l = [list(map(int, input().split())) for i in range(N)]
    result = 0
    for i in range(N):
        cout = 0
        for j in range(N):
            if l[j][i] == 1:
                cout = 1
            if l[j][i] == 2:
                if cout == 1:
                    result += 1
                    cout = 0
    print('#%d %d' %((tc+1), result))