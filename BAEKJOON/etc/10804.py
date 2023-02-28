num = [i for i in range(21)]
for _ in range(10):
    s, e = map(int, input().split())
    num[s:e + 1] = num[e:s - 1:-1]
for i in range(1, 21):
    print(num[i], end=' ')