n = set(range(1, 10001))
r = set()

for i in range(1, 10001):
    for j in str(i):
        i = i + int(j)
    r.add(i)

s = sorted(n - r)
for i in s:
    print(i)