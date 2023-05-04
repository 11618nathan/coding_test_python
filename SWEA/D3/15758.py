T = int(input())
for tc in range(T):
    S, T = input().split()
    s_len = len(S)
    t_len = len(T)
    if S * t_len == T * s_len:
        print('#%d ' %(tc+1) +'yes')
    else:
        print('#%d ' %(tc+1) +'no')