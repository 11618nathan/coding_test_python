n = 0
r = 0

for i in range(5):
    n = int(input())
    if (n < 40):
        n = 40
    r = r + n

print(int(r/5))