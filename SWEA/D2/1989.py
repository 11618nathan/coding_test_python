T = int(input())
for i in range(T):
    s = input()
    s_r = s[::-1]
    if s == s_r:
        print('#%d 1' %(i+1))
    else:
        print('#%d 0' %(i+1))