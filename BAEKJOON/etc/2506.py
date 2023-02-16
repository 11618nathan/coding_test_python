N = int(input())
score = list(map(int, input().split()))
result = 0
buf = 0
for i in score:
    if i == 1:
        buf += 1
        result += buf
    else:
        buf = 0
print(result)