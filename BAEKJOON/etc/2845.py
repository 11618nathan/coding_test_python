a, b = map(int, input().split())
per = list(map(int, input().split()))
p = a * b
for i in per:
    print(i - p, end=' ')