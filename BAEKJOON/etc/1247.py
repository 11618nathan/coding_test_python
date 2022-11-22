from sys import stdin

for i in range(3):
    t = int(stdin.readline())
    sum = 0
    for j in range(t):
        num = int(stdin.readline())
        sum += num
    if sum > 0:
        print('+')
    elif sum == 0:
        print('0')
    else:
        print('-')