c = int(input())

for i in range(c):
    l = list(map(int, input().split()))
    avg = sum(l[1:])/l[0]
    cot = 0
    rat = 0
    for j in l[1:]:
        if (avg < j):
            cot = cot + 1
        rat = (cot / l[0]) * 100
    print(f'{rat:.3f}%')