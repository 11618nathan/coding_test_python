t = int(input())

for i in range(t):
    l = list(input())
    temp = 97
    cout = 0
    for j in l:
        if cout < 27:
            if ord(j) == temp:
                cout += 1
                temp += 1
            else :
                break
        else:
            break
    print('#%d %d' %((i+1), cout))