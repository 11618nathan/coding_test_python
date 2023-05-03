T = int(input())
for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    B = Q
    if R < W:
        B = Q + ((W-R) * S)
    result = min(A, B)
    print('#%d %d' %(tc, result))