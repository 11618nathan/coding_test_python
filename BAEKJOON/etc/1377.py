import sys
input = sys.stdin.readline

n = int(input())
a = []

for i in range(n):
    a.append((int(input()), i))

max = 0
s = sorted(a)

for i in range(n):
    if max < s[i][1] - i:
        max = s[i][1] - i

print(max + 1)