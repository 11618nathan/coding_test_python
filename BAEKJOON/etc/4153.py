while(1):
    num = map(int, input().split())
    l = sorted(num)
    if (l[0]==0) and (l[1]==0) and (l[2]==0):
        break
    elif (l[0]**2+l[1]**2) == (l[2]**2):
        print("right")
    else:
        print("wrong")