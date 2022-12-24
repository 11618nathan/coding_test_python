s = input()
cout = 1
for i in s:
    print(i, end='')
    if cout % 10 == 0:
        print()
    cout += 1