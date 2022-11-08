t = int(input())

for i in range(t):
    cycle = int(input())
    result = []
    temp = []
    print('#%d' %(i+1))
    for j in range(cycle):
        result.append(1)
        temp.append(1)
        if j < 2:
            pass
        else:
            for k in range(1, len(result)-1):
                temp[k] = result[k-1] + result[k]
        for k in range(len(result)):
            result[k] = temp[k]
            print(str(result[k]) + " ", end="")
        print("")