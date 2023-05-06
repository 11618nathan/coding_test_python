n = int(input())
m = []
for nc in range(n):
    s, e = map(int, input().split())
    m.append((s, e))
m.sort(key=lambda x : (x[1], x[0]))
et = 0
cnt = 0
for s, e in m:
    if s >= et:
        et = e
        cnt += 1
print(cnt)