n = int(input())
r = n
count = 0

while (1):
    x = int(r / 10)
    y = (r % 10)
    z = (x + y) % 10
    r = (y * 10) + z
    count = count + 1
    if (n == r):
        break

print(count)