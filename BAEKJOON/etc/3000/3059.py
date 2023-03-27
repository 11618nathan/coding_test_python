n = int(input())

alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in range(n):
    l = list(input())
    sum = 0
    for j in alpha:
        if (j not in l): 
            sum = sum + ord(j)
        else: 
            continue
    print(sum)