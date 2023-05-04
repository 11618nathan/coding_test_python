T = int(input())
for tc in range(T):
    N, K =map(int, input().split())
    l = [list(map(int, input().split())) for i in range(N)]
    result = 0
    for col in range(N):
        cout = 0
        for row in range(N):
            if l[col][row] == 1:
                cout += 1
            if (l[col][row] == 0) or (row == N-1):
                if cout == K:
                    result += 1
                cout = 0
        for row in range(N):
            if l[row][col] == 1:
                cout += 1
            if l[row][col] == 0 or row == N-1:
                if cout == K:
                    result += 1
                cout = 0
    print("#%d %d" %((tc+1), result))