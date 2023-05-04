t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    if a < 10 and b < 10:
        print('#%d %d' %((i+1), a*b))
    else:
        print('#%d -1' %((i+1)))