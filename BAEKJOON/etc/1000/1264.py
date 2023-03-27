while 1:
    s = input()
    if s == '#':
        break
    cout = 0
    for c in s:
        if c in 'aeiouAEIOU':
            cout += 1
    print(cout)