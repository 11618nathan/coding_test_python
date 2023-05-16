N, M = map(int, input().split())
A = list(map(int, input().split()))
s = 0
e = 0

for i in A:
    if s < i:
        s = i
    e += i

while s <= e:
    mid = int((s+e)/2)
    sum = 0
    cout = 0
    for i in range(N):
        if sum + A[i] > mid:
            cout += 1
            sum = 0
        sum += A[i]
    if sum != 0:
        cout += 1
    if cout > M:
        s = mid + 1
    else:
        e = mid - 1

print(s)