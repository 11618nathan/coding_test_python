T = int(input())
for tc in range(T):
    N = int(input())
    if N % 2 == 0:
        print('#%d Even' %(tc+1))
    else:
        print('#%d Odd' %(tc+1))