T = int(input())
for tc in range(T):
    N = int(input())
    if N % 2 == 1:
        print('#%d ' %(tc+1) + 'Bob')
    else:
        print('#%d ' %(tc+1) + 'Alice')