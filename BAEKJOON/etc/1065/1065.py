n = int(input())

def s(n):
    c = 0
    for i in range(1, n + 1):
        l = list(map(int, str(i)))
        if (i < 100):
            c = c + 1
        elif l[0] - l[1] == l[1]-l[2]:
            c = c + 1
    return c

print(s(n))