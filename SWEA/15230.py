n = int(input())
l = [0 for i in range(n)]

for i in range(n):
    l = input()
    cout = 1
    m = ord(l[0])
    if (l[0] == 'a'):
        for j in l:
            r = ord(j)-1
            if (m == r):
                m = ord(j)
                cout += 1
            else :
                m = ord('a')
    else:
        cout = 0
          
    print("#%d %d" % (i+1, cout))