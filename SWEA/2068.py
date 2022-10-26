t = int(input())

for i in range(t):
	m = 0
	l = list(map(int, input().split()))
	m = max(l)
print('#%d %d' %((i+1), m))