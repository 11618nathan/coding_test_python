N = int(input())
K = int(input())

s = 1
e = K
ans = 0

while s <= e:
    mid = int((s + e) // 2)
    cnt = 0
    for i in range(1, N+1):
        cnt += min(int(mid / i), N)
    if cnt < K:
        s = mid + 1
    else:
        ans = mid
        e = mid -1

print(ans)