s ='#'
p = '+'

for i in range(5):
    cout = 0
    for j in range(5):
        if cout == i:
            print(s, end='')
        else:
            print(p, end='')
        cout += 1
    print('')