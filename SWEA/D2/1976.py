t = int(input())

for i in range(t):
    h1, m1, h2, m2 = map(int, input().split())
    rh = h1 + h2
    rm = m1 + m2
    if rm > 59:
        rm = abs(rm - 60)
        rh += 1
    if rh > 12:
        rh = abs(rh - 12)
    print('#%d %d %d' %((i+1), rh, rm))