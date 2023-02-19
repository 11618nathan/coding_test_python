T = int(input())
moneys = [25, 10, 5, 1]
cout = [0] * 4
for i in range(T):
    C = int(input())
    for j in range(len(moneys)):
        cout[j] = C // moneys[j]
        C = C % moneys[j]

    print(' '.join(map(str, cout)))