import sys
input = sys.stdin.readline
n, k = map(int, input().split())
# 약수는 1부터 시작하므로, n까지 
for i in range(1, n+1):
    if n % i == 0:
        k -= 1
    if k == 0:
        print(i)
        break
else:
    print(-1)

###########
cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)