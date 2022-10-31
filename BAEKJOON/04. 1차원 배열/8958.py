num = int(input())

for i in range(num):
    s = list(input())
    sum = 0
    cot = 1
    for i in s:
        if (i == 'O'):
            sum = sum + cot
            cot = cot + 1
        else:
            cot = 1
    print(sum)