n = int(input())
ans = [0] * n
a = list(map(int, input().split()))
s = []

for i in range(n):
	while s and a[s[-1]] < a[i]:
		ans[s.pop()] = a[i]
	s.append(i)
	
while s:
	ans[s.pop()] = -1

result = ""

for i in range(n):
	result += str(ans[i]) + ""

print(result)