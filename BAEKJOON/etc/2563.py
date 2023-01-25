import sys
input = sys.stdin.readline
r = 0
p = [[0]*101 for i in range(101)]
for _ in range(int(input())):
    a,b = map(int,input().split())
    for i in range(10):
        for j in range(10):
            p[a+i][b+j] = 1
for i in p:
    r += sum(i)
print(r)