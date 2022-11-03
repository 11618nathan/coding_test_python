tc =  int(input())

for i in range(tc):
    cout = 0
    n = int(input())
    for j in range(1, 10):
        if (n % j) == 0:
            if (n // j) < 10:
                cout += 1
            else:
                pass
    if cout > 0:
        print('#%d Yes' %(i+1))
    else:
        print('#%d No' %(i+1))