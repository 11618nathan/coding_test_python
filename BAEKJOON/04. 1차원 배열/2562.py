n = 9
l = [0 for i in range(9)]
for i in range(9):
    l[i] = int(input())
m = max(l)
print(m)
for i in range(9):
    if (m == l[i]):
        print(i+1)