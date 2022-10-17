from collections import deque

n, l = map(int, input().split())
dq = deque()

now = list(map(int, input().split()))

for i in range(n):
	while dq and ad[-1][0] > now[i]:
		dq.pop()
	dq.append((now[i], i))
	if dq[0][1] <= i - l:
		dq.popleft()
	print(dq[0][0], end='')