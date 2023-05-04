tc = int(input())

for i in range(tc):
    s = list(input())
    se = set(s)
    str1 = s[0]
    str2 = []
    cout = 0
    cout1 = 0
    cout2 = 0
    for j in s:
        if j == str1:
            cout1 += 1
        elif j != str1:
            if j == str2:
                cout2 += 1
            else:
                str2.append(j)
                cout2 += 1
        elif j == str2[0]:
            cout2 += 1
        else:
            pass
    
    if len(se) > 2:
        print('#%d No' %(i+1))
    elif (cout1 == 2) and (cout2 == 2):
        print('#%d Yes' %(i+1))
    else:
        print('#%d No' %(i+1))    