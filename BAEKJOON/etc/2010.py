import sys
n = int(sys.stdin.readline())
sum = 0
for i in range(n):
    plug = int(sys.stdin.readline())
    sum = sum + plug
print(sum-(n-1))