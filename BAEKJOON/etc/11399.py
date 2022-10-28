n = int(input())
a= list(map(int, input().split()))
s = [0] * n

for i in range(1, n):
    insert_p = i
    insert_v = a[i]
    for j in range(i-1, -1, -1):
        if a[j] < a[i]:
            insert_p = j + 1
            break
        if j == 0:
            insert_p = 0
    for j in range(i, insert_p, -1):
        a[j] = a[j-1]
    a[insert_p] = insert_v

s[0] = a[0]

for i in range(1, n):
    s[i] = s[i-1] + a[i]

sum = 0

for i in range(0, n):
    sum += s[i]

print(sum)