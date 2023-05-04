n = int(input())

compare = [3, 6, 9]

for i in range(n):
    cout = 0
    i += 1
    s = []
    for j in str(i):
        s.append(j)
    for k in s:
        if int(k) in compare:
            cout += 1
    if cout > 0:
        print('-'*cout, end=' ')
    else:
        print(i, end=' ')