c = []
for _ in range(8):
    c.append(list(map(str, list(input()))))
r = 0
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            if c[i][j] == 'F':
                r += 1
print(r)