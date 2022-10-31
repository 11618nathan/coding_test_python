t = int(input())

for i in range(t):
    n = int(input())
    str_arr = []
    cout = 1
    for j in range(n):
        str, num = input().split()
        num = int(num)
        for k in range(num):
            str_arr.append(str)
    print('#%d' %(i+1))
    for j in str_arr:
        if ((cout % 10) == 0):
            print(j)
            cout += 1
        else:
            print(j, end='')
            cout += 1
    print('')