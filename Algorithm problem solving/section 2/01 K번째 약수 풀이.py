# 띄어쓰기 입력구분 - map(), split()
N, K = map(int, input().split())
cnt = 0
for i in range(1, N+1):
    if n%i == 0:
        cnt += 1
    if cnt == k:
        print(i)
        break
else:
    print(-1)