n = int(input())
body = []
for i in range(n):
    t, w = map(int, input().split())
    body.append((t, w))
body.sort(reverse=True)
largest = 0
cnt = 0
for x, y in body:
    if y>largest:
        largest = y
        cnt += 1
print(cnt)